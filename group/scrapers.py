import requests
from bs4 import BeautifulSoup
import pandas as pd
import pdfplumber
import os

class scrapers:

    def pdf(NID, password):
        #from bs4 import BeautifulSoup
        #import requests
        s = requests.Session()
        loginUrl = 'https://ilearn2.fcu.edu.tw/login/index.php'
        page = s.get(loginUrl)
        data = BeautifulSoup(page.text, "html.parser")
        inputHtml = data.select('input[name="logintoken"]')  # 選擇input的標籤 且屬性name="logintoken"

        #NID = 'D0886096'
        #password = 'Ss6326969'
        token = inputHtml[0]['value']  # 抓logintoken的value
        loginPayload = {'username': NID, 'password': password, 'rememberusername': 1, 'anchor': None,
                        'logintoken': token}  # 這個是要post的帳號密碼

        loginResp = s.post(loginUrl, data=loginPayload)
        s.get("https://ilearn2.fcu.edu.tw/apps/apps_sso.php?log_lang=tw")
        s.get("https://myfcu.fcu.edu.tw/main/s3202/S3202_timetable_new.aspx")

        pdfFile = s.get("https://myfcu.fcu.edu.tw/main/s3202/timetable_print.aspx", params={"Y": 109, "S": 2})

        with open('課表.pdf', 'wb') as fd:
            fd.write(pdfFile.content)

    def readCourse():
        pdf = pdfplumber.open("課表.pdf")
        returnList = []
        p0 = pdf.pages[0]
        text = p0.extract_text()  # 讀文字
        count = 0
        p0 = pdf.pages[0]


        for table in p0.extract_tables():
            week = 1
            #print(table)
            for line in table:
                #print(line)
                if (line[2] != '' and count % 2 != 0 and count < 29):
                    #print(line[2].split('(')[0].replace('\n',''), week, line[0], '\n')
                    Course = {'CourseName': line[2].split('(')[0].replace('\n', ''), 'week': int(week),
                              'section': int(line[0])}
                    returnList.append(Course)
                count += 1
        count = 0

        for table in p0.extract_tables():
            week = 2
            for line in table:
                # print(line)
                if (line[3] != '' and count % 2 != 0 and count < 29):
                    #print(line[3], week, line[0], '\n')
                    Course = {'CourseName': line[3].split('(')[0].replace('\n', ''), 'week': int(week),
                              'section': int(line[0])}
                    returnList.append(Course)
                count += 1
        count = 0
        for table in p0.extract_tables():
            week = 3
            for line in table:
                # print(line)
                if (line[4] != '' and count % 2 != 0 and count < 29):
                    #print(line[4], week, line[0], '\n')
                    Course = {'CourseName': line[4].split('(')[0].replace('\n', ''), 'week': int(week),
                              'section': int(line[0])}
                    returnList.append(Course)
                count += 1
        count = 0
        for table in p0.extract_tables():
            week = 4
            for line in table:
                # print(line)
                if (line[5] != '' and count % 2 != 0 and count < 29):
                    #print(line[5], week, line[0], '\n')
                    Course = {'CourseName': line[5].split('(')[0].replace('\n', ''), 'week': int(week),
                              'section': int(line[0])}
                    returnList.append(Course)
                count += 1
        count = 0
        for table in p0.extract_tables():
            week = 5
            for line in table:
                #print(len(line))
                if len(line) < 7 :
                    continue
                if (line[6] != '' and count % 2 != 0 and count < 29):
                    #print(line[6], week, line[0], '\n')
                    Course = {'CourseName': line[6].split('(')[0].replace('\n', ''), 'week': int(week),
                              'section': int(line[0])}
                    returnList.append(Course)
                count += 1
        pdf.close()
        return returnList