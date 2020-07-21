from django.shortcuts import render
import requests
import json
# Create your views here.


def loginpage(request):
    return render(request, 'loginpage.html')

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')

def listing(request):
    return render(request, 'listing.html')



def submitUser(request):
    email = request.GET['email']
    password = request.GET['password']
    name = request.GET['Name']
    print(email, password, name, "this is me")

    url = "http://127.0.0.1:8000/api/login/"

    payload = {"email": email, "password": password, "name": name}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.text
    return render(request, 'temp.html', {'data': data})



def submitUser(request):
    email = request.GET['email']
    password = request.GET['password']
    name = request.GET['Name']
    print(email, password, name, "this is me")

    url = "http://127.0.0.1:8000/api/login/"

    payload = {"email": email, "password": password, "name": name}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.text
    return render(request, 'temp.html', {'data': data})
