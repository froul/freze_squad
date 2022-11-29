import re, os
import requests
from requests.structures import CaseInsensitiveDict
from config import Config
from lxml import etree
from loguru import logger
import xml.etree.ElementTree as ET
import re

CLIENT_ID = '3v5zx9xj9i9yvmvqlo125zwgr0ipfu'
client_id = CLIENT_ID
token = 'zcv69ewkup7ymlb3tjevchazdvehde'
#URL2 = "https://api.twitch.tv/helix/channels?broadcaster_id=85930341"


chan_name = "fr0u1" # - Переменная куда вписывать "НИК"



PARAMS2 = {
  "Client-ID": client_id,
  'Authorization': f"Bearer {token}"
}


URL_CHAN_NAME = "https://api.twitch.tv/helix/search/channels?query=" + chan_name + "&first=1"
URL_CHAN_NAME_REQ = requests.get(url = URL_CHAN_NAME, headers = PARAMS2)

text1 = URL_CHAN_NAME_REQ.text
text2 = text1.replace('"data"','')


text2 = text2.replace('{','')
text2 = text2.replace(':',' = ')
text2 = text2.replace('[','')
text2 = text2.replace(']','')
text2 = text2.replace('}','')
text2 = text2.replace('=',"")
text2 = text2.replace(' ',"")
text2 = text2.replace('"'," ")
text2 = text2.replace('  '," ")
text2 = text2.replace(',',"")
list_text2 = text2.split()
chanid = list_text2[11]
#print(list_text2)
#rint(text2)
if chanid == '85930341':
	print('Ты клоун? Сам на себя подписаться должен?')
	exit(0)


URL_EZE = "https://api.twitch.tv/helix/users/follows?from_id=" + chanid + "&to_id=85930341"
URL_TRIPL = "https://api.twitch.tv/helix/users/follows?from_id=" + chanid + "&to_id=791297037"
URL_KILLER = "https://api.twitch.tv/helix/users/follows?from_id=" + chanid + "&to_id=843002880"


r2 = requests.get(url = URL_EZE, headers = PARAMS2)
text1 = r2.text

text2 = text1.replace('"data"','')
text2 = text2.replace('{','')
text2 = text2.replace(':',' = ')
text2 = text2.replace('[','')
text2 = text2.replace(']','')
text2 = text2.replace('}','')
text2 = text2.replace('"broadcaster_id"','broadcaster_id')
text2 = text2.replace('"broadcaster_login"','broadcaster_login')
text2 = text2.replace('"broadcaster_name"','broadcaster_name')
text2 = text2.replace('"broadcaster_language"','broadcaster_language')
text2 = text2.replace('"game_id"','game_id')
text2 = text2.replace('"game_name"','game_name')
text2 = text2.replace('"title"','title')
text2 = text2.replace('"delay"','delay')
text2 = text2.replace(',',"\n")
text2 = text2.replace('=',"", 1)
text2 = text2.replace(' ',"", 2)

if text2.find('"total"1') != -1:
	text2 = 'Подписан на EZE MATIX' 
else: 
	text2 = 'Не подписан на EZE MATIX'

text_eze = text2
print(text2)

r2 = requests.get(url = URL_TRIPL, headers = PARAMS2)
text1 = r2.text

text2 = text1.replace('"data"','')
text2 = text2.replace('{','')
text2 = text2.replace(':',' = ')
text2 = text2.replace('[','')
text2 = text2.replace(']','')
text2 = text2.replace('}','')
text2 = text2.replace('"broadcaster_id"','broadcaster_id')
text2 = text2.replace('"broadcaster_login"','broadcaster_login')
text2 = text2.replace('"broadcaster_name"','broadcaster_name')
text2 = text2.replace('"broadcaster_language"','broadcaster_language')
text2 = text2.replace('"game_id"','game_id')
text2 = text2.replace('"game_name"','game_name')
text2 = text2.replace('"title"','title')
text2 = text2.replace('"delay"','delay')
text2 = text2.replace(',',"\n")
text2 = text2.replace('=',"", 1)
text2 = text2.replace(' ',"", 2)

if text2.find('"total"1') != -1:
	text2 = 'Подписан на triiplclick' 
else: 
	text2 = 'Не подписан на triiplclick'

text_trip = text2
print(text2)


r2 = requests.get(url = URL_KILLER, headers = PARAMS2)
text1 = r2.text

text2 = text1.replace('"data"','')
text2 = text2.replace('{','')
text2 = text2.replace(':',' = ')
text2 = text2.replace('[','')
text2 = text2.replace(']','')
text2 = text2.replace('}','')
text2 = text2.replace('"broadcaster_id"','broadcaster_id')
text2 = text2.replace('"broadcaster_login"','broadcaster_login')
text2 = text2.replace('"broadcaster_name"','broadcaster_name')
text2 = text2.replace('"broadcaster_language"','broadcaster_language')
text2 = text2.replace('"game_id"','game_id')
text2 = text2.replace('"game_name"','game_name')
text2 = text2.replace('"title"','title')
text2 = text2.replace('"delay"','delay')
text2 = text2.replace(',',"\n")
text2 = text2.replace('=',"", 1)
text2 = text2.replace(' ',"", 2)

if text2.find('"total"1') != -1:
	text2 = 'Подписан на killer__beauty' 
else: 
	text2 = 'Не подписан на killer__beauty'

text_killer = text2

print(text_killer)

sheets = requests.post(url = "https://script.google.com/macros/s/AKfycbwqwqVqAX8ALntDIUxqyLmErpzhBZVAphq6DEeE4pSm2oL7a2gfREkarJfrfxcGpoCf/exec?gid=1987211627", data={'Название канала':chan_name,'Основа 1':text_killer,'Основа 2':text_eze,'Основа 3':text_trip})
print(sheets)







'''
with open('data.xml', 'w') as f:
    f.write(r2.text)
if r2.status_code != 200:
    raise ValueError(f"Request add_user failed {r2.status_code}")
resp_xml_content = r2.content
print(f"{resp_xml_content}")
'''