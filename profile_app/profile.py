from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.views.generic import (TemplateView)
from django.shortcuts import redirect
from profile_app.libraries.profile_lib import Profile
# from shooting_range.models import MBay, MBooth
from django.http import Http404
# from bo.dbs import DB
import json
from datetime import datetime
import datetime

class View(TemplateView):
    template_name='profile/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['IsLogin'] = self.request.session['IsLogin']
    #     return context

    # def get(self, request, *args, **kwargs):
    #     IsLogin = request.session.get('IsLogin', 0)

    #     if IsLogin == False:
    #         return redirect('/bo/login/')        
    #     else:    
    #         return super().get(request, *args, **kwargs)          

class Transact(viewsets.ViewSet):
    '''
        Author: Armando Garing II
        Date Created: October 05, 2022
        Purpose: Responsible for all transaction
    '''                              
    @staticmethod
    def add_profile(request):
        profile = Profile()
        context, result_data = {}, {}

        data = json.dumps(request.data)
        context = json.loads(data)
        print(context)
        result_data = profile.add_profile(context)
        return Response(result_data, status=status.HTTP_201_CREATED) 

    @staticmethod
    def update_profile(request):
        profile = Profile()
        context, result_data = {}, {}

        data = json.dumps(request.data)
        context = json.loads(data)
        print(context)
        result_data = profile.update_profile(context)
        return Response(result_data, status=status.HTTP_201_CREATED) 

    @staticmethod
    def list_profile(request):
        profile = Profile()
        name = request.GET.get('name', '')
        print(name)
        result_data = profile.list_profile(name)

        return Response(result_data, status=status.HTTP_201_CREATED)                

    @staticmethod
    def remove_profile(request):
        profile = Profile()
        context, result_data = {}, {}

        data = json.dumps(request.data)
        context = json.loads(data)
        print(context)
        result_data = profile.remove_profile(context)
        return Response(result_data, status=status.HTTP_201_CREATED)



      
