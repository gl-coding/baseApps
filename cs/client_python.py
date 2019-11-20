#encoding=utf8
import json
#for urllib
import urllib2
#for requests 
import requests

data_global = {"info": "world"}
url_addr    = "http://127.0.0.1:8000"

def client_urllib():
    data_json  = json.dumps(data_global)
    client_url = url_addr
    request    = urllib2.Request(client_url)
    request.add_header('content-TYPE', 'application/json')
    f = urllib2.urlopen(request, data=data_json)
    print f.read()
    return f.read()

#client_urllib()

def client_requests():
    client_url = url_addr
    data_json  = json.dumps(data_global)   #dumps：将python对象解码为json数据
    r_json = requests.post(client_url, data_json)
    print(r_json.text)
    return r_json.text

client_requests()
