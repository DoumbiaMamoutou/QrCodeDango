from django.shortcuts import render
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
from django.http import JsonResponse ,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date,datetime,time
from nanapp.models import *
import json

import ipaddress
# Create your views here.



Nan = ipaddress.ip_network('192.168.50.0/24')
for x in Nan.hosts():
     
    print(x)  



@csrf_exempt
def login(request):
    status = False
    message = ""
    data ={}
    if request.method == "POST":
        try:
            postdata = json.loads(request.body.decode('utf-8'))
            username =  postdata['username']
            password = postdata['password']
        except :
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            
        user = authenticate(username=username, password=password)
        if user is not None:
            
            profile = Profile.objects.filter(user=user).values('contacts','user__username','genre','user__email','specialite','images',)[:1].get()
            
            data = {
                    'user':profile,
                    }
            return JsonResponse(data)

        else:
            return HttpResponse(status=401)


    

@csrf_exempt
def qrverif(request):
    status = False
    message = ""
    if request.method == "POST":
        try:
            postdata = json.loads(request.body.decode('utf-8'))
            username =  postdata['username']
            qrcode = postdata['qrcode']
            ip_adress = postdata['ip_adrrese']
        except Exception as e:
            print("erro in ",str(e))
            message=str(e)
            username = request.POST.get('username',None)
            qrcode = request.POST.get('qrcode',None)
            ip_adress = request.POST.get('ip_adrrese',None)
        try:
            print(username)
            user = User.objects.filter(username=username)[:1].get()
            if user is not None:
                if ipaddress.ip_address('{ip}'.format(ip=ip_adress)) in ipaddress.ip_network('192.168.50.0/24'):
                    try:
                        jours = date.today()
                        code = Qrcode.objects.filter(jours=jours)[:1].get()
                        if code.is_valid:
                            try:
                                print("un")
                                profile = Profile.objects.filter(user=user)[:1].get()
                                print("deux")
                                presence = Presence.objects.filter(etudiant=profile,jour=jours).get()
                                print("status code ",presence.status)
                                if presence.status == False:
                                    if qrcode == code.titre_slug:
                                        presence.status = True
                                        status = True
                                        message = 'Success'
                                        presence.save()
                                    else:
                                        status = False
                                        message = 'mauvais QR_CODE'
                                else:
                                    status = False
                                    message = 'Vous avez deja marquer votre presence' 
                            except Exception as e:
                                message =str(e)
                                print("IN MY EXECPTION ",str(e))
                        else:
                            return HttpResponse(status=422)
                        
                    except :
                        pass
    
                else:
                    status = False
                    message = 'Vous devez etre a NaN avant de Scaner le QrCode' 
                    
                
        except Exception as e:
            message=str(e)
            status=False
    
    if not status:
        
        
        return  JsonResponse({"status":status,"message":message},safe=True)
        
    else:
        
        data={
            "status":status,
            "message":message
        }
        return JsonResponse(data,safe=True)