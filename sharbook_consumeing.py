import requests
import MySQLdb as db
import json

# database info
DBHOST = 'localhost'
DBUSERNAME = 'root'
DBPASSWORD = 'soni'
DBNAME = 'bookdata'

api_key = "vrrqzd8bfn4yvwvmkefsfutz"
base_url = "http://api.bookshare.org/book/search/author/"


def get_author():
	authorlist = []
	with open('authorlist.txt','r') as f:
		authorlist = f.readlines()
		return authorlist

# db connection
def connect_db():	
	connection = db.connect( host = DBHOST, user = DBUSERNAME, passwd = DBPASSWORD, db = DBNAME)
	return connection

# closing connection
def close_db():
	connection.close()


# getting data
def get_data():
	connection = connect_db()

	query_string = ""
	for author in get_author():
		url = ""
		url = base_url + author
		url += "/format/json?api_key="
		url += api_key

		r = requests.get(url)
		
		jdata = json.loads(r.text)

		book_list = jdata['bookshare']['book']['list']
		total_page = book_list['numPages']
		result = book_list['result']
		for book in result:
			book_authors = book['author']
			brifsynopsis = book['briefSynopsis'].replace('"', r'\"')


			query = '''insert into bookdata.book(title, publisher, isbn13, brief_synopsis, share_book_id, available_to_download, \
				dtbook_size, freely_available) values("%s","%s",%s,"%s",%s,%s,%s,%s)'''%( 
								book['title'], book.get('publisher'), book.get('isbn13'), brifsynopsis, book['id'], 
								book['availableToDownload'], book['dtbookSize'], book['freelyAvailable']
								)

			cursor = connection.cursor()
			cursor.execute(query)
			cursor.close()




get_data()


