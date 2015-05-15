#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs
import requests
import pymongo
import pprint

Main_Url = "http://api.nytimes.com/svc/"
Popular = "mostpopular/v2/"
API_key = "?api-key=b2f92fb98088b256316d8584e1aaca61:13:70248560"


def query_site(whattype, what_seciton, how_long):
    url = Main_Url + Popular + whattype + what_seciton + how_long + API_key
    r = requests.get(url)

    if r.status_code == requests.codes.ok:
        pprint.pprint(r.json()['results'])
        return r.json()
    else:
        r.raise_for_status()


def article_overview(data):
    # pprint.pprint(data)
    titles = {}
    article = data['results']
    # [x.encode('utf-8') for x in article]
    for a in article:
        print type(article)
        section = a['section'].replace('.', '')
        # print section
        # print len(section)
        title = a['title']
        # print title.encode('utf-8')
         
        titles.update({section: title})
    print len(titles)
    # pprint.pprint(titles)
    return titles


def mongo_save(dbwrite):
    connection = pymongo.MongoClient()
    db = connection.uda
    ls1 = db.ls1

    ls1.save(dbwrite)


if __name__ == "__main__":
    data = query_site('mostviewed', '/all-sections/', '1')
    dbwrite = article_overview(data)  
    # mongo_save(dbwrite)

# pprint.pprint(article_overview(data))

