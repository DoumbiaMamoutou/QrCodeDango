from django.shortcuts import render
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date,datetime,time
from nanapp.models import *
# Create your views here.

@csrf_exempt
def login(request):
    status = False
    message = ""
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
            status = True
            message = "bon identifiant"

        else:
            
            status=False
            message = "Username ou password incorect"

    return JsonResponse({
            'status':status,
            'message':message
        })
    
@csrf_exempt
def qrverif(request):
    status = False
    message = ""
    if request.method == "POST":
        try:
            postdata = json.loads(request.body.decode('utf-8'))
            username =  postdata['username']
            qrcode = postdata['qrcode']
            
        except :
            username = request.POST.get('username',None)
            qrcode = request.POST.get('qrcode',None)

        user = User.objects.filter(username=username)[:1].get()
        if user is not None:
            try:
                jours = date.today()
                code = Qrcode.objects.filter(jours=jours)[:1].get()
                if code.is_valid:    
                    try:
                        profile = Profile.objects.filter(user=user)[:1].get()
                        presence = Presence.objects.filter(etudiant=profile,jour=jours)[:1].get()
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

                    except :
                        pass
                else:
                    
                    status = False
                    message = "l'heure requise est passée"

                    
            except:
                
                pass

    return JsonResponse({
            'status':status,
            'message':message
        })