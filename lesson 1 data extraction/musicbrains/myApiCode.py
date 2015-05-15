import musicbrainzngs
import os
import pprint


musicbrainzngs.set_useragent('jmusic', '0.0.1', contact="@bigjeffdogg")

artist_id = "c5c2ea1c-4bde-4f4d-bd0b-47b200bf99d6"
try:
    result = musicbrainzngs.get_artist_by_id(artist_id)
    print result['artist'].keys()
except WebServiceError as exc:
    print("Something went wrong with the request: %s" % exc)
else:
    artist = result["artist"]
    print artist.keys()
    print("name:\t\t%s" % artist["name"])
    print("sort name:\t%s" % artist["sort-name"])

    print iter(artist)
    print artist.get('id')
    pairs = [(v,k) for (k,v) in artist.iteritems()]
    print pairs
    


result = musicbrainzngs.get_artist_by_id(artist_id,
              includes=["release-groups"], release_type=["album", "ep"])
for release_group in result["artist"]["release-group-list"]:
    print("{title} ({type})".format(title=release_group["title"],
                                    type=release_group["type"]))

release_id = "46a48e90-819b-4bed-81fa-5ca8aa33fbf3"
data = musicbrainzngs.get_cover_art_list("46a48e90-819b-4bed-81fa-5ca8aa33fbf3")
for image in data["images"]:
    if "Front" in image["types"] and image["approved"]:
        print "%s is an approved front image!" % image["thumbnails"]["large"]
        brea