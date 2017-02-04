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

def convert_time(now):
    date,time = now.split('T')
    year,month,day = date.split('-')
    normal,jet_lag = time.split('+')     
 
def homepage(request):  
    template = get_template('index.html')
    
    last_data = urlopen("http://api.thingspeak.com/channels/148353/feed/last.json?key=K8TNQ7BOCQ3JZMK2&timezone=Asia/Taipei").read().decode('utf-8')
    
    lastdataJson = json.loads(last_data)
    
    
    tpr = lastdataJson.get('field1')
    wet  = lastdataJson.get('field2')
    ur = lastdataJson.get('field3')
    li = lastdataJson.get('field4')    
    observe_time = lastdataJson.get('created_at')
    #year,month,day = convert_time(now)
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
