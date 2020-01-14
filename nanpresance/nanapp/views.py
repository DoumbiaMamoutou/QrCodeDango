from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from datetime import date,datetime,time
from  django.contrib.auth import  authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .import models
from django.utils.translation import ugettext_lazy as _

# Create your views here.


def login_page(request):

    return render(request,'dashbord/login.html')
def register(request):
    return render(request,'dashbord/register.html')
@login_required(login_url='login')

def index(request):

    # isQr =models.Qrcode.objects.filter(jours=date.today(),status=True).exists()
    # qrDesactive = models.Qrcode.objects.filter(jours=date.today(),status=False).exists()
    # nbr_student=models.Profile.objects.all().count()
    # nbr_presant=models.Presence.objects.filter(status=True).count()
    # nbr_abs = models.Presence.objects.filter(jour=date.today(),status=False).count()
    # if(isQr):
    #     myQr=models.Qrcode.objects.filter(jours=date.today(),status=True)[:1].get()
    #     list_presence = models.Presence.objects.filter(jour=date.today())

    try:
        isQr = models.Qrcode.objects.filter(jours=date.today(),status=True).exists() 
        qrDesactive = models.Qrcode.objects.filter(jours=date.today(),status=False).exists()
        todays = date.today()
        date_of_days = _(todays.strftime("%A"))
        groupe = models.Groupe.objects.filter(jour_passage__nom__startswith = date_of_days)

        for g in groupe:
            nom = g.nom
        nbr_student = models.Profile.objects.filter(groupe__nom = nom).count()

        nbr_presant=models.Presence.objects.filter(jour=date.today(),status=True).count()
        nbr_abs = models.Presence.objects.filter(jour=date.today(),status=False).count()
        jan = models.Presence.objects.filter(created_at__month = 1 ,status=True).count()
        feb = models.Presence.objects.filter(created_at__month = 2 ,status=True).count()
        mars = models.Presence.objects.filter(created_at__month = 3 ,status=True).count()
        avril = models.Presence.objects.filter(created_at__month = 4 ,status=True).count()
        mai = models.Presence.objects.filter(created_at__month = 5 ,status=True).count()
        juin = models.Presence.objects.filter(created_at__month = 6 ,status=True).count()
        july = models.Presence.objects.filter(created_at__month = 7 ,status=True).count()
        aout = models.Presence.objects.filter(created_at__month = 8 ,status=True).count()
        sept = models.Presence.objects.filter(created_at__month = 9 ,status=True).count()
        octobre = models.Presence.objects.filter(created_at__month = 10 ,status=True).count()
        nov = models.Presence.objects.filter(created_at__month = 11 ,status=True).count()
        dec = models.Presence.objects.filter(created_at__month = 12 ,status=True).count()
      
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(isQr)  
    except exception as e:
        print(str(e))
        

    if(isQr):
        try:
            
            myQr=models.Qrcode.objects.filter(jours=date.today(),status=True)[:1].get()
            list_presence =models.Presence.objects.filter(jour=date.today())
            jan = models.Presence.objects.filter(created_at__month = 1 ,status=True).count()
            feb = models.Presence.objects.filter(created_at__month = 2 ,status=True).count()
            mars = models.Presence.objects.filter(created_at__month = 3 ,status=True).count()
            avril = models.Presence.objects.filter(created_at__month = 4 ,status=True).count()
            mai = models.Presence.objects.filter(created_at__month = 5 ,status=True).count()
            juin = models.Presence.objects.filter(created_at__month = 6 ,status=True).count()
            july = models.Presence.objects.filter(created_at__month = 7 ,status=True).count()
            aout = models.Presence.objects.filter(created_at__month = 8 ,status=True).count()
            sept = models.Presence.objects.filter(created_at__month = 9 ,status=True).count()
            octobre = models.Presence.objects.filter(created_at__month = 10 ,status=True).count()
            nov = models.Presence.objects.filter(created_at__month = 11 ,status=True).count()
            dec = models.Presence.objects.filter(created_at__month = 12 ,status=True).count()

            data={
                'myQr':myQr,
                'isQr':True,
                'liste_presence':list_presence,
                'nbr_etudiant':nbr_student,
                'nbr_presant':nbr_presant,
                'nbr_abs':nbr_abs,
                'jan':jan,
                'feb':feb,
                'mars':mars,
                'avril':avril,
                'mai':mai,
                'juin':juin,
                'july':july,
                'aout':aout,
                'sept':sept,
                'october':octobre,
                'nov':nov,
                'dec':dec,
                'nom':nom
                
                
            }
        except exception as e:
            pass

    elif qrDesactive:
        try:
            jan = models.Presence.objects.filter(created_at__month = 1 ,status=True).count()
            feb = models.Presence.objects.filter(created_at__month = 2 ,status=True).count()
            mars = models.Presence.objects.filter(created_at__month = 3 ,status=True).count()
            avril = models.Presence.objects.filter(created_at__month = 4 ,status=True).count()
            mai = models.Presence.objects.filter(created_at__month = 5 ,status=True).count()
            juin = models.Presence.objects.filter(created_at__month = 6 ,status=True).count()
            july = models.Presence.objects.filter(created_at__month = 7 ,status=True).count()
            aout = models.Presence.objects.filter(created_at__month = 8 ,status=True).count()
            sept = models.Presence.objects.filter(created_at__month = 9 ,status=True).count()
            octobre = models.Presence.objects.filter(created_at__month = 10 ,status=True).count()
            nov = models.Presence.objects.filter(created_at__month = 11 ,status=True).count()
            dec = models.Presence.objects.filter(created_at__month = 12 ,status=True).count()
            
            list_presence =models.Presence.objects.filter(jour=date.today())
            
            data={
            "isQr":False,
            'nbr_etudiant': nbr_student,
            'nbr_presant': nbr_presant,
            'liste_presence':list_presence,
            'nbr_abs': nbr_abs,
            'jan':jan,
            'feb':feb,
            'mars':mars,
            'avril':avril,
            'mai':mai,
            'juin':juin,
            'july':july,
            'aout':aout,
            'sept':sept,
            'october':octobre,
            'nov':nov,
            'dec':dec,
            'nom':nom
            
            }
        except exception as e:
            pass


    else:
        data={
        "isQr":False,
        'nbr_etudiant': nbr_student,
        'nbr_presant': nbr_presant,
        'nbr_abs': nbr_abs,
        'jan':jan,
        'feb':feb,
        'mars':mars,
        'avril':avril,
        'mai':mai,
        'juin':juin,
        'july':july,
        'aout':aout,
        'sept':sept,
        'october':octobre,
        'nov':nov,
        'dec':dec,
        'nom':nom
        }
        

    
    return render(request,'dashbord/index.html',data)


def scanner(request):
    try:
        
        
        isQr =models.Qrcode.objects.filter(jours=date.today(),status=True).exists()
        qrDesactive = models.Qrcode.objects.filter(jours=date.today(),status=False).exists()
        
    except exception as e:
        pass



    if(isQr):
        try:
            myQr=models.Qrcode.objects.filter(jours=date.today(),status=True)[:1].get()
            list_presence = models.Presence.objects.filter(jour=date.today())(0)
        except :
            pass

            
        data={
            'myQr':myQr,
            'isQr':True,
        }
    else:
        data={
        "isQr":False,
        }
    
    return render(request,'dashbord/qrCode_page.html',data)


def postLogin(request):
    if request.method == "POST":
        
        login_user = request.POST.get('login',False)
        password = request.POST.get('pass',False)
    
        user = authenticate(request,username=login_user,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            data={
                'error':True,
                'login':login,
                'pass':password
            }
        return render(request,'pages/login.html',data)
    
def postRegister(request):
    if request.method == "POST":
        
        try:
            login =request.POST.get('login',False)
            email =request.POST.get('email',False)
            password =request.POST.get('pass',False)
            repass = request.POST.get('repass',False)
        except exception as e:
            pass

        error=None
        print("################### registe post ###############")
        print(login,email,password)

    if(len(login) < 3):
        message='Login trop court '
        error =True
    if(password != repass):
        message ='Error password'
        error = True
    try:
        verifU = User.objects.filter(username=login)
    except :
        pass

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
        message ="Error Username  "
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
    try:
        post_data=json.loads(request.body.decode('utf-8'))
        jours =post_data['jours']
        hDebut=post_data['heurDebut']
        hFin=post_data['heurFin']
        
    except Exception as e:
        data={
            'success':False,
            'message':'Error de convertion des variables'
        }
        print("Error de recuperration des variables:",str(e))

    try:
        my_user =models.Qrcode.objects.filter(jours=date.today())[:1].get()
        qrExist=True
        
    except Exception as e:
        qrExist=False
        print("Exection Qr Existe ",str(e))
    
    if not qrExist:
        try:
            new_qr_code = models.Qrcode(debut_heure_arrivee=hDebut,fin_heure_arrivee=hFin,created_by=request.user)
            new_qr_code.save()
            # ceration de la liste de presance
            todays = date.today()
            date_of_days = _(todays.strftime("%A"))
            groupe = models.Groupe.objects.filter(jour_passage__nom__startswith = date_of_days)

            for g in groupe:
                nom = g.nom
            all_user = models.Profile.objects.filter(groupe__nom = nom)

            for u in all_user:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                my_list = models.Presence(jour=date.today(),etudiant=u,qrcode=new_qr_code,heure_arrivee=current_time)
                my_list.save()
            data ={
                'success':True,
                'message':'code qr genere avec succes '
            }
        except Exception as e:
            print("Error to adding Qr code ",str(e))
            data ={
                'success':False,
                'message':'Error dans creation du code Qr '
            }
    else:
        data ={
            'success':False,
            'message':'un Code Qr a déja été generer'
        }

    return JsonResponse(data,safe=True)

def unActiveQr(request):
    try:
        post_data=json.loads(request.body.decode('utf-8'))
        jours = date.today()
    except Exception as e:
        print("Error Recupperation veriable :",str(e))
        data={
            'success':False,
            'message':'Error Recupperation variable '
        }
    try:
        new_qr_code = models.Qrcode.objects.filter(jours=jours)[:1].get()
        new_qr_code.status=False
        new_qr_code.save()
        data={
            'success':True,
            'message':'Update ok '
        }
    except Exception as e:
        print("Error to find CodeQr ",str(e))
        data={
            'success':False,
            'message':'Error to find CodeQr '
        }
    return JsonResponse(data,safe=True)
def logout_page(request):
    logout(request)
    return redirect('login')
    