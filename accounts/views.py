from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .form import RegisterForm,LoginForm
# Create your views here.

@login_required(login_url="Login")
def index(request):
    return render(request,'accounts/index.html')

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Index')
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # 重定向到首页或其他页面
        else:
            error = '用户名或密码错误，请重试。'  # 错误提示信息
    else:
        error = None
    context = {
        'form': form,
        'error': error  # 将错误提示信息传递给模板
    }
    return render(request, 'accounts/login.html', context)



def log_out(request):
    logout(request)
    return redirect('/login') #重新導向到登入畫面