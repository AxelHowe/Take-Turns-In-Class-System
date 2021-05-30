from django import forms
from group.models import NID, Course

class NIDForm(forms.ModelForm):
    NIDuser = forms.CharField(label='NID', max_length=128)
    NIDpassword = forms.CharField(label='密碼', widget=forms.PasswordInput)
    #User = forms.CharField(label='123', widget=forms.PasswordInput)
    class Meta:
        model = NID
        fields = ['NIDuser', 'NIDpassword', ]

class CourseForm(forms.ModelForm):
    #NID = models.ForeignKey(NID, on_delete=models.CASCADE)
    #CourseTable = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
    #teacher = models.CharField(max_length=128)
    week_choice = [(1, '週一'), (2, '週二'), (3, '週三'), (4, '週四'), (5, '週五'), (6, '週六'), (7, '週日'), ]
    section_choice = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                      (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14),]
    CourseName = forms.CharField(label='課程名稱', max_length=128)
    #CourseCode = forms.IntegerField(label='選課代號', widget=forms.NumberInput)
    week = forms.IntegerField(label='週次', widget=forms.Select(choices=week_choice))
    section = forms.IntegerField(label='節次', widget=forms.Select(choices=section_choice))

    #user_type = forms.IntegerField(initial=2,
    #                               widget=forms.widgets.Select(choices=user_type_choice, ))
    class Meta:
        model = Course
        fields = ['CourseName', 'week', 'section']