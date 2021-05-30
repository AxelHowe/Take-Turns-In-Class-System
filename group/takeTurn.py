''' 我存課表資料用的code
NIDs = NID.objects.filter(User=UserID)
    nids = []
    courses = []
    for i,v in enumerate(NIDs):
        nids.append(v)
        course = Course.objects.filter(NID=v)
        temp=[]
        for j,value in enumerate(course):
            tmp = {'CourseName':value.CourseName, 'week':value.week, 'section':value.section}
            temp.append(tmp)
        courses.append(temp)
'''

nid = ['D0886096', 'D0886108', 'D0886112', 'D0886172']
courses = [[{'CourseName': '程式設計', 'week': 1, 'section': 1}, {'CourseName': '', 'week': 2, 'section': 1}, {'CourseName': '', 'week': 3, 'section': 1}, {'CourseName': '', 'week':
 4, 'section': 1}, {'CourseName': '', 'week': 5, 'section': 1}, {'CourseName': '', 'week': 6, 'section': 1}, {'CourseName': '', 'week': 7, 'section': 1}, {'CourseName':
'程式設計', 'week': 1, 'section': 2}, {'CourseName': '系統程式', 'week': 2, 'section': 2}, {'CourseName': '', 'week': 3, 'section': 2}, {'CourseName': '', 'week': 4, 'section'
: 2}, {'CourseName': '', 'week': 5, 'section': 2}, {'CourseName': '', 'week': 6, 'section': 2}, {'CourseName': '', 'week': 7, 'section': 2}, {'CourseName': '', 'week':
1, 'section': 3}, {'CourseName': '系統程式', 'week': 2, 'section': 3}, {'CourseName': '資料結構', 'week': 3, 'section': 3}, {'CourseName': '', 'week': 4, 'section': 3}, {
'CourseName': '', 'week': 5, 'section': 3}, {'CourseName': '', 'week': 6, 'section': 3}, {'CourseName': '', 'week': 7, 'section': 3}, {'CourseName': '', 'week': 1, 'section'
: 4}, {'CourseName': '', 'week': 2, 'section': 4}, {'CourseName': '資料結構', 'week': 3, 'section': 4}, {'CourseName': '機率與統計', 'week': 4, 'section': 4}, {'CourseName':
 '', 'week': 5, 'section': 4}, {'CourseName': '', 'week': 6, 'section': 4}, {'CourseName': '', 'week': 7, 'section': 4}, {'CourseName': '', 'week': 1, 'section': 5}, {
'CourseName': '', 'week': 2, 'section': 5}, {'CourseName': '', 'week': 3, 'section': 5}, {'CourseName': '機率與統計', 'week': 4, 'section': 5}, {'CourseName': '', 'week': 5
, 'section': 5}, {'CourseName': '', 'week': 6, 'section': 5}, {'CourseName': '', 'week': 7, 'section': 5}, {'CourseName': '', 'week': 1, 'section': 6}, {'CourseName': '',
'week': 2, 'section': 6}, {'CourseName': '', 'week': 3, 'section': 6}, {'CourseName': '', 'week': 4, 'section': 6}, {'CourseName': '', 'week': 5, 'section': 6}, {'CourseName':
 '', 'week': 6, 'section': 6}, {'CourseName': '', 'week': 7, 'section': 6}, {'CourseName': '', 'week': 1, 'section': 7}, {'CourseName': '', 'week': 2, 'section': 7}, {
'CourseName': '', 'week': 3, 'section': 7}, {'CourseName': '', 'week': 4, 'section': 7}, {'CourseName': '', 'week': 5, 'section': 7}, {'CourseName': '', 'week': 6, 'section'
: 7}, {'CourseName': '', 'week': 7, 'section': 7}, {'CourseName': '', 'week': 1, 'section': 8}, {'CourseName': '', 'week': 2, 'section': 8}, {'CourseName': '', 'week': 3
, 'section': 8}, {'CourseName': '', 'week': 4, 'section': 8}, {'CourseName': '', 'week': 5, 'section': 8}, {'CourseName': '', 'week': 6, 'section': 8}, {'CourseName': '',
'week': 7, 'section': 8}, {'CourseName': '', 'week': 1, 'section': 9}, {'CourseName': '', 'week': 2, 'section': 9}, {'CourseName': '', 'week': 3, 'section': 9}, {'CourseName'
: '', 'week': 4, 'section': 9}, {'CourseName': '', 'week': 5, 'section': 9}, {'CourseName': '', 'week': 6, 'section': 9}, {'CourseName': '', 'week': 7, 'section': 9}, {
'CourseName': '', 'week': 1, 'section': 10}, {'CourseName': '', 'week': 2, 'section': 10}, {'CourseName': '', 'week': 3, 'section': 10}, {'CourseName': '', 'week': 4, 'section':
 10}, {'CourseName': '', 'week': 5, 'section': 10}, {'CourseName': '', 'week': 6, 'section': 10}, {'CourseName': '', 'week': 7, 'section': 10}, {'CourseName': '',
'week': 1, 'section': 11}, {'CourseName': '', 'week': 2, 'section': 11}, {'CourseName': '', 'week': 3, 'section': 11}, {'CourseName': '', 'week': 4, 'section': 11}, {'CourseName'
: '', 'week': 5, 'section': 11}, {'CourseName': '', 'week': 6, 'section': 11}, {'CourseName': '', 'week': 7, 'section': 11}, {'CourseName': '', 'week': 1, 'section':
12}, {'CourseName': '', 'week': 2, 'section': 12}, {'CourseName': '', 'week': 3, 'section': 12}, {'CourseName': '', 'week': 4, 'section': 12}, {'CourseName': '', 'week': 5
, 'section': 12}, {'CourseName': '', 'week': 6, 'section': 12}, {'CourseName': '', 'week': 7, 'section': 12}, {'CourseName': '', 'week': 1, 'section': 13}, {'CourseName':
'', 'week': 2, 'section': 13}, {'CourseName': '', 'week': 3, 'section': 13}, {'CourseName': '', 'week': 4, 'section': 13}, {'CourseName': '', 'week': 5, 'section': 13}, {
'CourseName': '', 'week': 6, 'section': 13}, {'CourseName': '', 'week': 7, 'section': 13}, {'CourseName': '', 'week': 1, 'section': 14}, {'CourseName': '', 'week': 2, 'section'
: 14}, {'CourseName': '', 'week': 3, 'section': 14}, {'CourseName': '', 'week': 4, 'section': 14}, {'CourseName': '', 'week': 5, 'section': 14}, {'CourseName': '',
'week': 6, 'section': 14}, {'CourseName': '', 'week': 7, 'section': 14}], [{'CourseName': '', 'week': 1, 'section': 1}, {'CourseName': '', 'week': 2, 'section': 1}, {'CourseName':
 '', 'week': 3, 'section': 1}, {'CourseName': '', 'week': 4, 'section': 1}, {'CourseName': '', 'week': 5, 'section': 1}, {'CourseName': '', 'week': 6, 'section': 1},
{'CourseName': '', 'week': 7, 'section': 1}, {'CourseName': '', 'week': 1, 'section': 2}, {'CourseName': '', 'week': 2, 'section': 2}, {'CourseName': '', 'week': 3, 'section':
 2}, {'CourseName': '', 'week': 4, 'section': 2}, {'CourseName': '', 'week': 5, 'section': 2}, {'CourseName': '', 'week': 6, 'section': 2}, {'CourseName': '', 'week':
7, 'section': 2}, {'CourseName': '', 'week': 1, 'section': 3}, {'CourseName': '', 'week': 2, 'section': 3}, {'CourseName': '', 'week': 3, 'section': 3}, {'CourseName': '',
 'week': 4, 'section': 3}, {'CourseName': '程式設計', 'week': 5, 'section': 3}, {'CourseName': '', 'week': 6, 'section': 3}, {'CourseName': '', 'week': 7, 'section': 3}, {
'CourseName': '', 'week': 1, 'section': 4}, {'CourseName': '', 'week': 2, 'section': 4}, {'CourseName': '', 'week': 3, 'section': 4}, {'CourseName': '', 'week': 4, 'section':
 4}, {'CourseName': '程式設計', 'week': 5, 'section': 4}, {'CourseName': '', 'week': 6, 'section': 4}, {'CourseName': '', 'week': 7, 'section': 4}, {'CourseName': '',
'week': 1, 'section': 5}, {'CourseName': '', 'week': 2, 'section': 5}, {'CourseName': '', 'week': 3, 'section': 5}, {'CourseName': '', 'week': 4, 'section': 5}, {'CourseName':
 '', 'week': 5, 'section': 5}, {'CourseName': '', 'week': 6, 'section': 5}, {'CourseName': '', 'week': 7, 'section': 5}, {'CourseName': '', 'week': 1, 'section': 6}, {
'CourseName': '', 'week': 2, 'section': 6}, {'CourseName': '', 'week': 3, 'section': 6}, {'CourseName': '', 'week': 4, 'section': 6}, {'CourseName': '', 'week': 5, 'section':
 6}, {'CourseName': '', 'week': 6, 'section': 6}, {'CourseName': '', 'week': 7, 'section': 6}, {'CourseName': '', 'week': 1, 'section': 7}, {'CourseName': '邏輯設計',
'week': 2, 'section': 7}, {'CourseName': '', 'week': 3, 'section': 7}, {'CourseName': '', 'week': 4, 'section': 7}, {'CourseName': '', 'week': 5, 'section': 7}, {'CourseName':
 '', 'week': 6, 'section': 7}, {'CourseName': '', 'week': 7, 'section': 7}, {'CourseName': '', 'week': 1, 'section': 8}, {'CourseName': '邏輯設計', 'week': 2, 'section':
 8}, {'CourseName': '', 'week': 3, 'section': 8}, {'CourseName': '', 'week': 4, 'section': 8}, {'CourseName': '', 'week': 5, 'section': 8}, {'CourseName': '', 'week': 6,
'section': 8}, {'CourseName': '', 'week': 7, 'section': 8}, {'CourseName': '', 'week': 1, 'section': 9}, {'CourseName': '', 'week': 2, 'section': 9}, {'CourseName': '',
'week': 3, 'section': 9}, {'CourseName': '', 'week': 4, 'section': 9}, {'CourseName': '', 'week': 5, 'section': 9}, {'CourseName': '', 'week': 6, 'section': 9}, {'CourseName'
: '', 'week': 7, 'section': 9}, {'CourseName': '', 'week': 1, 'section': 10}, {'CourseName': '', 'week': 2, 'section': 10}, {'CourseName': '', 'week': 3, 'section': 10}, {
'CourseName': '', 'week': 4, 'section': 10}, {'CourseName': '', 'week': 5, 'section': 10}, {'CourseName': '', 'week': 6, 'section': 10}, {'CourseName': '', 'week': 7, 'section':
 10}, {'CourseName': '', 'week': 1, 'section': 11}, {'CourseName': '', 'week': 2, 'section': 11}, {'CourseName': '', 'week': 3, 'section': 11}, {'CourseName': '',
'week': 4, 'section': 11}, {'CourseName': '', 'week': 5, 'section': 11}, {'CourseName': '', 'week': 6, 'section': 11}, {'CourseName': '', 'week': 7, 'section': 11}, {'CourseName':
 '', 'week': 1, 'section': 12}, {'CourseName': '', 'week': 2, 'section': 12}, {'CourseName': '', 'week': 3, 'section': 12}, {'CourseName': '', 'week': 4, 'section':
12}, {'CourseName': '', 'week': 5, 'section': 12}, {'CourseName': '', 'week': 6, 'section': 12}, {'CourseName': '', 'week': 7, 'section': 12}, {'CourseName': '', 'week': 1
, 'section': 13}, {'CourseName': '', 'week': 2, 'section': 13}, {'CourseName': '', 'week': 3, 'section': 13}, {'CourseName': '', 'week': 4, 'section': 13}, {'CourseName':
'', 'week': 5, 'section': 13}, {'CourseName': '', 'week': 6, 'section': 13}, {'CourseName': '', 'week': 7, 'section': 13}, {'CourseName': '', 'week': 1, 'section': 14}, {
'CourseName': '', 'week': 2, 'section': 14}, {'CourseName': '', 'week': 3, 'section': 14}, {'CourseName': '', 'week': 4, 'section': 14}, {'CourseName': '', 'week': 5, 'section':
 14}, {'CourseName': '', 'week': 6, 'section': 14}, {'CourseName': '', 'week': 7, 'section': 14}], [{'CourseName': '程式設計', 'week': 1, 'section': 1}, {'CourseName'
: '', 'week': 2, 'section': 1}, {'CourseName': '', 'week': 3, 'section': 1}, {'CourseName': '', 'week': 4, 'section': 1}, {'CourseName': '', 'week': 5, 'section': 1}, {
'CourseName': '', 'week': 6, 'section': 1}, {'CourseName': '', 'week': 7, 'section': 1}, {'CourseName': '程式設計', 'week': 1, 'section': 2}, {'CourseName': '系統程式', 'week'
: 2, 'section': 2}, {'CourseName': '', 'week': 3, 'section': 2}, {'CourseName': '', 'week': 4, 'section': 2}, {'CourseName': '', 'week': 5, 'section': 2}, {'CourseName':
'', 'week': 6, 'section': 2}, {'CourseName': '', 'week': 7, 'section': 2}, {'CourseName': '', 'week': 1, 'section': 3}, {'CourseName': '系統程式', 'week': 2, 'section': 3}
, {'CourseName': '資料結構', 'week': 3, 'section': 3}, {'CourseName': '', 'week': 4, 'section': 3}, {'CourseName': '', 'week': 5, 'section': 3}, {'CourseName': '', 'week':
 6, 'section': 3}, {'CourseName': '', 'week': 7, 'section': 3}, {'CourseName': '', 'week': 1, 'section': 4}, {'CourseName': '', 'week': 2, 'section': 4}, {'CourseName':
'資料結構', 'week': 3, 'section': 4}, {'CourseName': '機率與統計', 'week': 4, 'section': 4}, {'CourseName': '', 'week': 5, 'section': 4}, {'CourseName': '', 'week': 6,
'section': 4}, {'CourseName': '', 'week': 7, 'section': 4}, {'CourseName': '', 'week': 1, 'section': 5}, {'CourseName': '', 'week': 2, 'section': 5}, {'CourseName': '', 'week'
: 3, 'section': 5}, {'CourseName': '機率與統計', 'week': 4, 'section': 5}, {'CourseName': '', 'week': 5, 'section': 5}, {'CourseName': '', 'week': 6, 'section': 5}, {
'CourseName': '', 'week': 7, 'section': 5}, {'CourseName': '', 'week': 1, 'section': 6}, {'CourseName': '', 'week': 2, 'section': 6}, {'CourseName': '', 'week': 3, 'section': 6
}, {'CourseName': '', 'week': 4, 'section': 6}, {'CourseName': '', 'week': 5, 'section': 6}, {'CourseName': '', 'week': 6, 'section': 6}, {'CourseName': '', 'week': 7,
'section': 6}, {'CourseName': '', 'week': 1, 'section': 7}, {'CourseName': '', 'week': 2, 'section': 7}, {'CourseName': '', 'week': 3, 'section': 7}, {'CourseName': '', 'week'
: 4, 'section': 7}, {'CourseName': '', 'week': 5, 'section': 7}, {'CourseName': '', 'week': 6, 'section': 7}, {'CourseName': '', 'week': 7, 'section': 7}, {'CourseName':
'', 'week': 1, 'section': 8}, {'CourseName': '', 'week': 2, 'section': 8}, {'CourseName': '', 'week': 3, 'section': 8}, {'CourseName': '', 'week': 4, 'section': 8}, {
'CourseName': '', 'week': 5, 'section': 8}, {'CourseName': '', 'week': 6, 'section': 8}, {'CourseName': '', 'week': 7, 'section': 8}, {'CourseName': '', 'week': 1, 'section': 9
}, {'CourseName': '', 'week': 2, 'section': 9}, {'CourseName': '', 'week': 3, 'section': 9}, {'CourseName': '', 'week': 4, 'section': 9}, {'CourseName': '', 'week': 5,
'section': 9}, {'CourseName': '', 'week': 6, 'section': 9}, {'CourseName': '', 'week': 7, 'section': 9}, {'CourseName': '', 'week': 1, 'section': 10}, {'CourseName': '', 'week'
: 2, 'section': 10}, {'CourseName': '', 'week': 3, 'section': 10}, {'CourseName': '', 'week': 4, 'section': 10}, {'CourseName': '', 'week': 5, 'section': 10}, {'CourseName':
 '', 'week': 6, 'section': 10}, {'CourseName': '', 'week': 7, 'section': 10}, {'CourseName': '', 'week': 1, 'section': 11}, {'CourseName': '', 'week': 2, 'section': 11
}, {'CourseName': '', 'week': 3, 'section': 11}, {'CourseName': '', 'week': 4, 'section': 11}, {'CourseName': '', 'week': 5, 'section': 11}, {'CourseName': '', 'week': 6,
'section': 11}, {'CourseName': '', 'week': 7, 'section': 11}, {'CourseName': '', 'week': 1, 'section': 12}, {'CourseName': '', 'week': 2, 'section': 12}, {'CourseName': ''
, 'week': 3, 'section': 12}, {'CourseName': '', 'week': 4, 'section': 12}, {'CourseName': '', 'week': 5, 'section': 12}, {'CourseName': '', 'week': 6, 'section': 12}, {
'CourseName': '', 'week': 7, 'section': 12}, {'CourseName': '', 'week': 1, 'section': 13}, {'CourseName': '', 'week': 2, 'section': 13}, {'CourseName': '', 'week': 3, 'section':
 13}, {'CourseName': '', 'week': 4, 'section': 13}, {'CourseName': '', 'week': 5, 'section': 13}, {'CourseName': '', 'week': 6, 'section': 13}, {'CourseName': '', 'week'
: 7, 'section': 13}, {'CourseName': '', 'week': 1, 'section': 14}, {'CourseName': '', 'week': 2, 'section': 14}, {'CourseName': '', 'week': 3, 'section': 14}, {'CourseName':
 '', 'week': 4, 'section': 14}, {'CourseName': '', 'week': 5, 'section': 14}, {'CourseName': '', 'week': 6, 'section': 14}, {'CourseName': '', 'week': 7, 'section': 14}
], [{'CourseName': '', 'week': 1, 'section': 1}, {'CourseName': '', 'week': 2, 'section': 1}, {'CourseName': '', 'week': 3, 'section': 1}, {'CourseName': '', 'week': 4,
'section': 1}, {'CourseName': '', 'week': 5, 'section': 1}, {'CourseName': '', 'week': 6, 'section': 1}, {'CourseName': '', 'week': 7, 'section': 1}, {'CourseName': '', 'week'
: 1, 'section': 2}, {'CourseName': '', 'week': 2, 'section': 2}, {'CourseName': '', 'week': 3, 'section': 2}, {'CourseName': '', 'week': 4, 'section': 2}, {'CourseName':
 '', 'week': 5, 'section': 2}, {'CourseName': '', 'week': 6, 'section': 2}, {'CourseName': '', 'week': 7, 'section': 2}, {'CourseName': '', 'week': 1, 'section': 3}, {
'CourseName': '', 'week': 2, 'section': 3}, {'CourseName': '', 'week': 3, 'section': 3}, {'CourseName': '', 'week': 4, 'section': 3}, {'CourseName': '', 'week': 5, 'section':
3}, {'CourseName': '', 'week': 6, 'section': 3}, {'CourseName': '', 'week': 7, 'section': 3}, {'CourseName': '', 'week': 1, 'section': 4}, {'CourseName': '', 'week': 2,
'section': 4}, {'CourseName': '', 'week': 3, 'section': 4}, {'CourseName': '', 'week': 4, 'section': 4}, {'CourseName': '', 'week': 5, 'section': 4}, {'CourseName': '', 'week'
: 6, 'section': 4}, {'CourseName': '', 'week': 7, 'section': 4}, {'CourseName': '', 'week': 1, 'section': 5}, {'CourseName': '', 'week': 2, 'section': 5}, {'CourseName':
 '', 'week': 3, 'section': 5}, {'CourseName': '', 'week': 4, 'section': 5}, {'CourseName': '', 'week': 5, 'section': 5}, {'CourseName': '', 'week': 6, 'section': 5}, {
'CourseName': '', 'week': 7, 'section': 5}, {'CourseName': '', 'week': 1, 'section': 6}, {'CourseName': '', 'week': 2, 'section': 6}, {'CourseName': '', 'week': 3, 'section':
6}, {'CourseName': '', 'week': 4, 'section': 6}, {'CourseName': '', 'week': 5, 'section': 6}, {'CourseName': '', 'week': 6, 'section': 6}, {'CourseName': '', 'week': 7,
'section': 6}, {'CourseName': '系統分析與設計', 'week': 1, 'section': 7}, {'CourseName': '邏輯設計', 'week': 2, 'section': 7}, {'CourseName': '', 'week': 3, 'section': 7}, {
'CourseName': '', 'week': 4, 'section': 7}, {'CourseName': '', 'week': 5, 'section': 7}, {'CourseName': '', 'week': 6, 'section': 7}, {'CourseName': '', 'week': 7, 'section'
: 7}, {'CourseName': '系統分析與設計', 'week': 1, 'section': 8}, {'CourseName': '邏輯設計', 'week': 2, 'section': 8}, {'CourseName': '', 'week': 3, 'section': 8}, {
'CourseName': '', 'week': 4, 'section': 8}, {'CourseName': '', 'week': 5, 'section': 8}, {'CourseName': '', 'week': 6, 'section': 8}, {'CourseName': '', 'week': 7, 'section': 8
}, {'CourseName': '', 'week': 1, 'section': 9}, {'CourseName': '', 'week': 2, 'section': 9}, {'CourseName': '', 'week': 3, 'section': 9}, {'CourseName': '', 'week': 4,
'section': 9}, {'CourseName': '', 'week': 5, 'section': 9}, {'CourseName': '', 'week': 6, 'section': 9}, {'CourseName': '', 'week': 7, 'section': 9}, {'CourseName': '', 'week'
: 1, 'section': 10}, {'CourseName': '', 'week': 2, 'section': 10}, {'CourseName': '', 'week': 3, 'section': 10}, {'CourseName': '', 'week': 4, 'section': 10}, {'CourseName'
: '', 'week': 5, 'section': 10}, {'CourseName': '', 'week': 6, 'section': 10}, {'CourseName': '', 'week': 7, 'section': 10}, {'CourseName': '', 'week': 1, 'section': 11}
, {'CourseName': '', 'week': 2, 'section': 11}, {'CourseName': '', 'week': 3, 'section': 11}, {'CourseName': '', 'week': 4, 'section': 11}, {'CourseName': '', 'week': 5,
'section': 11}, {'CourseName': '', 'week': 6, 'section': 11}, {'CourseName': '', 'week': 7, 'section': 11}, {'CourseName': '', 'week': 1, 'section': 12}, {'CourseName': '',
 'week': 2, 'section': 12}, {'CourseName': '', 'week': 3, 'section': 12}, {'CourseName': '', 'week': 4, 'section': 12}, {'CourseName': '', 'week': 5, 'section': 12}, {
'CourseName': '', 'week': 6, 'section': 12}, {'CourseName': '', 'week': 7, 'section': 12}, {'CourseName': '', 'week': 1, 'section': 13}, {'CourseName': '', 'week': 2, 'section'
: 13}, {'CourseName': '', 'week': 3, 'section': 13}, {'CourseName': '', 'week': 4, 'section': 13}, {'CourseName': '', 'week': 5, 'section': 13}, {'CourseName': '', 'week'
: 6, 'section': 13}, {'CourseName': '', 'week': 7, 'section': 13}, {'CourseName': '', 'week': 1, 'section': 14}, {'CourseName': '', 'week': 2, 'section': 14}, {'CourseName'
: '', 'week': 3, 'section': 14}, {'CourseName': '', 'week': 4, 'section': 14}, {'CourseName': '', 'week': 5, 'section': 14}, {'CourseName': '', 'week': 6, 'section': 14},
 {'CourseName': '', 'week': 7, 'section': 14}]]


##nid為所有輪流上課的人
##courses放了所有人的課表 courses[0]是nid[0]的課表
print(courses[0][0])##某一堂課的內容  印出看資料發現為星期一第一節的程式設計課
print(courses[0][0]['CourseName'])##程式設計