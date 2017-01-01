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
    single_data = urlopen("http://api.thingspeak.com/channels/148353/feed/last.json?key=K8TNQ7BOCQ3JZMK2&timezone=Asia/Taipei").read().decode('utf-8')
    dataJson = json.loads(single_data)
    temperature  = dataJson.get('field1')
    wet  = dataJson.get('field2')
    ultraviolet_radiation = dataJson.get('field3')
    light_intensity = dataJson.get('field4')
    now = dataJson.get('created_at')
    plot = figure()
    plot.line([1,2,3,4,5],[5,4,3,2,1])
    script, div = components(plot)
    html = template.render(locals())
    return HttpResponse(html)

def status(request):
    template = get_template('status.html')
    return HttpResponse(template)