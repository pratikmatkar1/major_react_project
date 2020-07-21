from django.shortcuts import render
import requests
import json
from api.models import UserAPI

# Create your views here.
def signup(request):
    return render(request, 'signup.html')


def submitUser1(request):
    email = request.GET['email']
    password = request.GET['password']
    name = request.GET['Name']
    print(email, password, name, "this is me")

    url = "http://127.0.0.1:8000/apilogin/"

    payload = {"email": email, "password": password, "name": name}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.text
    return render(request, 'temp.html', {'data': data})


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserApiSerializer1
# Create your views here.

from django.shortcuts import get_object_or_404

class UserApiView1(APIView):

    def get(self, request):
        #print(request.data)
        queryset = UserAPI.objects.filter(email=request.data.get('email'))
        if queryset:
            if queryset.values('password').first()['password'] == request.data.get('password'):
                return Response("logged in successfully")
            else:
                return Response("Password is incorrect  ")



        else:
            return Response("Please register")



    def post(self, request):
        queryset = request.data
        serializer = UserApiSerializer1(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()

        return Response("Registered successfully")


    def put(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)

        parsed_data = request.data
        serializer = UserApiSerializer1(instance=queryset, data=parsed_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
        return Response("Updated successfully")



    def delete(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)
        queryset.delete()
        return Response("Deleted successfully")





