from django.shortcuts import render

# Create your views here.
def index(request):
    data={
        'qr_message':'bonjour le monde'
    }
    return render(request,'pages/index.html',data)