  
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
User = get_user_model()
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# Create your views here.
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import(
RegistrationSerializer,
LoginSerializer
)
def validate_email(email):
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if user != None:
        return email
@api_view(['POST',])
#permission_classes = [AllowAny]
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        data = {}
        context={}
        email={}

        email = request.data.get('email')
        if validate_email(email) != None:
            context['sucess'] = False
            context['response'] = status.HTTP_403_FORBIDDEN
            context['error_message'] = 'That email is already in use.'
            context['data']=data
            return Response(context)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            context['sucess'] = True
            context['error_message'] = 'Sucessfully registered'
            context['response'] = status.HTTP_201_CREATED
            data['email'] = user.email
            data['username'] = user.username
            data['Is_User'] = user.Is_User
            token = Token.objects.create(user=user).key
            data['token'] = token
            data = serializer.errors
            context['data']=data
        else:
            context['sucess'] = False
            context['message'] = 'not registered registered'
            context['response'] = status.HTTP_401_UNAUTHORIZED
            data = serializer.errors
            context['error_message']=data
    return Response(context)

@api_view(('GET',))
@permission_classes((AllowAny,))
def activate(request, uidb64, token):
    context={}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
       # user.profile.email_confirmed = True
        user.save()
        #login(request, user)
        context['status']=status.HTTP_201_CREATED
    return Response(context)


@api_view(['POST',])
@permission_classes((AllowAny,))
def ObtainAuthTokenView(request):
    if request.method=='POST':
        serializer=LoginSerializer(data=request.data)
        context={}
        data={}
        if serializer.is_valid(raise_exception=True):
            #serializer.save()
            usernam=serializer.validated_data['username']
            passwor=serializer.validated_data['password']
            account=authenticate(username=usernam ,password=passwor)
            if account:
                try:
                    token = Token.objects.get(user=account)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=account)
                context['response']=200
                context['success']=True
                context['error_message']="sucessfull login"
                data['token'] = token.key
                data['username']=account.username
                data['email']=account.email
                data['id']=account.id
                context['data']=data
            else:
                context['success']=False
                context['status']: 440
                context['response'] = 'Error'
                context['error_message'] = 'Invalid credentials'
        return Response(context)