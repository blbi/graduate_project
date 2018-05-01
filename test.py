from bs4 import BeautifulSoup as bs
import urllib
import pymysql
import requests

#list pool
raw_url = []
url_info_list = []

#match attribute in cosmetic table
def match_cos_subtype(subtype) :
	return {'0':"lip", '1':"mascara",'2':"blusher",'3':"shadow",'4':"shading",'5':"eyeliner",'6':"eyebrow",'7':"highlighter"}.get(subtype,"dc")

def match_base_cos_ton(ton) :
	return {'0':"warm",'1':"cool"}.get(ton,"dc")

def match_base_cos_skintype(skintype) :
	return {'0':"gi", '1':"gun",'2':"gok"}.get(skintype,"dc")

def match_base_cos_per_season(season) :
	return {'0':"spring", '1':"summer",'2':"fall",'3':"winter"}.get(season,"dc")

def match_cos_enter(enter) :
	return {'0':"nature", '1':"theface",'2':"mis",'3':"ari",'4':"atude",'5':"olive",'6':"innisfree",'7':"tony"}.get(enter,"dc")

#match attribute in basecos table
def match_base_subtype(subtype) :
	return {'0':"lotion", '1':"skin",'2':"concealer",'3':"cushion",'4':"cream",'5':"foundation",'6':"fact",'7':"bb"}.get(subtype,"dc")

def match_base_enter(enter) :
	return {'0':"thesam", '1':"theface",'2':"mis",'3':"skinfood",'4':"aritaum",'5':"olive",'6':"innisfree",'7':"tony"}.get(enter,"dc")

#match attribute in tool table
def match_tool_subtype(subtype) : 
	return {'0':"lipbrush",'1':"eyelashcurler",'2':"brushset",'3':"eyebrush",'4':"artificialeyelashes",'5':"puff",'6':"facebrush"}.get(subtype,"dc")

def match_tool_brush(brush) :
	return {'0':"artificial",'1':"nature"}

#match attribute in perfume table
def match_perfume_brand(brand) :
	return {'0':"끌로에",'1':"랑방",'2':"클린",'3':"불가리",'4':"존바바토스",'5':"지미추"}.get(brand,"dc")

def match_perfume_sex(sex) :
	return {'0':"male",'1':"female"}.get(sex,"dc")

def match_perfume_keyword(keyword) :
	return {'0':"새내기",'1':"연예인",'2':"10대",'3':"20대",'4':"30대",'5':"40대"}.get(keyword,"dc")

#match attribute in hair table
def match_hair_subtype(subtype) :
	return {'0':"린스",'1':"샴푸",'2':"스프레이",'3':"에센스",'4':"염색약",'5':"왁스",'6':"팩"}.get(subtype,"dc")

def match_hair_hairtype(hairtype) :
	return {'0':"gi",'1':"gun"}.get(hairtype,"dc")

#about cosmetic table
def select_url(user_input) :
	global raw_url
	query = ""

	if (user_input[0] == '0') : 
		table = "cosmetic"
		subtype = match_cos_subtype(user_input[1])
		ton = match_base_cos_ton(user_input[2])
		skintype = match_base_cos_skintype(user_input[3])
		season = match_base_cos_per_season(user_input[4])
		enter = match_cos_enter(user_input[5])

		#select query
		query = """select url from %s where subtype = "%s" and ton = "%s" and skintype = "%s" and season = "%s" and enter = "%s";"""%(table, subtype, ton, skintype, season, enter)
	elif (user_input[0] == '1') :
		table = "basecos"
		subtype = match_base_subtype(user_input[1])
		ton = match_base_cos_ton(user_input[2])
		skintype = match_base_cos_skintype(user_input[3])
		season = match_base_cos_per_season(user_input[4])
		enter = match_base_enter(user_input[5])
		#query = """ 추가하면 됨... """

	elif (user_input[0] =='2') :
		table = "tool"
		subtype = match_tool_subtype(user_input[1])
		brush = match_tool_brush(user_input[2])
		#query = """ 추가하면 됨... """

	elif (user_input[0] =='3') :
		table = "perfume"
		brand = match_perfume_brand(user_input[1])
		sex = match_perfume_sex(user_input[2])
		season = match_base_cos_per_season(user_input[3])
		keyword = match_perfume_keyword(user_input[4])
		#query = """ 추가하면 됨... """

	elif (user_input[0] =='4') :
		table = "hair"
		subtype = match_hair_subtype(user_input[1])
		hairtype = match_hair_hairtype(user_input[2])
		#query = """ 추가하면 됨... """
		
	cur.execute(query)
	raw_url = cur.fetchall()

#extract view_count, like_count, title
def extract_info(youtube_url) : 
	resp = requests.get(youtube_url)
	soup = bs(resp.text, "html.parser")

	view = soup.find("span","view-count").get_text().split(' ')[1].replace("회","").replace(",","")
	view_count = int(view)

	like = soup.find_all("span","yt-uix-button-content")[20].get_text().replace(",","")
	like_count = int(like)

	hate = soup.find_all("span","yt-uix-button-content")[25].get_text().replace(",","")
	hate_count = int(hate)

	time = soup.find_all("span","ytp-time-duration")

	title = soup.find("span","watch-title").get_text().replace(" ","").replace("\n","")
	#f = open("C:/users/thakd/desktop/유튜브.txt",'wb')
	#f.write(resp.text.encode('utf-8'))

	return {"ratio":like_count/hate_count, "view_count":view_count,"title":title,"url":youtube_url}

def user_input() :
	category = input("첫자리 : 0~5(table 5개 + dc테이블)\n둘째~여섯째 자리 : 0~8(아홉개) 범위 입력\n")	
	select_url(category)
	if(len(raw_url)>1) :
		for i in range(0,len(raw_url)) :
			url_info_list.append(extract_info(raw_url[i][0]))
	else :
		url_info_list[0] = extract_info(raw_url[i][0])
		print(url_info_list)
	#for i in range(0,len(url)) :
	#	print(extract_info(url[i][0]).get("ratio"))

def output_url_list() :
	newlist = sorted(url_info_list, key=lambda k: (k["ratio"], k["view_count"]), reverse=True)
	return newlist

if __name__ =='__main__' :
	#connect db first
	db = pymysql.connect(host="localhost", user="thakd", password="sjaqj15951!", db="mydb")
	cur = db.cursor()
	cur.execute("use mydb")

	user_input()
	url_info_list = output_url_list()
	print("sorted url :: ")
	print(url_info_list)
	db.close()