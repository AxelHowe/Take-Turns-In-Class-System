from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def main(request):
    #context = {'like':'Django is good'}
    return render(request, 'main/main.html')

'''
HttpResponse() 回覆字串或物件
render()  回覆網頁
redirect()   轉址
get_object_or_404() 找不到就回傳404
'''


def about(request):
    return render(request, 'main/about.html')

#def login(request):
 #   return render(request, 'main/login.html')