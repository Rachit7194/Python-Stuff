import os
import requests
import json
import MySQLdb as db
import time


DBHOST = 'localhost'
DBUSERNAME = 'root'
DBPASSWORD = 'quixom'
DBNAME = 'bookdata'


# db connection
def connect_db():
    connection = db.connect(host=DBHOST, user=DBUSERNAME, passwd=DBPASSWORD, db=DBNAME)
    return connection


# closing connection
def close_db(connection):
    connection.close()


def insert_book(item):
    title = item.get('title').replace('"', '\\"').encode('utf8')
    avail_to_down = item.get("availableToDownload")
    freelyAvailable = item.get("freelyAvailable")
    brief_Synopsis = item.get("briefSynopsis").replace('"', '\\"').encode('utf8')
    dtbookSize = item.get("dtbookSize")
    images = item.get("images")
    book_id = item.get("id")
    isbn_num = item.get("isbn13")
    publisher = item.get("publisher").replace('"', '\\"').encode('utf8')
    query = '''insert into bookdata.book(title, available_to_download, freely_available, images,
                                                brief_synopsis, dtbook_size, share_book_id, isbn13, publisher)
                                                 values
                                                 ("{title}", "{avail_to_down}", "{freelyAvailable}", "{images}", "{brief_Synopsis}", "{dtbookSize}", "{book_id}", "{isbn_num}", "{publisher}"  )'''.format(
        title=title, avail_to_down=avail_to_down, freelyAvailable=freelyAvailable, images=images,
        brief_Synopsis=brief_Synopsis, dtbookSize=dtbookSize, book_id=book_id, isbn_num=isbn_num, publisher=publisher)
    return execute_query(query)


def insert_author(item, book_id):
    authors = item.get("author")
    for author in authors:
        select_query = '''select id from bookdata.author where name = "{authors}" ; '''.format(authors=author.encode('utf8'))
        res = execute_select(select_query)
        if not len(res):
            query = '''insert into bookdata.author(name) values ("{authors}"); ''' .format(authors=author.encode('utf8'))
            author_id = execute_query(query)
        else:
            author_id = res[0][0]

        insert_related(book_id, author_id)
    return


def insert_related(book_id, author_id):
    query = '''insert into  bookdata.author_book_rel(book_id, author_id) values
                ({book_id}, {author_id} )'''.format(book_id=book_id, author_id=author_id)

    return execute_query(query)

def execute_query(query):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    # get id = cursor.lastrowid
    last_id = cursor.lastrowid
    cursor.close()
    return last_id

def execute_select(query):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def get_data(url=None, data=None, headers=None):
    # pass either a single urllib2.Request object, or a url,data,headers set to use
    r = json.loads(requests.get(url).text)
    return r



def extract_data():
    book = "https://api.bookshare.org/book/latest/format/json?api_key="
    api_key = "vrrqzd8bfn4yvwvmkefsfutz"
    mainurl = book + api_key
    data = get_data(mainurl)
    totalpages =  data['bookshare']['book']['list']['numPages']
    print type(totalpages)
    perpage =  data['bookshare']['book']['list']['page']
    for page in range(totalpages):
        page += 1
        book = "https://api.bookshare.org/book/latest/page/" + str(page)  + "/format/json?api_key="
        api_key = "vrrqzd8bfn4yvwvmkefsfutz"
        pageurl = book + api_key
        data = get_data(pageurl)
        # getconnnection
        finaldata = data['bookshare']['book']['list']['result']
        # print finaldata
        for item in finaldata:
            book_id = insert_book(item)
            insert_author(item, book_id)

        time.sleep(1)

extract_data()
