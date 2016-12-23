from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from urllib.request import urlopen
import json
# Create your views here.
def homepage(request):
    template = get_template('index.html')
    data = urlopen("http://api.thingspeak.com/channels/148353/feed/last.json?key=K8TNQ7BOCQ3JZMK2").read().decode('utf-8')
    dataJson = json.loads(data)
    temperature  = dataJson.get('field1')
    wet  = dataJson.get('field2')
    ultraviolet_radiation = dataJson.get('field3')
    light_intensity = dataJson.get('field4')
    now = dataJson.get('created_at')
    html = template.render(locals())
    return HttpResponse(html)