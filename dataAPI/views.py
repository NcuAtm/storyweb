from django.shortcuts import render, redirect
from .models import UserExtension
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import pytz
import os
import hashlib

def index(request):
    print(request.POST) #print(request.GET.get('a'))
    if request.method=="POST":
        print("index login success!! ")
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        
        if user and user.is_active:
            auth.login(request, user)
            user_e, created = UserExtension.objects.get_or_create(user=user)
            user_e.personal_key = hashlib.md5(os.urandom(32)).hexdigest()
            user_e.save(update_fields=['personal_key']) #change p_k only
            return HttpResponseRedirect('/projects/get/'+request.POST.get('last')+'/'\
+request.POST.get('bd')+'/'+request.POST.get('bt')+'/'+request.POST.get('ed')+'/'+request.POST.get('et'))
        else:
            return HttpResponse("index login did't success!!")
    
    return render(request, 'storyboard.html')

@login_required
def post_detail(request,last,bd,bt,ed,et):
    username = request.user
    user = User.objects.get(username=username)
    u=UserExtension.objects.get(user=user)
    np={
        'name':u.user.username,
        'p_k':u.personal_key,
    }
    s='/dashboard/'+np['p_k']+ '/'+last+ '/'+bd+ '/'+bt+ '/'+ed+ '/'+et
    return HttpResponseRedirect(s)

@login_required
def dashboard(request,pk,last,bd,bt,ed,et):
    print("=======>dashboard okay!")
    compare_username = request.user
    user = User.objects.get(username=compare_username)
    u=UserExtension.objects.get(user=user)

# u-p-a-ad (UserExtension-ProjectData-Aerobox-    AeroboxData)
#           user          pj_name     aerobox_id  pm
#           u_name        start_time  sitename    temp
#           personal_key  end_time                co2
#                                                 rh
#                                                 lon
#                                                 lat
#                                                 time

    u_list, p_list, a_list, ad_list={},{},{},{}
    pn,an,adn=0,0,0
    if(UserExtension.objects.filter(personal_key=pk,user__username=compare_username).first()):#if exists()

        for p in u.projectdata.all(): #can use:filter get(just one)
            for a in p.aerobox.all():
                #for ad in a.aeroboxdata.all():
                ad=a.aeroboxdata.last()
                adp=a.aeroboxdata.filter(rh=90)#QuerySet
                
                print(":::::",bd,bt,'/',str(ad.time).split()[0],'/',str(ad.time).split()[1][0:5])
                print(";;;;;",bd>str(ad.time).split()[0])
                bd=datetime.strptime(bd+bt, '%Y-%m-%d%H:%M')
                print(bd,'//',ad.time)
                bd.astimezone(pytz.utc)
                ad.time.astimezone(pytz.utc)

                try:
                    print(ad.time,"====",bd,"====",ad.time>bd)
                    #print(adp[0].time,"====",bd,"====",adp[0].time>bd)
                except IndexError:
                    print("no adp")
                    

                ad_list={
                             'loading time':ad.time,
                             'lon':ad.lon,
                             'lat':ad.lat,
                             'pm':ad.pm,
                             'temp':ad.temp,
                             'rh':ad.rh,
                             'co2':ad.co2,
                }
                a_list['last:']=ad_list
                adn+=1

#                    print(ad)
#
#                    ad_list={
#                             'loading time':ad.time,
#                             'lon':ad.lon,
#                             'lat':ad.lat,
#                             'pm':ad.pm,
#                             'temp':ad.temp,
#                             'rh':ad.rh,
#                             'co2':ad.co2,
#                    }
#                    a_list[str(adn)]=ad_list
#                    adn+=1

                p_list['aerobox '+a.aerobox_id]=a_list
                an+=1
                a_list={}
                adn=0
            u_list['project"'+p.pj_name+'"']=p_list
            pn+=1
            p_list={}
            an=0

    return JsonResponse(u_list)


