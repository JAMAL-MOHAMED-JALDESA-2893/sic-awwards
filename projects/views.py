from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import profileForm,UserUpdateForm,RegistrationForm,projectForm,UpdateUserProfileForm,RateForm
from .models import Projects,Profile
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile,Projects,Revieww
from .serializer import ProfileSerializer,ProjectSerializer