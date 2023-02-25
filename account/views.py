
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import UserInfo

from rest_framework.permissions import IsAuthenticated

class UsersInfo(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):
        userInfo=UserInfo.objects.all() 
        s1 = UserSerializer(userInfo,many=True)
        return Response(s1.data)
    def post(self, request, *args, **kwargs):
        s1=UserSerializer(data=request.data)
        if s1.is_valid():
            s1.save()
            return Response(s1.data)
        else:
            return Response(s1.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UpdateUserInfo(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request,pk):
        userInfo=UserInfo.objects.get(pk=pk)
        s1=UserSerializer(userInfo)
        return Response(s1.data)
    def put(self, request, pk):
        userInfo=UserInfo.objects.get(pk=pk)
        s1=UserSerializer(userInfo,data=request.data)
        if s1.is_valid():
            s1.save()
            return Response(s1.data)
        else:
            return Response(s1.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        userInfo=UserInfo.objects.get(pk=pk)
        userInfo.delete()
        return {"delete":True}





