from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from urllib.request import urlopen
import json
# Create your views here.
def homepage(request):
	template = get_template('index.html')
	data = urlopen("https://api.thingspeak.com/channels/202242/fields/1.json?key=YTCKLSZDCL10P60Q&results=1")\
	.read().decode('utf-8')
	dataJson = json.loads(data)
	meta = dataJson.get("feeds")[0]['field1']
	html = template.render(locals())
	return HttpResponse(html)