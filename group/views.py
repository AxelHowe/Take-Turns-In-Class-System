from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from group.forms import NIDForm, CourseForm
from group.models import NID,Course#,CourseTable
from user.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def group(request, UserID):
    #NIDs = NID.objects.all()
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
    print(nids)
    print(courses)
        #print(str(course[1].week)+ ' ' + str(course[1].section))
    content = {'NIDs':NIDs}
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
    print('看這裡啦幹')
    print(NIDform['NIDuser'].value())
    #nid = NID()
    NID.objects.create(User=User.objects.get(id=UserID),NIDuser=NIDform['NIDuser'].value(), NIDpassword=NIDform['NIDpassword'].value())
    #NIDform.save()
    messages.success(request, 'NID已新增')
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


    #c1 = {}

    #print(c1)
    course1 = {}
    course2 = {}
    course3 = {}
    course4 = {}
    course5 = {}
    course6 = {}
    course7 = {}
    course8 = {}
    course9 = {}
    course10 = {}
    course11 = {}
    course12 = {}
    course13 = {}
    course14 = {}
    #course1 = {1: Course(week=1,section=1,NID=nid), 2: Course(week=2,section=1, NID=nid), 3: Course(week=3,section=1, NID=nid), 4: Course(week=4,section=1, NID=nid), 5: Course(week=5,section=1, NID=nid), 6: Course(week=6,section=1, NID=nid), 7: Course(week=7,section=1, NID=nid)}
    # course2 = {1: Course(week=1,section=2, NID=nid), 2: Course(week=2,section=2, NID=nid), 3: Course(week=3,section=2, NID=nid), 4: Course(week=4,section=2, NID=nid), 5: Course(week=5,section=2, NID=nid), 6: Course(week=6,section=2, NID=nid), 7: Course(week=7,section=2, NID=nid)}
    # course3 = {1: Course(week=1,section=3, NID=nid), 2: Course(week=2,section=3, NID=nid), 3: Course(week=3,section=3, NID=nid), 4: Course(week=4,section=3, NID=nid), 5: Course(week=5,section=3, NID=nid), 6: Course(week=6,section=3, NID=nid), 7: Course(week=7,section=3, NID=nid)}
    # course4 = {1: Course(week=1,section=4, NID=nid), 2: Course(week=2,section=4, NID=nid), 3: Course(week=3,section=4, NID=nid), 4: Course(week=4,section=4, NID=nid), 5: Course(week=5,section=4, NID=nid), 6: Course(week=6,section=4, NID=nid), 7: Course(week=7,section=4, NID=nid)}
    # course5 = {1: Course(week=1, section=5, NID=nid), 2: Course(week=2, section=5, NID=nid), 3: Course(week=3, section=5, NID=nid),
    #            4: Course(week=4, section=5, NID=nid), 5: Course(week=5, section=5, NID=nid), 6: Course(week=6, section=5, NID=nid),
    #            7: Course(week=7, section=5, NID=nid)}
    # course6 = {1: Course(week=1, section=6, NID=nid), 2: Course(week=2, section=6, NID=nid), 3: Course(week=3, section=6, NID=nid),
    #            4: Course(week=4, section=6, NID=nid), 5: Course(week=5, section=6, NID=nid), 6: Course(week=6, section=6, NID=nid),
    #            7: Course(week=7, section=6, NID=nid)}
    # course7 = {1: Course(week=1, section=7, NID=nid), 2: Course(week=2, section=7, NID=nid), 3: Course(week=3, section=7, NID=nid),
    #            4: Course(week=4, section=7, NID=nid), 5: Course(week=5, section=7, NID=nid), 6: Course(week=6, section=7, NID=nid),
    #            7: Course(week=7, section=7, NID=nid)}
    # course8 = {1: Course(week=1, section=8, NID=nid), 2: Course(week=2, section=8, NID=nid), 3: Course(week=3, section=8, NID=nid),
    #            4: Course(week=4, section=8, NID=nid), 5: Course(week=5, section=8, NID=nid), 6: Course(week=6, section=8, NID=nid),
    #            7: Course(week=7, section=8, NID=nid)}
    # course9 = {1: Course(week=1, section=9, NID=nid), 2: Course(week=2, section=9, NID=nid), 3: Course(week=3, section=9, NID=nid),
    #            4: Course(week=4, section=9, NID=nid), 5: Course(week=5, section=9, NID=nid), 6: Course(week=6, section=9, NID=nid),
    #            7: Course(week=7, section=9, NID=nid)}
    # course10 = {1: Course(week=1, section=10, NID=nid), 2: Course(week=2, section=10, NID=nid), 3: Course(week=3, section=10, NID=nid),
    #            4: Course(week=4, section=10, NID=nid), 5: Course(week=5, section=10, NID=nid), 6: Course(week=6, section=10, NID=nid),
    #            7: Course(week=7, section=10, NID=nid)}
    # course11 = {1: Course(week=1, section=11, NID=nid), 2: Course(week=2, section=11, NID=nid), 3: Course(week=3, section=11, NID=nid),
    #            4: Course(week=4, section=11, NID=nid), 5: Course(week=5, section=11, NID=nid), 6: Course(week=6, section=11, NID=nid),
    #            7: Course(week=7, section=11, NID=nid)}
    # course12 = {1: Course(week=1, section=12, NID=nid), 2: Course(week=2, section=12, NID=nid), 3: Course(week=3, section=12, NID=nid),
    #            4: Course(week=4, section=12, NID=nid), 5: Course(week=5, section=12, NID=nid), 6: Course(week=6, section=12, NID=nid),
    #            7: Course(week=7, section=12, NID=nid)}
    # course13 = {1: Course(week=1, section=13, NID=nid), 2: Course(week=2, section=13, NID=nid), 3: Course(week=3, section=13, NID=nid),
    #            4: Course(week=4, section=13, NID=nid), 5: Course(week=5, section=13, NID=nid), 6: Course(week=6, section=13, NID=nid),
    #            7: Course(week=7, section=13, NID=nid)}
    # course14 = {1: Course(week=1, section=14, NID=nid), 2: Course(week=2, section=14, NID=nid), 3: Course(week=3, section=14, NID=nid),
    #            4: Course(week=4, section=14, NID=nid), 5: Course(week=5, section=14, NID=nid), 6: Course(week=6, section=14, NID=nid),
    #            7: Course(week=7, section=14, NID=nid)}
#=============================================
    #course1 = [1:Course(week=1,section=1), 2:Course(week=2,section=1), 3:Course(week=3,section=1), Course(week=4,section=1), Course(week=5,section=1), Course(week=6,section=1), Course(week=7,section=1)]
    #course2 = [Course(week=1,section=2), Course(week=2,section=1), Course(week=3,section=1), Course(week=4,section=1), Course(week=5,section=1), Course(week=6,section=1), Course(week=7,section=1)]
    #course3 = [Course(week=1,section=3), Course(week=2,section=1), Course(week=3,section=1), Course(week=4,section=1), Course(week=5,section=1), Course(week=6,section=1), Course(week=7,section=1)]
    #course4 = [Course(week=1,section=4), Course(week=2,section=1), Course(week=3,section=1), Course(week=4,section=1), Course(week=5,section=1), Course(week=6,section=1), Course(week=7,section=1)]
    coursetable = {}
    coursetable = {1: course1, 2: course2, 3: course3, 4: course4, 5: course5, 6: course6, 7: course7, 8: course8,
                   9: course9, 10: course10, 11: course11, 12: course12, 13: course13, 14: course14             }
    #coursetable = [course1,  course2,  course3,  course4]

    for i in range(1,8):
        for j in range(1,15):
            Course.objects.get_or_create(week=i, section=j, NID=nid)
            coursetable[j][i] = Course.objects.get(week=i, section=j, NID=nid)
    # course = Course.objects.filter(NID=nid)
    # for i in course:
    #     coursetable[i.section][i.week] = i

    content = {'nid': nid, 'NIDs': NIDs, 'course': coursetable}
    return render(request, 'group/viewCourse.html', content)
@login_required
def updateCourse(request, UserID, NIDid, CourseID):
    nid = get_object_or_404(NID, id=NIDid)
    course = get_object_or_404(Course, id=CourseID)
    template = 'group/addCourse.html'

    if request.method == 'GET':
        Courseform = CourseForm(instance=course)
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
    course = get_object_or_404(Course, id=CourseID)
    #course.CourseName = ''
    #course.save()
    course.delete()
    #刪除要改
    messages.success(request, '刪除成功')
    return redirect('group:viewCourse', UserID=UserID, NIDid=NIDid)