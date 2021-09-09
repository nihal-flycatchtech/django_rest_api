from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from create_user.api.serializers import Registerserializers


class Registration_view(APIView):


    def post(self,request):


        if request.method=='POST':
            serializer=Registerserializers(data=request.data)
            data={}
            if serializer.is_valid():
                account=serializer.save()
                data['response']="successfully registered a new user"
                data['email']=account.email
                data['username'] = account.username
            else:
                data=serializer.errors
            return Response(data)

class HelloView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        content = {'message': 'Hello,World'}
        return Response(content)





