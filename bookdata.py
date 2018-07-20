import os
import urllib2
import bookdb
import json


def request(request=None, url=None, data=None, headers=None):
 #pass either a single urllib2.Request object, or a url,data,headers set to use
    if request is not None:
      return urllib2.urlopen(request)
    else:
      return urllib2.urlopen(url, data, headers)

def extract_data():
    book = "https://api.bookshare.org/book/latest/format/json?"
    api_key = "vrrqzd8bfn4yvwvmkefsfutz"
    latest_book = book + api_key
    print latest_book
    data = json.loads(request(latest_book)
    # finaldata = data['bookshare']['book']['list']['result']
    # for item in finaldata:
    #     title = item.get('title')
    #     auth = item.get('author')
    #     avail_to_down = item.get("availableToDownload"))
    #     brief_Synopsis = item.get("briefSynopsis")
    #     dtbookSize = item.get("dtbookSize")
    #     book.id = item.get("id")
    #     isbn_num = item.get("isbn13")
    #     publisher = item.get("publisher")



extract_data()