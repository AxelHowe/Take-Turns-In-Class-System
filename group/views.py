from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from group.forms import NIDForm, CourseForm
from group.models import NID,Course#,CourseTable
from user.models import User
from django.contrib.auth.decorators import login_required
from group.scrapers import scrapers
import os
# Create your views here.
@login_required
def group(request, UserID):
    #NIDs = NID.objects.all()
    NIDs = NID.objects.filter(User=UserID)

    nids = []
    courses = []
    course1 = []
    course2 = []
    course3 = []
    course4 = []
    course5 = []
    course6 = []
    course7 = []
    course8 = []
    course9 = []
    course10 = []
    course11 = []
    course12 = []
    course13 = []
    course14 = []
    if len(NIDs) == 0: ##剛開始還沒有新增NID
        just_a_trash = {'CourseName':'',}
        for i in range(7):
            course1.append(just_a_trash)
            course2.append(just_a_trash)
            course3.append(just_a_trash)
            course4.append(just_a_trash)
            course5.append(just_a_trash)
            course6.append(just_a_trash)
            course7.append(just_a_trash)
            course8.append(just_a_trash)
            course9.append(just_a_trash)
            course10.append(just_a_trash)
            course11.append(just_a_trash)
            course12.append(just_a_trash)
            course13.append(just_a_trash)
            course14.append(just_a_trash)
        content = {'NIDs': NIDs,  'course1': course1, 'course2': course2,
                   'course3': course3, 'course4': course4, 'course5': course5, 'course6': course6,
                   'course7': course7, 'course8': course8, 'course9': course9, 'course10': course10,
                   'course11': course11, 'course12': course12, 'course13': course13, 'course14': course14}
        return render(request, 'group/group.html', content)

    for i,v in enumerate(NIDs):
        nids.append(v)
        course = Course.objects.filter(NID=v)
        temp=[]
        for j,value in enumerate(course):
            tmp = {'CourseName':value.CourseName, 'week':value.week, 'section':value.section}
            temp.append(tmp)
        courses.append(temp)
        ##################胖胖寫的演算法
    teemCourse = []
    temp = courses[0]
    for i, v in enumerate(temp):
        v.setdefault('times', 0)

    for i, v in enumerate(courses):
        if (i == 0):
            continue
        for j, value1 in enumerate(temp):
            k = 0
            for k, value2 in enumerate(v):
                if (value1['CourseName'] == value2['CourseName'] and value1['week'] == value2['week'] and value1[
                    'section'] == value2['section']):
                    value1['times'] += 1

    for i, v in enumerate(temp):
        if (v['times'] == (len(nids) - 1)):
            teemCourse.append(v)
        else:
            teemCourse.append({'CourseName': '', 'week': v['week'], 'section': v['section'], 'times': 3})
    #for i, v in enumerate(teemCourse):
        #print(v)
            ###############
   # print(nids)
   # print(courses)
        #print(str(course[1].week)+ ' ' + str(course[1].section))

    for i in range(7):
        course1.append(teemCourse[i])
        course2.append(teemCourse[i + 7])
        course3.append(teemCourse[i + 14])
        course4.append(teemCourse[i + 21])
        course5.append(teemCourse[i + 28])
        course6.append(teemCourse[i + 35])
        course7.append(teemCourse[i + 42])
        course8.append(teemCourse[i + 49])
        course9.append(teemCourse[i + 56])
        course10.append(teemCourse[i + 63])
        course11.append(teemCourse[i + 70])
        course12.append(teemCourse[i + 77])
        course13.append(teemCourse[i + 84])
        course14.append(teemCourse[i + 91])
    print(course14)
    content = {'NIDs':NIDs, 'course':teemCourse, 'course1':course1, 'course2':course2,
               'course3':course3, 'course4':course4, 'course5':course5, 'course6':course6,
               'course7':course7, 'course8':course8, 'course9':course9, 'course10':course10,
               'course11':course11, 'course12':course12, 'course13':course13, 'course14':course14}
    return render(request, 'group/group.html', content)

@login_required
def addNID(request, UserID):
    template = 'group/addNID.html'

    if request.method == 'GET':
        return render(request, template, {'NIDform': NIDForm()})
    # POST
    NIDform = NIDForm(request.POST)
    if not NIDform.is_valid():
        # TODO: 爬蟲
        return render(request, template, {'NIDform': NIDform})



    scrapers.pdf(NIDform['NIDuser'].value(),NIDform['NIDpassword'].value())

    courseList = scrapers.readCourse()
    print(courseList)
    nid = NID.objects.create(User=User.objects.get(id=UserID), NIDuser=NIDform['NIDuser'].value(),
                             NIDpassword=NIDform['NIDpassword'].value())
    print(nid)
    for i in range(1,15):
        for j in range(1,8):
            newCourse = Course()
            newCourse.NID = nid
            newCourse.week = j
            newCourse.section = i
            newCourse.save()
    for i in courseList:
        newCourse = Course.objects.get_or_create(NID=nid, week=i['week'], section=i['section'])
        #newCourse.NID = nid
        newCourse=newCourse[0]
        newCourse.CourseName = i['CourseName']
        #newCourse.week = i['week']
        #newCourse.section = i['section']
        newCourse.save()

    #NIDform.save()
    messages.success(request, 'NID已新增')
    os.remove('課表.pdf')
    return redirect('group:group', UserID=UserID)

@login_required
def deleteNID(request, UserID, NIDid):
    if request.method == 'GET':
        return redirect('group:group', UserID=UserID)
    #POST
    nid = get_object_or_404(NID, id=NIDid)
    nid.delete()
    messages.success(request, 'NID已刪除')
    return redirect('group:group', UserID=UserID)
@login_required
def viewCourse(request, UserID, NIDid,):
    nid = get_object_or_404(NID, id=NIDid)
    NIDs = NID.objects.filter(User=UserID)
    #courseTable = CourseTable.objects.filter(NID=nid)

    course = Course.objects.filter(NID=nid)
    courses = []
    temp = []
    for j, value in enumerate(course):
        #tmp = {'CourseName': value.CourseName, 'week': value.week, 'section': value.section}
        courses.append(value)
    #print(courses)
    #courses.append(temp)
    #print(courses[1])
    course1 = []
    course2 = []
    course3 = []
    course4 = []
    course5 = []
    course6 = []
    course7 = []
    course8 = []
    course9 = []
    course10 = []
    course11 = []
    course12 = []
    course13 = []
    course14 = []
    for i in range(7):
        course1.append(courses[i])
        course2.append(courses[i + 7])
        course3.append(courses[i + 14])
        course4.append(courses[i + 21])
        course5.append(courses[i + 28])
        course6.append(courses[i + 35])
        course7.append(courses[i + 42])
        course8.append(courses[i + 49])
        course9.append(courses[i + 56])
        course10.append(courses[i + 63])
        course11.append(courses[i + 70])
        course12.append(courses[i + 77])
        course13.append(courses[i + 84])
        course14.append(courses[i + 91])
    #print(course14)


    #coursetable = {1: course1, 2: course2, 3: course3, 4: course4, 5: course5, 6: course6, 7: course7, 8: course8,
    #               9: course9, 10: course10, 11: course11, 12: course12, 13: course13, 14: course14             }

    '''
    for i in range(1,8):
        for j in range(1,15):
            Course.objects.get_or_create(week=i, section=j, NID=nid)
            coursetable[j][i] = Course.objects.get(week=i, section=j, NID=nid)

    '''
    content = {'nid': nid, 'NIDs': NIDs, 'course1':course1, 'course2':course2,
               'course3':course3, 'course4':course4, 'course5':course5, 'course6':course6,
               'course7':course7, 'course8':course8, 'course9':course9, 'course10':course10,
               'course11':course11, 'course12':course12, 'course13':course13, 'course14':course14}
    return render(request, 'group/viewCourse.html', content)
@login_required
def updateCourse(request, UserID, NIDid, CourseID):
    nid = get_object_or_404(NID, id=NIDid)
    course = get_object_or_404(Course, id=CourseID)
    template = 'group/addCourse.html'

    if request.method == 'GET':
        Courseform = CourseForm(instance=course)
        #Courseform = CourseForm()
        return render(request, template, {'Courseform': Courseform, 'nid': nid})
    # POST
    Courseform = CourseForm(request.POST, instance=course)
    if not Courseform.is_valid():
        # TODO: 爬蟲
        return render(request, template, {'Courseform': Courseform, 'nid': nid})
    #course.delete()
    print(Courseform['week'].value())
    print(Courseform['section'].value())
    print(Courseform['CourseName'].value())
    course = Course.objects.get_or_create(week= Courseform['week'].value(), section=Courseform['section'].value(), NID=nid)
    #print(course[0])
   # print(course[0].CourseName)
    course[0].CourseName= Courseform['CourseName'].value()
    course[0].save()

    messages.success(request, '編輯成功')
    return redirect('group:viewCourse', UserID=UserID, NIDid=NIDid)
@login_required
def deleteCourse(request, UserID, NIDid, CourseID):
    if request.method == 'GET':
        return redirect('group:group', UserID=UserID)
    # POST
    nid = get_object_or_404(NID, id=NIDid)
    course = get_object_or_404(Course, id=CourseID, NID=nid)

    print('刪除的課是  ' + course.CourseName)
    print('刪除的課是  ' + str(CourseID))
    course.CourseName = ''
    course.save()
    #course.delete()
    #刪除要改
    messages.success(request, '刪除成功')
    return redirect('group:viewCourse', UserID=UserID, NIDid=NIDid)