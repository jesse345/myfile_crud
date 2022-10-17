
from django.db import models
from django.shortcuts import redirect
import urllib.request
import socket
from django.http import HttpResponse
import uuid
import sys, requests, urllib
import random 
import calendar
import time


class MReference(models.Model):
    reference_id = models.BigIntegerField(primary_key=True)
    reference_group = models.CharField(max_length=100)
    reference_code = models.CharField(max_length=20)
    reference_shortdesc = models.CharField(max_length=100)
    reference_longdesc = models.CharField(
                            max_length=200,
                            null=True,
                            blank=True,
                            default=None  
                            )
    reference_desc = models.CharField(max_length=500)
    reference_groupcode = models.CharField(
                            max_length=20,
                            null=True,
                            blank=True,
                            default=None                            
                            )
    reference_tablestatus_id = models.BigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    addedby_user_id = models.BigIntegerField()
    updatedby_user_id = models.BigIntegerField(
        null=True,
        blank=True
    )
    date_updated = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )

class Repeated:
    def __init__(self):
        pass

    def current_time():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        return current_time

    def send_message(self, data):
        print('Sending Message...') 
        params = (
            ('apikey', self.apikey),
            ('sendername', self.sender),
            ('message', data['message']),
            ('number', data['number'])
        )

        if data['message_type'] == 'message':
            path = 'https://semaphore.co/api/v4/messages?' + urllib.parse.urlencode(params)

        if data['message_type'] == 'otp':            
            path = 'https://semaphore.co/api/v4/otp?' + urllib.parse.urlencode(params)
        print(path)
        res = requests.post(path)
        print(res.json())
        return res.json()

    def send_sms(self, message, number):
        context = {}
        
        context['message'] = message
        context['number'] = number
        context['message_type'] = 'message'
        
        return self.send_message(context)

    def send_otp(self, message, number):
        context = {}
        
        context['message'] = message
        context['number'] = number
        context['message_type'] = 'otp'
        
        return self.send_message(context) 

    def generate_otp(self):
        key = random.randint(999,9999)
        start = random.randint(0, 9)
        end = random.randint(0, 9)
        key = str(start) + str(key) + str(end)
        return key

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]  

    def cleanup_query(query): 
        try:
            # replace all single qoute delimiter to double
            query = query.replace("'", "\"")

            # replace first delimiter
            query = query.replace("\"", "'",1)

            # replace last delimiter
            s = query
            old = '"'
            new = '\''
            maxreplace = 1

            return new.join(s.rsplit(old, maxreplace))
                
        except:
            print("Unable to cleanup")                     


    def empty_to_null(value):
        return 'NULL' if value == None else value         

    def no_record():
        context = {
                 "IsSuccess" : 0
                ,"Result"  : 'No Record Found'
        }

        return context
    
    def form_method_invalid():
        context = {
                 "IsSuccess" : 0
                ,"Result"  : 'Form Method Invalid'
        }

        return context    
    
    def str_to_list(string):
        li = list(string.split(","))
        return li  
    
    def external_ip():
        external_ip = requests.get('https://checkip.amazonaws.com').text.strip()
        return external_ip
    
    def get_local_hostname_ip(output):
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)

            if output == 'host':
                return host_name

            if output == 'ip':
                return host_ip
            
        except:
            return HttpResponse("Unable to get Hostname and IP")    

    def my_random_string(string_length=10):
        """Returns a random string of length string_length."""
        random = str(uuid.uuid4()) # Convert UUID format to a Python string.
        random = random.upper() # Make all characters uppercase.
        random = random.replace("-","") # Remove the UUID '-'.
        return random[0:string_length] # Return the random string.
    
    def key_not_exists(self, key, data):
        return True if key not in data or data[key] == '' else False

    def http_message(self, code):
        if code == 200:
            message = "success"
        elif code == 204:
            message = "no content"              
        elif code == 400:
            message = "bad request"                          
        elif code == 401:
            message = "unauthorized"  
        else:      
            message = "no matching code"
        return message 

    def month_name(month_number):
        return calendar.month_name[month_number]

    def get_reference_id(code):
        queryset = MReference.objects.filter(reference_code = code, reference_tablestatus_id = 1)

        return queryset.values('reference_id')[0]['reference_id']

