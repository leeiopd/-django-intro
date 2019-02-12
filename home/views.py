from django.shortcuts import render, HttpResponse
import datetime
import random

# Create your views here.
def index(request):
    print(request)
    print(type(request))
    print(request.META)
    return render(request, 'home/index.html')
    
def dinner(request):
    box = ['치킨', '치킨', '편도', '수국']
    dinner = random.choice(box)
    # render 필수인자
    # 1) request, 2) template 파일(html)
    # render 선택인자
    # 3) dictionary : 템플릿에서 쓸 변수 인자 값을 정의, 값을 html로 넘기려면 dictionary형태로 넘겨야함.
    return render(request, 'home/dinner.html', {'dinner':dinner, 'box':box})
    # template은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
    # Django Template Language
    
def you(request, name):
    return render(request, 'home/you.html', {'name':name})


# 넘겨받을때 <int:num>으로 넘겨받으면 int형으로 받을 수 있다. 기본적으로는 str형으로 넘어온다.    
def cube(request, num):
    cube_num = int(num)**3
    return render(request, 'home/cube.html', {'num':num, 'cube_num':cube_num})
    
def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    ping = request.GET.get('ping')
    return render(request, 'home/pong.html', {'ping':ping})
    
def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_read(request):
    user_name = request.POST.get('user_name')
    user_password = request.POST.get('password')
    return render(request, 'home/user_read.html', {'user_name':user_name, "user_password":user_password})
    
def template_example(request):
    my_info = {'name':'이주호', 'age':'30', 'nickname':'ho'}
    my_list = ['짜장면', '짬뽕', '탕수육', '양장피']
    my_sentence = 'Life is short, you need python!'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.datetime.now()
    empty_list = []
    
    return render(request, 'home/template_example.html', {'my_info':my_info, 'my_list':my_list, 'my_sentence':my_sentence, 'messages':messages, 'datetimenow':datetimenow, 'empty_list':empty_list})
    
def static_example(request):
    return render(request, 'home/static_example.html')