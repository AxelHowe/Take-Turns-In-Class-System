from populate import base
from group.models import NID, Course#, CourseTable
from user.models import User
nid = ['D0886096', 'D0886108', 'D0886172', 'D0886112']
course = ['程式設計', '系統程式', '資料結構', '機率與統計','資料庫系統']
def populate():
    print('Populating User ... ', end='')
    User.objects.exclude(is_superuser=True).delete()
    user = User.objects.create_user(username='123', password='123')

    print('done')

    print('Populating NID and Course ... ', end='')
    NID.objects.all().delete()
    Course.objects.all().delete()
    #CourseTable.objects.all().delete()

    #coursetable = CourseTable()
    #coursetable.User=user
    #coursetable.save()
   # CourseTable.objects.create(User=user)


    index = 0
    for i in nid:
        n = NID()
        n.NIDuser = i
        n.NIDpassword = i
        #n.CourseTable = coursetable
        n.User = user
        n.save()
        if index==0 or index ==3:
            for j in range(4):
                Course.objects.create(NID=n, CourseName=course[j], week=j+1, section=j+1)
                Course.objects.create(NID=n, CourseName=course[j], week=j + 1, section=j + 2)
        elif index==1:
            Course.objects.create(NID=n, CourseName=course[0], week=5, section=3)
            Course.objects.create(NID=n, CourseName=course[0], week=5, section=4)
            Course.objects.create(NID=n, CourseName='邏輯設計', week=2, section=7)
            Course.objects.create(NID=n, CourseName='邏輯設計', week=2, section=8)
        else:
            Course.objects.create(NID=n, CourseName='邏輯設計', week=2, section=7)
            Course.objects.create(NID=n, CourseName='邏輯設計', week=2, section=8)
            Course.objects.create(NID=n, CourseName='系統分析與設計', week=1, section=7)
            Course.objects.create(NID=n, CourseName='系統分析與設計', week=1, section=8)
        index +=1
        #for comment in comments:
            #Comment.objects.create(article=article, content=comment)

    print('done')


if __name__ == '__main__':
    populate()