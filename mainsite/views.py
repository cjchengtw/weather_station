# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from urllib.request import urlopen
from bokeh.plotting import figure, output_file,Row
import json 
from bokeh.embed import components
from bokeh.models.widgets import Slider,RadioButtonGroup
from datetime import datetime
from django.views.generic.base import View,TemplateView
from bokeh.layouts import gridplot
from django.core.mail import EmailMessage
from mainsite import forms
# Create your views here.
def draw(data,field):
    plot = figure(tools="",logo=None,x_axis_type="datetime")
    #plot.line([i for i in range(0,100)],[float(data[i]['field1']) for i in range(0,100)])
    plot.line([i for i in range(0,100)],[data[i].get('{}'.format(field)) for i in range(0,100)])
    return plot
def is_leap(year):
    if year % 400 == 0 or year % 4 ==0 and year % 100 != 0:
        return False
    else:
        return True
        
def convert_time(now):
    solar_month=[1,3,5,7,8,10,12]
    lunar_month=[4,6,9,11]
    february = [2]
    date,time = now.split('T')
    year,month,day = date.split('-')
    year,month,day = int(year),int(month),int(day)
    normal,jet_lag = time.split('+')     
    hour,minute,second = normal.split(':')
    d_hour,d_minute = jet_lag.split(':')
    minute = int(minute) + int(d_minute)    
    hour = int(hour) + int(d_hour)
    if hour> 24:
        hour -= 24
        if month in solar_month:
            if day == 31:
                month += 1
        elif month in february:
            if is_leap(year):
                if day == 29:
                    month += 1
            else:
                if day == 27:
                    month +=1
        elif month in lunar_month:
            if day == 30:
                month += 1
        if month > 12:
            year += 1
            month = 1
    return year,month,day,hour,minute,second
def homepage(request):  
    template = get_template('index.html')
    
    last_data = urlopen("http://api.thingspeak.com/channels/148353/feed/last.json?key=K8TNQ7BOCQ3JZMK2&timezone=Asia/Taipei").read().decode('utf-8')
    
    lastdataJson = json.loads(last_data)
    
    
    tpr = lastdataJson.get('field1')
    wet  = lastdataJson.get('field2')
    ur = lastdataJson.get('field3')
    li = lastdataJson.get('field4')    
    observe_time = lastdataJson.get('created_at')
    year,month,day,hour,minute,second = convert_time(observe_time)
    recent_time = str(datetime.now())
    html = template.render(locals())
    return HttpResponse(html)



    #temperature->tpr, ultraviolet_radiation->ur,light_intensity->li
def status(request):
    template = get_template('status.html')
    data_group = urlopen("https://api.thingspeak.com/channels/148353/fields/1.json?key=K8TNQ7BOCQ3JZMK2&timezone=Asiz/Taipei").read().decode('utf-8')
    datagroupJson = json.loads(data_group)
    data  = datagroupJson.get('feeds')
    button_group = RadioButtonGroup(labels=["溫度", "濕度", "光照度"], active=0)
    #layout = Column(button_group,plot)          # 將圖表與 Slider 與RadioButtonGroup排版
    tmp_plot = draw(data,'field1')
    wtr_plot = draw(data,'field1')
    #ur_plot = draw(data,'field3')
    #li_plot = draw(data,'field4')
   
    #plots = {'tmp': tmp_plot, 'wet': tmp_plot, 'ur': tmp_plot, 'li': tmp_plot}
    # plots = (tmp_plot,wet_plot,ur_plot,li_plot)
   
   
   #grid = gridplot([tmp_plot,wtr_plot],[ur_plot,li_plot]) 
    grid = Row(tmp_plot,wtr_plot)
    script,div = components(grid)
    html = template.render(locals())
    return HttpResponse(html)

def form(request):
    if request.method == 'POST':
        form = forms.Contact(request.POST)
        if form.is_valid():
            message = "感謝回饋！"
        else:
            message = "請再次檢查您的輸入資訊。"
    else:
        form = forms.Contact()
    form = forms.Contact()
    template = get_template('form.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    
    return HttpResponse(html)    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #temperature  = dataJson.get('field1')
