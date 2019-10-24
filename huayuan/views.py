from django.shortcuts import render,redirect
from huayuan import models
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
import pymysql
import json
# Create your views here.

#主页
def index(request):
    conn = pymysql.connect(host="localhost", user="root", password="12345678", database="znhy", port=3306)
    cur = conn.cursor()
    sql = 'SELECT  Humidity,Temperature FROM test'
    cur.execute(sql)
    datas = cur.fetchall()
    jsonData = {}
    id = []
    Temperature = []
    for data in datas:
        id.append(data[0])
        Temperature.append(data[1])


    dict={
        'id':json.dumps(id),
        'Temperature':json.dumps(Temperature)
    }

    sql = 'SELECT  Humidity,avg FROM test'
    cur.execute(sql)
    datas = cur.fetchall()
    jsonData = {}
    id = []
    soil_Avg = []
    for data in datas:
        id.append(data[0])
        soil_Avg.append(data[1])

    dict = {
        'ids': json.dumps(id),
        'Illumination': json.dumps(soil_Avg)
    }
    sql = 'SELECT  Humidity,Illumination FROM test'
    cur.execute(sql)
    datas = cur.fetchall()
    jsonData = {}
    id = []
    Illumination = []
    for data in datas:
        id.append(data[0])
        Illumination.append(data[1])

    dict = {
        'ids': json.dumps(id),
        'Illumination': json.dumps(Illumination)
    }
    user=request.session['username']
    return render(request, 'index.html',{"id":id,"Temperature":Temperature,'ids':id,'soil_Avg':soil_Avg,'ids':id,'Illumination':Illumination,'user':user})

#注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('email')
        password = request.POST.get('password')
        reviewpassword = request.POST.get('reviewpassword')
        message="所有信息必须填写"
        if models.userRegister.objects.get(username=username):
            message="此用户已注册"
        elif models.userRegister.objects.get(username=username):



#登录
def login(request):

    if request.session.get('is_login',None):
        return  redirect('/index/')
    if request.method == 'POST':
        yonghuname = request.POST.get('yonghu')
        password = request.POST.get('password')
        user=auth.authenticate(request,yonghu=yonghuname,password=password)
        message="所有信息都必须填写!"
        if yonghuname and password is not None:
            yonghuname=yonghuname.strip()
            try:
                user=models.userRegister.objects.get(useremail=yonghuname)
                if user.password == password:
                    request.session['useremail'] = user.useremail
                    request.session['username'] = user.username
                    return redirect('/index/')
                else:
                    message = '登录密码错误'
            except:
                message='用户不存在'


            return  render(request,'login.html',{'message':message})
    return render(request, 'login.html')


def aleats(request):
    user = request.session['username']
    return render(request, 'alerts.html',{'user':user})


def blank(request):
    user = request.session['username']
    if request.method =='POST':
        username=request.POST.get("username")
        if user==username:
            username=user
        else:
            username=username
        usersex=request.POST.get("usersex")
        userNation=request.POST.get("userNation")
        userbirthday=request.POST.get("userbirthday")
        userage = request.POST.get("userage")
        user_cai_type=request.POST.get("user_cai_type")
        userIdCard=request.POST.get("userIdCard")
        userFaith =request.POST.get("userFaith")
        userRemark=request.POST.get("userRemark")
        userphone =request.POST.get("userphone")
        userAddress=request.POST.get("userAddress")
        userImage =request.POST.get(" userImage")
        models.personal_information.objects.create(username=username,usersex=usersex,userage=userage,userAddress=userAddress,userbirthday=userbirthday,user_cai_type=user_cai_type,userNation=userNation, userIdCard=userIdCard,userFaith =userFaith,userRemark=userRemark,userphone =userphone,userImage =userImage)
    # messege="修改成功"
    return render(request, 'blank.html',{'user':user})


def buttons(request):
    user = request.session['username']
    return render(request, 'buttons.html',{'user':user})


def cards(request):
    user = request.session['username']
    return render(request, 'cards.html',{'user':user})


def chartjs(request):
    user = request.session['username']
    return render(request, 'chartjs.html',{'user':user})


def invoice(request):
    user = request.session['username']
    return render(request, 'invoice.html',{'user':user})


def modal(request):
    user = request.session['username']
    return render(request, 'modals.html',{'user':user})


def pepei(request):
    user = request.session['username']
    return render(request, 'pepei.html',{'user':user})

def progress_bars(request):
    user = request.session['username']
    return render(request, 'progress_bars.html',{'user':user})

def ren(request):
    user = request.session['username']
    return render(request, 'ren.html',{'user':user})

def rizhi(request):
    user = request.session['username']
    return render(request, 'rizhi.html',{'user':user})

def settings(request):
    user = request.session['username']
    return render(request, 'settings.html',{'user':user})

def tabs(request):
    user = request.session['username']
    return render(request, 'tabs.html',{'user':user})

def user(request):
    user = request.session['username']
    return render(request, 'user.html',{'user':user})

def zhi(request):
    user = request.session['username']
    return render(request, 'zhi.html',{'user':user})

def zhiwuzhonglei(request):
    user = request.session['username']
    return render(request, 'zhiwuzhonglei.html',{'user':user})
def jsdaoru(request):
    pass
def alerts(request):
    user = request.session['username']
    return render(request, 'alerts.html', {'user': user})
    # conn=pymysql.connect(host="localhost", user="root", password="12345678", database="znhy", port=3306)
    # cur = conn.cursor()
    # sql = 'SELECT  Humidity,Temperature FROM test'
    # cur.execute(sql)
    # datas = cur.fetchall()
    # jsonData={}
    # id = []
    # Temperature = []
    # for data in datas:
    #     id.append(data[0])
    #     Temperature.append(data[1])
    # return render(request,'login.html',{'id':id,'Temperature':Temperature})
    # jsonData['id'] = id
    # jsonData['Temperature'] = Temperature
    # Temperature = json.dump(jsonData)
    # cur.close()
    # conn.close()
    # wheelsList = models.userRegister.objects.all()
    # name = list(models.userRegister.objects.values_list('name',flat=True))
    # data = list(models.userRegister.objects.values_list('trackid',flat=True))
    # return render(request,'index.html',{'Temperature':Temperature})