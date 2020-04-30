from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .telegram.params import *
from .telegram.api_models import Update
from .telegram.api_method import send_message, send_photo#, send_html_message#and orters
from .models import TelegramChat#, Knowledge, Policy
import requests
import json

def webhook(request):
    if request.method == "POST":
        print('hey bro!')
        j_data = json.loads(request.body.decode())
        u_data = Update.json_deserializer(j_data)
        if u_data != None:
            if u_data.message.text == '/wantjson':
                print('/wantjson')
                return_json={
                    'test':'this is test',
                    'num':123,
                    'face':':)',
                }
                send_message(u_data.message.chat_belong_to.id,return_json)

            if u_data.message.text == '/get_storyweb':
                print('/get_storyweb')
                send_message(u_data.message.chat_belong_to.id,'https://106601015.pythonanywhere.com')

            if u_data.message.text == '/get_testphoto':
                print('/get_testphoto')
                sended_urls = 'https://upload.cc/i1/2020/04/30/PQvDJW.png'
                send_photo(u_data.message.chat_belong_to.id, sended_urls)
#https://hackstime.com/wp-content/uploads/2019/07/Django-python-tutorial.png

            if u_data.message.photo != None:
                print('/get_pictest')
                print('u_data.message.photo  ',u_data.message.photo)
                send_message(u_data.message.chat_belong_to.id,'return your image :)')
                send_photo(u_data.message.chat_belong_to.id, u_data.message.photo[0]['file_id'])

        return HttpResponse('ok')
    else:
        return HttpResponse("This page is for telegram post, but you are getting!")

