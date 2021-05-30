from django.contrib import admin
from group.models import NID, Course#, CourseTable
# Register your models here.

admin.site.register(NID)
#admin.site.register(CourseTable)
admin.site.register(Course)