from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json

def login_page(request):
    return render(request, 'accounts/login.html')

def ajax_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "fail"})
