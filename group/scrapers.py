from bs4 import BeautifulSoup
import requests
s = requests.Session()
url='https://myfcu.fcu.edu.tw/main/infomyfculogin.aspx'
page = s.get(url)

NID = input("學號:")
password = input("密碼:")

data = BeautifulSoup(page.text, "html.parser")
token = data.select('input[name="logintoken"]') #選擇input的標籤 且屬性name="logintoken"
value = token[0]['value']    #抓logintoken的value

data={'username':NID,'password':password,'logintoken':value} #這個是要post的帳號密碼
page2 = s.post(url,data=data)
data2 = BeautifulSoup(page2.text, "html.parser")
course = data2.select("div.name")         #select課程名稱
teacher = data2.select("div.teachers")    #select老師名稱

for i,v in enumerate(course):             #印出
    print(v.select("a")[0]['title'] + '  ' + teacher[i].select("span")[0].text)

'''
ScriptManager1: UpdatePanel1|OKButton
__LASTFOCUS: 
__EVENTTARGET: 
__EVENTARGUMENT: 
__VIEWSTATE: /wEPDwUJNTEwMzE5ODM5DxYCHgxJc01hc3RlclBhZ2VkFgQCAw8PFgIeBFRleHQFJDwhLS0gVGhpcyBQYWdlIGlzIG5vcm1hbCBkaXNwbGF5IC0tPmRkAgUPZBYCAgUPZBYCZg9kFg4CAQ8PFgIfAQUG55So5oi2ZGQCBQ8PFgIfAQUG5a+G56K8ZGQCCQ8PFgIfAQUJ6LOH5paZ5bqrZGQCCw8QZA8WAmYCARYCEAULTUlTREJTRVJWRVIFC01JU0RCU0VSVkVSZxAFDk1JU0RCU0VSVkVSQURPBQ5NSVNEQlNFUlZFUkFET2cWAWZkAg0PEA8WAh8BBQzoqJjkvY/lr4bnorxkZGRkAhkPDxYCHwEFBuaWueahiGRkAhsPEA8WCh4KRGF0YU1lbWJlcgUGVGFibGUxHg1EYXRhVGV4dEZpZWxkBQhpdGVtbmFtZR4ORGF0YVZhbHVlRmllbGQFCGl0ZW10eXBlHgtfIURhdGFCb3VuZGceDEF1dG9Qb3N0QmFja2hkEBUDB0ZjdUFwcHMJRmN1UHRBcHBzCEZjdUVBcHBzFQMHRmN1QXBwcwlGY3VQdEFwcHMIRmN1RUFwcHMUKwMDZ2dnFgFmZGTukIoLV1vQdJGW9cEdOhoVP8/j6w==
__VIEWSTATEGENERATOR: 49CFD8FD
__SCROLLPOSITIONX: 0
__SCROLLPOSITIONY: 0
__EVENTVALIDATION: /wEWBQLMwIu1BwKGnL+QDwKl1bKzCQK1qbSRCwKOoeEv1y7HUqvpYx14ZzqoMZ4PzMlVxgY=
txtUserName: D0886096
txtPassword: Ss6326969
__ASYNCPOST: true
OKButton: login
'''