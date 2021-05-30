from django.urls import path
from group import views

app_name = 'group'
urlpatterns = [
    path('<int:UserID>', views.group, name='group'),
    path('<int:UserID>/addNID/', views.addNID, name='addNID'),
    path('<int:UserID>/deleteNID/<int:NIDid>/', views.deleteNID, name='deleteNID'),
    path('<int:UserID>/viewCourse/<int:NIDid>/', views.viewCourse, name='viewCourse'),
    path('<int:UserID>/updateCourse/<int:NIDid>/<int:CourseID>/', views.updateCourse, name='updateCourse'),
    path('<int:UserID>/deleteCourse/<int:NIDid>/<int:CourseID>/', views.deleteCourse, name='deleteCourse'),
]