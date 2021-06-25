from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import UserForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    '''
        Register a new user
        '''
    template = 'user/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm': UserForm()})

    # POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        messages.error(request, '請填資料')
        return render(request, template, {'userForm': userForm})

    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']

        if password == password_check:
            if User.objects.filter(username=username).exists():
                messages.info(request, "帳戶已存在！")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('User Created!')
                return redirect('login')
        else:
            messages.info(request, "密碼不相符！")
        return redirect('register')
    else:
        return render(request, 'accounts/accounts_base.html', {'login_page':False})
        '''

def login(request):
    '''
        Login an existing user
        '''
    template = 'user/login.html'
    if request.method == 'GET':
        return render(request, template)

    # POST
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    if not username or not password:  # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)

    user = authenticate(username=username, password=password)
    if not user:  # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)

    # login success
    auth_login(request, user)
    messages.success(request, '登入成功')
    return redirect('main:main')
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "帳號或密碼有誤！")
            return redirect('login')
    else:
        return render(request, 'user/login.html')
        
    '''
@login_required
def logout(request):
    '''
    Logout the user
    '''
    auth_logout(request)
    messages.success(request, '登出成功')
    return redirect('main:main')

