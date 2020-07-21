
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserApiSerializer
# Create your views here.
from.models import UserAPI
from django.shortcuts import get_object_or_404
from django.shortcuts import render



class UserApiView(APIView):

    def get(self, request):
        #print(request.data)
        queryset = UserAPI.objects.filter(email=request.data.get('email'))

        if queryset:
            if queryset.values('password').first()['password'] == request.data.get('password'):
                return Response("logged in successfullyq2ws")
            else:
                return Response("Password is incorrect")



        else:
            return Response("Please register")



    def post(self, request):
        queryset = request.data
        serializer = UserApiSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()

        return Response("Registered successfully")


    def put(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)

        parsed_data = request.data
        serializer = UserApiSerializer(instance=queryset, data=parsed_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
        return Response("Updated successfully")



    def delete(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)
        queryset.delete()
        return Response("Deleted successfully")


