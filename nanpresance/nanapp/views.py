from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import date,datetime,time
from .import models

# Create your views here.
def index(request):
    isQr =models.Qrcode.objects.filter(jours=date.today()).exists()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(isQr)
    if(isQr):
        myQr=models.Qrcode.objects.get(jours=date.today())
        list_presence =models.Presence.objects.filter(jour=date.today())
        data={
            'myQr':myQr,
            'isQr':True,
            'liste_presence':list_presence
        }
    else:
        data={
            'isQr':False
        }
    return render(request,'pages/index.html',data)

def scanner(request):
    data={
        'qr_message':'bonjour le monde'
    }
    return render(request,'pages/scanner.html',data)

def addQrCode(request):
    post_data=json.loads(request.body.decode('utf-8'))
    jours =post_data['jours']
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
        
    }
    return JsonResponse(data,safe=True)