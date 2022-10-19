from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from profile_app.models import  MProfile
from profile_app.common import MReference, Repeated
from profile_app.serializers import ProfileSerializer
from django.http import Http404
from django.db import transaction
import json
import os
# from .dbs import DB
from django.http import JsonResponse
from django.shortcuts import render
from django.db.utils import OperationalError
from django.conf import settings
from django.views.generic import (View,TemplateView)
from django.core.exceptions import PermissionDenied
from datetime import date

class Profile():
    def __init__(self):
        pass

    def get_object(self, pk):
        try:
            return MProfile.objects.get(pk=pk)
        except:
            raise Http404

    def remove_profile(self, param):
        result_data = {}
        
        # try:
        # profile_id = MProfile.objects.get(profile_id = param['profile_id'])
        # serialize = ProfileSerializer(profile_id, data=param)
        print(param['profile_id'])
        profile = MProfile.objects.get(profile_id = param['profile_id'])
        profile.reference_tablestatus_fk = MReference.objects.get(reference_id = 2) # Inactive
        profile.save()

        result_data['code'] = status.HTTP_200_OK               
        result_data['profile_id'] = profile.profile_id           
        # except:
        #     result_data['code'] = status.HTTP_400_BAD_REQUEST
        
        return result_data

    def add_profile(self, param):
        result_data = {}

        try:
            profile_id = 1 if MProfile.objects.count() == 0 else MProfile.objects.last().profile_id + 1
            param['profile_id'] = profile_id
            param['addedby_user_id'] = 999999
            print(param)

            serialize = ProfileSerializer(data=param)
            if serialize.is_valid():
                serialize.save() 
                result_data['code'] = status.HTTP_200_OK               
                result_data['data'] = serialize.data    
            else:
                result_data['code'] = status.HTTP_400_BAD_REQUEST
                result_data['message'] = serialize.errors
        except:
            result_data['code'] = status.HTTP_400_BAD_REQUEST
        
        return result_data

    def list_profile(self, param):
        result_data = {}

        try:
            queryset_profile = MProfile.objects.filter(reference_tablestatus_fk=1).filter(firstname__icontains=param).order_by('profile_id') 

            if len(queryset_profile):
                data= list(queryset_profile.values('profile_id'
                                                    ,'firstname','lastname','address','age','birthday')) 

                result_data['code'] = status.HTTP_200_OK   
                result_data['data'] = data
            else:
                result_data['code'] = status.HTTP_400_BAD_REQUEST

        except:
            result_data['code'] = status.HTTP_400_BAD_REQUEST

        return result_data 

    def update_profile(self, param):
        result_data = {}

        try:
            profile_id = self.get_object(param['profile_id'])
            serialize = ProfileSerializer(profile_id, data=param)
            if serialize.is_valid():
                serialize.save() 
                result_data['code'] = status.HTTP_200_OK               
                result_data['data'] = serialize.data    
            else:
                result_data['code'] = status.HTTP_400_BAD_REQUEST
                result_data['message'] = serialize.errors
        except:
            result_data['code'] = status.HTTP_400_BAD_REQUEST
        
        return result_data
