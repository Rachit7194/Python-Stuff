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
    try:
        brief_Synopsis = item.get("briefSynopsis").replace('"', '\\"').encode('utf8')
    except AttributeError as e:
        brief_Synopsis = None

    dtbookSize = item.get("dtbookSize")
    images = item.get("images")
    book_id = item.get("id")
    isbn_num = item.get("isbn13")

    try:
        publisher = item.get("publisher").replace('"', '\\"').encode('utf8')
    except AttributeError as e:
        publisher = None


    select_query = '''select id from bookdata.book where isbn13 = "{isbn}" ; '''.format(isbn=isbn_num)
    res = execute_select(select_query)
    if not len(res):
        query = '''insert into bookdata.book(title, available_to_download, freely_available, images,
                                                    brief_synopsis, dtbook_size, share_book_id, isbn13, publisher)
                                                     values
                                                     ("{title}", "{avail_to_down}", "{freelyAvailable}", "{images}", "{brief_Synopsis}", "{dtbookSize}", "{book_id}", "{isbn_num}", "{publisher}"  )'''.format(
            title=title, avail_to_down=avail_to_down, freelyAvailable=freelyAvailable, images=images,
            brief_Synopsis=brief_Synopsis, dtbookSize=dtbookSize, book_id=book_id, isbn_num=isbn_num, publisher=publisher)
        id =  execute_query(query)
    else:
        id = res[0][0]
    return id


def insert_author(item, book_id):
    authors = item.get("author")
    for author in authors:
        author = author.replace('"', '\\"').encode('utf8')
        select_query = '''select id from bookdata.author where name = "{authors}" ; '''.format(authors=author)
        res = execute_select(select_query)
        if not len(res):
            query = '''insert into bookdata.author(name) values ("{authors}"); ''' .format(authors=author)
            author_id = execute_query(query)
        else:
            author_id = res[0][0]

        insert_related(book_id, author_id)
    return



def insert_related(book_id, author_id):
    select_query = '''select id from bookdata.author_book_rel where author_id = "{aid}" and book_id = "{bid}" ; '''.format(aid=author_id, bid=book_id)
    res = execute_select(select_query)
    if not len(res):
        query = '''insert into  bookdata.author_book_rel(book_id, author_id) values
                    ({book_id}, {author_id} )'''.format(book_id=book_id, author_id=author_id)
        id = execute_query(query)
    else:
        id = res[0][0]
    return  id

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
    # if "'<>() " in url:
    #     print "sff"
    #     url1 = url.strip("'<>() ")
    #     mainurl = url1.replace('\'', '\"')
    try:
        page = requests.get(url)
        r = json.loads(page.text)
    except Exception as e:
        print e
    # else:
    #     r = requests.get(url).json()
    return r



def popularbooks_extract_data():
    print "dsfdffgG"
    book = "https://api.bookshare.org/book/popular/format/json?api_key="
    api_key = "vrrqzd8bfn4yvwvmkefsfutz"
    mainurl = book + api_key
    data = get_data(mainurl)
    totalpages =  data['bookshare']['book']['list']['numPages']
    perpage =  data['bookshare']['book']['list']['page']
    for page in range(totalpages):
        page += 1
        book = "https://api.bookshare.org/book/popular/page/" + str(page)  + "/format/json?api_key="
        api_key = "vrrqzd8bfn4yvwvmkefsfutz"
        pageurl = book + api_key
        print pageurl
        data = get_data(pageurl)
        # getconnnection
        finaldata = data['bookshare']['book']['list']['result']
        # print finaldata
        for item in finaldata:
            book_id = insert_book(item)
            insert_author(item, book_id)

        time.sleep(1)

def latestbooks_extract_data():
    book = "https://api.bookshare.org/book/latest/format/json?api_key="
    api_key = "vrrqzd8bfn4yvwvmkefsfutz"
    mainurl = book + api_key
    data = get_data(mainurl)
    totalpages = data['bookshare']['book']['list']['numPages']
    print type(totalpages)
    perpage = data['bookshare']['book']['list']['page']
    for page in range(totalpages):
        page += 1
        book = "https://api.bookshare.org/book/latest/page/" + str(page) + "/format/json?api_key="
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

# popularbooks_extract_data()

if __name__ == '__main__':
    popularbooks_extract_data()
    latestbooks_extract_data()
