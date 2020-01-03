from django.shortcuts import render
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
            message = "bon identifinat"

        else:
            
            status=False
            message = "Username ou password incorect"

    return JsonResponse({
            'status':status,
            'message':message
        })