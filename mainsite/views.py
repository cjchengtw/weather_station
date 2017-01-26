from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from bokeh.resources import CDN
from urllib.request import urlopen
import json
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
# Create your views here.
def homepage(request):
    template = get_template('index.html')
    data = urlopen("http://api.thingspeak.com/channels/148353/feed/last.json?key=K8TNQ7BOCQ3JZMK2&timezone=Asia/Taipei").read().decode('utf-8')
    dataJson = json.loads(data)
    #temperature  = dataJson.get('field1')
    #wet  = dataJson.get('field2')
    #ultraviolet_radiation = dataJson.get('field3')
    #light_intensity = dataJson.get('field4')
    #now = dataJson.get('created_at')
    
    plot = figure(tools="",logo=None)
    plot.line([i for i in range(0,100)],[float(data[i]['field1']) for i in range(0,100)]) #temperature
    slide = Slider()                 # 建立 Slider
    layout = hplot(plot,slide)          # 將圖表與 Slider 利用 hplot 排版
    script, div = components(plot)
    html = template.render(locals())
    return HttpResponse(html)

def status(request):
    template = get_template('status.html')
    html = template.render(locals())
    return HttpResponse(html)