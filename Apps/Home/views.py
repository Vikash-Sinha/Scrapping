from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.http import JsonResponse
import datetime
import xlrd
from djqscsv import render_to_csv_response

from django.db.models import Q
import pandas as pd

class NewXlsFile(View):
    template = 'Home/new_xls_file.html'
    def get(self,request):
        return render(request,self.template)
    def post(self,request):
        # import pdb
        # pdb.set_trace()
        file = request.FILES.get('files')
        df = pd.ExcelFile(file)
        sheet_count = len(df.sheet_names)
        for sheet_index in range(sheet_count):
            sheet = df.parse(sheet_index)
            for i in range(1,sheet.shape[0]):
                if sheet.iat[i,8] is not None:
                    obj = ScrappingData()
                    if str(sheet.iat[i,2]) is not None:
                        obj.language = sheet.iat[i,2]
                    if str(sheet.iat[i, 3]) is not None:
                        obj.plateform = sheet.iat[i,3]
                    if str(sheet.iat[i, 4]) is not None:
                        obj.state = sheet.iat[i,4]
                    if str(sheet.iat[i, 5]) is not None:
                        obj.influancer = sheet.iat[i,5]
                    if str(sheet.iat[i, 6]) is not None:
                        obj.channel_name = sheet.iat[i,6]
                    if str(sheet.iat[i, 7]) is not None:
                        obj.type = sheet.iat[i,7]
                    if str(sheet.iat[i, 8]) is not None:
                        obj.link = sheet.iat[i,8]
                    if str(sheet.iat[i, 9]) is not None:
                        obj.subscriber = sheet.iat[i,9]
                    if str(sheet.iat[i, 10]) is not None:
                        obj.avg_view = sheet.iat[i,10]
                    if str(sheet.iat[i, 14]) is not None:
                        obj.contact_no = sheet.iat[i,14]
                    if str(sheet.iat[i, 15]) is not None:
                        obj.email_id = sheet.iat[i,15]
                    obj.save()
        return redirect('home')

def delQuery(request):
    obj = ScrappingData.objects.filter(~Q(link__startswith='https:'))
    obj.delete()
    return redirect('home')

class Home(View):
    template = 'Home/home.html'
    def get(self,request):
        state = request.GET.get('state')
        type = request.GET.get('type')
        avg = request.GET.get('avg')
        subs = request.GET.get('subs')
        platform = request.GET.get('platform')
        influencer = request.GET.get('influencer')
        lang = request.GET.get('lang')
        down = request.GET.get('down')
        obj = ScrappingData.objects.all().order_by('-pk')
        if state is not '' and state is not None :
            obj = obj.filter(state__icontains=state)
        if platform is not '' and platform is not None:
            obj = obj.filter(plateform__icontains=platform)
        if subs is not '' and subs is not None:
            obj = obj.filter(subscriber__gte=subs)
        if avg is not '' and avg is not None:
            obj = obj.filter(avg_view__gte=avg)
        if type is not '' and type is not None:
            obj = obj.filter(type__icontains=type)
        if influencer is not '' and influencer is not None:
            obj = obj.filter(influancer__icontains=influencer)
        if lang is not '' and lang is not None:
            obj = obj.filter(language__icontains=lang)

        if down is not '' and down is not None:
            obj = obj.values('id', 'language','plateform','state','influancer','channel_name','type','link','subscriber','avg_view','feature','review','pokar','contact_no','email_id')
            return render_to_csv_response(obj)
        total = obj.count()
        paginator = Paginator(obj, 50)
        page_number = request.GET.get('page')
        obj = paginator.get_page(page_number)
        context={
           'state':state,
            'type':type,
            'avg':avg,
            'lang':lang,
            'subs':subs,
            'platform':platform,
            'influancer': influencer,
            'scrap_obj': obj,
            'total': total
        }
        return render(request,self.template,context)
