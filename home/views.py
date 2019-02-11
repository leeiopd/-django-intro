from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    print(request)
    print(type(request))
    print(request.META)
    return render(request, 'index.html')
    
def dinner(request):
    box = ['치킨', '치킨', '편도', '수국']
    dinner = random.choice(box)
    # render 필수인자
    # 1) request, 2) template 파일(html)
    # render 선택인자
    # 3) dictionary : 템플릿에서 쓸 변수 인자 값을 정의, 값을 html로 넘기려면 dictionary형태로 넘겨야함.
    return render(request, 'dinner.html', {'dinner':dinner, 'box':box})
    # template은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
    # Django Template Language