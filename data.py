# import datetime, time
# now = datetime.time()
# print now - datetime.timedelta(days=1) <= self.pub_date <= now
# from bs4 import BeautifulSoup
# import requests

# url = "https://www.tennis-point.fr/index.php?stoken=737F2976&lang=1&cl=search&searchparam=E705Y-0193"

# # Getting the webpage, creating a Response object.
# response = requests.get(url)

# # Extracting the source code of the page.
# data = response.text

# # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
# soup = BeautifulSoup(data, 'html.parser')
# # print soup
# urls =[ item.get("href") for item in soup.find_all("a")]
# print(urls)
# # 

# # 
# line = '''<form id="main">\n
# <input {disable}  style="display:none" id="CALLERID" value = "58713780" >\n
# <input{disable} style = "display:none" id = "GR_BUS" value = "VGH1"\n >
# < td >< inputid = "label"{disable}style = "font-size: 9px;width: 100 %;margin: 0;padding: 1;" type=text></td>
# </form>>'''

# line = '''RPM,Load Current,Output
# 1200,3,12
# 1500,4,13'''

# line  = '''
# <form action="/adjust_table.py" method="post">
#   <table>
#     <tr>
#     <td colspan = 4><input type="text" name="id" value="123" readonly></td>
#     <td colspan = 4>name: George</td>
#     <td colspan = 4>age: <input type="text" name="age[123]" value="73"></td>
#     </tr>
#     <tr>
#     <td colspan = 4><input type="text" name="id" value="1269" readonly></td>
#     <td colspan = 4>name: Jake</td>
#     <td colspan = 4>age: <input type="text" name="age[1269]" value="26"></td>
#     </tr>
#     <input type="submit" value="Submit">
#   </table>
# </form>'''



# from bs4 import BeautifulSoup

# soup = BeautifulSoup(line)
# for values in soup.findAll("td"):
#     print values.text




# while count(5,10):
# 	print count
# 	print count.next
# while count(0,5):
# 	if count <= 5:
# 		break
# 	print count
	
# from itertools import count
# for i in count(0):
# 	if i >= 5:break
# 	print i
# 	with open(r"test {0}".format(str(i)), "w") as file:
# 		file.write("Hello World")
# print "HI"
# info=['kirsty','32','germany']
# df = pd.read_csv('hexdata.csv')
# import json
# csv_file = pd.DataFrame(pd.read_csv("hexdata.csv", sep = ",", header = 0, index_col = False))
# data = json.loads(csv_file.to_json())
# print type(data)
# f = [values for keys,values in json.dumps(data.items())]
# print f
# final = data.items()
# print df2
# df.append(["name"]) = 'info' 
# df2 = pd.Series(info, index=["name", "age",
# 	"country"])

# df=df.append(pd.Series(np.array([0])),ignore_index=True)
# df.append(df2)
# print df.drop_duplicates()
# df.drop_duplicates(subset='1', keep="last")
# li = [{"employee_id":1,"project_handled": "pas"},{"employee_id":1,"project_handled": "asap"},{"employee_id":2,"project_handled": "trimm"},{"employee_id":2,"project_handled": "fat"}]
# df = pd.DataFrame(li)
# df.set_index("YES", inplace=True)
# print(df)
# print df2

# with open("sample.txt", 'r') as file:
# 	print file.read()
# import json

#=================================***********************************=================================
# import pandas as pd
# df = pd.read_csv("sample.txt", sep=" " , names=["Host", "Version"])
# # print dir(df)
# t = []
# for item, item1 in zip(df["Host"], df["Version"]):
# 	print item1
# 	# break
    # if "Hostname" in item[0] or "version" in item[0]:
    #     # t.append(item[0]) +  " : " + str(item[1])
    #     t.append(item[1])
# df['t'] = t
# print df
# print df.to_html(index=False)

#=================================***********************************=================================
# f = {}
# d = []
# for item in zip(df["Host"], df["Version"]):
#     if "version" in item[0]:
#     	d.append(item[1])
#         print(item[0] +  " : " + str(item[1]))

# print "=============================================================="
# print d
# print type(df)
# print set([(item1) for item, item1 in zip(df["Host"], df["Version"]) if "Hostname" or "version" in item and "Hostname" or "version" in item1])
	# if "version" in item:
		# print item + "--------" + item1
		# print "++++"
		# break
	# 	final_data[item[]] =str(item[1])


# print "-----------------------------------"
# print final_data
# print "-----------------------------------"
# data = json.loads(df.to_json())
# print data
# for (k,v), (k2,v2) in zip(d.items(), d2.items()):
# import subprocess
# subprocess.call(["python", r"C:\Users\Quixom\AppData\Roaming\Kodi\userdata\addon_data\script.smoothstreams-v3\test.py"], stdout=subprocess.PIPE)
# def chk_string(item):
# 	x = lambda items: item.lower() if isinstance(item, str) is True else item
# 	print x
# 	return x

# l = ["HEllo", "World", 123]
# x = map(lambda item: item.lower() if isinstance(item, str) is True else item, l)
# print(x)

# print([chk_string(x) for x in l])
# import time
# s =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(time.time()))).split("")
# print s






# newList = []
# quan = 0
# for i in range(0,len(user)):      
#     originator = user[i]['name']
#     for j in range(i+1,len(user)):
#         if originator == user[j]['name']:
#             quan = user[i]['quantity'] + user[j]['quantity']
#             newList.append({'name': originator, 'Quantity': quan})


# x = 3
# def run():
# 	global x
# 	return x

# x+=1
# run()
# print(x)

# animals = ['LION', 'TIGER', 'DEER', 'CHICKEN']
# new_catch = []
# farm = [{'LION':'carnivorous', 'legs': 4 , 'strength': 98.7, 'kills': True},
# {'TIGER':'carnivorous', 'legs': 4 , 'strength': 100.18, 'kills': True},
# {'DEER':'harbivorous', 'legs': 4, 'speed': 87.3, 'kills': False},
# {'CHICKEN':'null', 'legs': 2, 'speed': 5, 'strength':2.3, 'kills': False},
# {'PIG': 'omnivorous', 'legs': 4, 'strength': 55.0, 'kills': True, 'speed':64}]

# # while not(new_catch in animals):    
# while not(new_catch in animals):    
#   animal = input("give me a:... ").upper()
#   for farmanimals in farm:
#    for key, value in farmanimals.items():
#       if animal in farmanimals:
#          print('')
#          print("#{}:{}".format(key, value))
#          print('') 
# else:
#   new_catch.append(animal)
#   print("sorry, {} is not available!!".format(new_catch))
#   print(new_catch)



# class Point():
#     def __init__(self,pointCoords):
#         self.coords = np.array([round(i,8) for i in pointCoords])
#     def __str__(self):
#         return "Point with coords: {0}".format(self.coords)
#     def getCoords(self):
#         return self.coords

# import lxml.etree as etree

# from bs4 import BeautifulSoup
# with open("sample.xml", "r") as f: # opening xml file
#     content = f.read().decode('utf-8', 'ignore') # xml content stored in this variable and decode to utf-8

# soup = BeautifulSoup(content, 'html.parser') #parse content to BeautifulSoup Module
# data = [data.attrsfor data in soup.findAll("test")]

	# if data.startswith("xmlns"):
	# 	print data
	# print dir(data)
	# print data.get("xmlns")
# print [data for data in soup.findAll('xmlns')]
 
# print dir(soup)
# print soup.find('test')
# print soup.find_all("test")

# from xml.etree.ElementTree import parse
# xml_doc = parse("sample.xml")
# xml_root = xml_doc.getroot()
# print xml_root.get("xmlns")
# for cat in xml_root:
# 	print cat
# 	print cat.attrib['xmlns']
# print dir(xml_root)
# url = 'https://www.timeshighereducation.com/world-university-rankings/2018/world-ranking#!/page/0/length/25/sort_by/rank/sort_order/asc/cols/stats'
# import requests
# from bs4 import BeautifulSoup
# html_content = requests.get(url).content
# soup = BeautifulSoup(html_content, 'lxml')
# print soup.find_all("tr")
# print [ data.text for data in soup.find_all('table')]
# class Person(object):
#     age = 0
#     name = ''
#     def __init__(self,personAge,personName):
#         self.age = personAge
#         self.name= personName

#     def __str__(self):
#         return self.name


# d = Person(24,'ram')
# print d

# import pandas as pd
# theList= ["ABCD","EFGH","IJKL","MNOP"]
# company = pd.DataFrame(columns=theList)
# data = company.to_csv("sample.csv")
# import yaml as y
# Movies = pd.read_csv('tmdb_5000_movies.csv',encoding="ISO-8859-1")
# company = pd.DataFrame(Movies[['original_title','production_companies']])
# for idn in range(10000):
# for index in range(len(company['original_title'])):
#     akm = y.load(company.loc[index,'production_companies'])
#     for i in range(len(akm)):
#         if akm[i]['id'] == idn:
#             if str(idn) not in keyword.columns:
#                 keyword[str(idn)] = " "    
#                 keyword.loc[index,str(idn)] = 1
#             elif str(idn) in keyword.columns:
#                 keyword.loc[index,str(idn)] = 1
#             # check if akm == idn
#         # akm length
# keyword = keyword.fillna(0)
# html_data = """
# <span class="some_data">
#         title 1 : data 1
#         <br/>
#         title 2 : data 2
#         <br/>
#         title 3 : data 3
#         <br/>
#         <span class="meta_data">
#             other additional data
#         </span>
# </span>
# """

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_data, 'html.parser') #parse content to BeautifulSoup Module
# tags = soup.find("span", {"class":"some_data"}).text.strip("\n").split("\t")
# print set(tags[0].split(" "))

	# break
	# if item.isalpha():
	# 	print item
# Extracting all the <a> tags into a list.
# tags = soup.find("div", {"class": "productsPicture"}).findAll("a")
# print tags
# Extracting URLs from the attribute href in the <a> tags.
# for tag in tags:
#     print(tag.get('href'))

# import requests
# from bs4 import BeautifulSoup

# # I am only interested in some particular blocks from the bitcoin blockchain
# url = "https://blockchain.info/block-height/521578"

# # Getting table from the url
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# stat_table = soup.find_all('table', class_ = 'table table-striped')
# stat_table = stat_table[0]
# for row in stat_table.find_all("tr"):
# 	    for cell in row.find_all("td")[1:].rstrip(): # look that I am interested only in the 2nd column
# 	    	print(cell.text.rstrip())

data = """<ul class="also">
    <li>once as the adjective <i class="ab">abdrea</i> (<span class="at">groups</span>)</li>
    <li>twice as the noun <i class="ab">shokdia</i> (<span class="at">techs</span>)</li>
</ul>"""


# # with open("sample.xml", "r") as f: # opening xml file
#     # content = f.read() # xml content stored in this variable and decode to utf-8
# from bs4 import BeautifulSoup
# import json
# data = """<div class="title" style="visibility: visible"> </div>"""
# soup = BeautifulSoup(data, 'html.parser') #parse content to BeautifulSoup Module
# div_content = dict(soup.find("div").attrs)
# print("div_content   :  {0}".format(div_content)) #div content
# print("style_content :  {0}".format(div_content.get("style"))) # style attribute
# print("class_content :  {0}".format(div_content.get("class")[0])) # class attribute
# print(soup.select('tr').text)
# # print [i.text for i in soup.find_all("line")][0] + str([i.text for i in soup.find_all("li")][1])

#   # if i.get("class") == "specChecked":
#   #   print [str(i.get("class", ''))  + "," + str(i.text) for i in soup.find_all("li")]
#   #   print "\n"

# line = """<img id="webfast-uhyubv" alt="" data-type="image" id="comp-jefxldtzbalatamediacontentimage" src="http://webfast.co/images/webfast-logo.png" /> """
# # print [data for data in soup.find_all("d")]
# import requests

headers = {"User-Agent": "Mozilla/5.0(Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}

# url = "https://www.google.co.in/search?rlz=1C1CHBD_enIN789IN790&ei=iWj5WouoDsfGvgSr16bwDg&q=United+States%09KEEP+SMILIN+FAMILY+DENTAL%092281+N+ZARAGOZA+RD+STE+102&oq=United+States%09KEEP+SMILIN+FAMILY+DENTAL%092281+N+ZARAGOZA+RD+STE+102&gs_l=psy-ab.12...1153407.1153407.0.1154512.0.0.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..0.0.0....0.YvWjU-kIBUs"
# from bs4 import BeautifulSoup
# # s=requests.get(url, headers=HEADERS)
# soup =BeautifulSoup(line,'lxml')
# print soup.findAll("img")
# print soup.string
# data=  soup.findAll("div",{"class":"zloOqf kpS1Ac vk_gy"})
# print data
# final_d=  data[0].find("span")
# print final_d.text
# actual_data = [item.get("") for item in data]
# print actual_data
import requests, json

data = """<ul class="also">
    <li>once as the adjective <i class="ab">abdrea</i> (<span class="at">groups</span>)</li>
    <li>twice as the noun <i class="ab">shokdia</i> (<span class="at">techs</span>)</li>
</ul>"""

from bs4 import BeautifulSoup
page_soup = BeautifulSoup(data, "html.parser")
i_data, span_data= zip([x.text for x in page_soup.find_all("i")], [y.text for y in page_soup.find_all("span")])
 
print(i_data )
print(span_data)
