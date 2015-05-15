#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import locale
import os
import sys
import unicodedata

from kitchen.text.converters import getwriter, to_bytes, to_unicode
from kitchen.i18n import get_translation_object

if __name__ == '__main__':
    # Setup gettext driven translations but use the kitchen functions so
    # we don't have the mismatched bytes-unicode issues.
    translations = get_translation_object('example')
    # We use _() for marking strings that we operate on as unicode
    # This is pretty much everything
    _ = translations.ugettext
    # And b_() for marking strings that we operate on as bytes.
    # This is limited to exceptions
    b_ = translations.lgettext

    # Setup stdout
    encoding = locale.getpreferredencoding()
    Writer = getwriter(encoding)
    sys.stdout = Writer(sys.stdout)

    # Load data.  Format is filename\0description
    # description should be utf-8 but filename can be any legal filename
    # on the filesystem
    # Sample datafile.txt:
    #   /etc/shells\x00Shells available on caf\xc3\xa9.lan
    #   /var/tmp/file\xff\x00File with non-utf8 data in the filename
    #
    # And to create /var/tmp/file\xff (under bash or zsh) do:
    #   echo 'Some data' > /var/tmp/file$'\377'
    datafile = open('datafile.txt', 'r')
    data = {}
    for line in datafile:
        # We're going to keep filename as bytes because we will need the
        # exact bytes to access files on a POSIX operating system.
        # description, we'll immediately transform into unicode type.
        # b_filename, description = line.split('\0',2)

        # to_unicode defaults to decoding output from utf-8 and replacing
        # any problematic bytes with the unicode replacement character
        # We accept mangling of the description here knowing that our file
        # format is supposed to use utf-8 in that field and that the
        # description will only be displayed to the user, not used as
        # a key value.
        description = to_unicode(line, 'utf-8').strip()
        # data[b_filename] = description
    datafile.close()

    # We're going to add a pair of extra fields onto our data to show the
    # length of the description and the filesize.  We put those between
    # the filename and description because we haven't checked that the
    # description is free of NULLs.
    datafile = open('newdatafile.txt', 'w')

    # Name filename with a b_ prefix to denote byte string of unknown encoding
    for b_filename in data:
        # Since we have the byte representation of filename, we can read any
        # filename
        if os.access(b_filename, os.F_OK):
            size = os.path.getsize(b_filename)
        else:
            size = 0
        # Because the description is unicode type,  we know the number of
        # characters corresponds to the length of the normalized unicode
        # string.
        length = len(unicodedata.normalize('NFC', description))

        # Print a summary to the screen
        # Note that we do not let implici type conversion from str to
        # unicode transform b_filename into a unicode string.  That might
        # fail as python would use the ASCII filename.  Instead we use
        # to_unicode() to explictly transform in a way that we know will
        # not traceback.
        print _(u'filename: %s') % to_unicode(b_filename)
        print _(u'file size: %s') % size
        print _(u'desc length: %s') % length
        print _(u'description: %s') % data[b_filename]

        # First combine the unicode portion
        line = u'%s\0%s\0%s' % (size, length, data[b_filename])
        # Since the filenames are bytes, turn everything else to bytes before combining
        # Turning into unicode first would be wrong as the bytes in b_filename
        # might not convert
        b_line = '%s\0%s\n' % (b_filename, to_bytes(line))

        # Just to demonstrate that getwriter will pass bytes through fine
        print b_('Wrote: %s') % b_line
        datafile.write(b_line)
    datafile.close()

    # And just to show how to properly deal with an exception.
    # Note two things about this:
    # 1) We use the b_() function to translate the string.  This returns a
    #    byte string instead of a unicode string
    # 2) We're using the b_() function returned by kitchen.  If we had
    #    used the one from gettext we would need to convert the message to
    #    a byte str first
    message = u'Demonstrate the proper way to raise exceptions.  Sincerely,  \u3068\u3057\u304a'
    raise Exception(b_(message))