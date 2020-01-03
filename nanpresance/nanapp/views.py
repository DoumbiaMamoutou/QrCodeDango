from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from datetime import date,datetime,time
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .import models

# Create your views here.

def login(request):
    return render(request,'pages/login.html')
def register(request):
    return render(request,'pages/register.html')
def index(request):
    isQr =models.Qrcode.objects.filter(jours=date.today()).exists()
    nbr_student=models.Profile.objects.all().count()
    nbr_presant=models.Presence.objects.filter(status=True).count()
    nbr_abs = models.Presence.objects.filter(status=False).count()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(isQr)
    if(isQr):
        myQr=models.Qrcode.objects.filter(jours=date.today(),status=True)[:1]
        list_presence =models.Presence.objects.filter(jour=date.today())
        data={
            'myQr':myQr,
            'isQr':True,
            'liste_presence':list_presence,
            'nbr_etudiant':nbr_student,
            'nbr_presant':nbr_presant,
            'nbr_abs':nbr_abs
        }
    else:
        data={
            "isQr":False,
            'nbr_etudiant': nbr_student,
            'nbr_presant': nbr_presant,
            'nbr_abs': nbr_abs
        }
    return render(request,'pages/index.html',data)

def scanner(request):
    data={
        'qr_message':'bonjour le monde'
    }
    return render(request,'pages/scanner.html',data)


def postLogin(request):
    login = request.POST.get('login',False)
    password = request.POST.get('pass',False)
    
    my_user = authenticate(username=login,password=password)
    if(my_user is not None):
        return redirect('index')
    else:
        data={
            'error':True,
            'login':login,
            'pass':password
        }
        return render(request,'pages/login.html',data)
    
def postRegister(request):
    login =request.POST.get('login',False)
    email =request.POST.get('email',False)
    password =request.POST.get('pass',False)
    repass = request.POST.get('repass',False)
    error=None
    print("################### registe post ###############")
    print(login,email,password)

    if(len(login) < 3):
        message='Login trop court '
        error =True
    if(password != repass):
        message ='Error password'
        error = True
    verifU = User.objects.filter(username=login)
    print(verifU)
    if(verifU):
        error =True
        message = "desole ce login existe dejat ;-("
   
    try:
        myU =User(username=login,email=email)
        myU.save()
        myU.password=password
        myU.set_password(myU.password)
        myU.save()
    except Exception as e :
        error =True
        message =str(e)
    if(error):
        data={
            'error':True,
            'message':message,
            'login':login,
            'email':email,
            
        }
        return render(request,'pages/register.html',data)
    else:
        return redirect('index')

def addQrCode(request):
    post_data=json.loads(request.body.decode('utf-8'))
    jours =post_data['jours']
    if models.Qrcode.objects.filter(jours=jours).exists():
        data={
            'success':False,
            'message':'le code a dejat ete genere '
        }
    else:
        new_qr_code = models.Qrcode(jours=jours,created_by=request.user)
        new_qr_code.save()
        # ceration de la liste de presance
        all_user = models.Profile.objects.filter(status=True)
        for u in all_user:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            my_list = models.Presence(jour=date.today(),etudiant=u,qrcode=new_qr_code,heure_arrivee=current_time)
            my_list.save()
        data ={
            'success':True,
            'message':'code qr genere avec succe '
        }
    return JsonResponse(data,safe=True)