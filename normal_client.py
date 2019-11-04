#encoding=utf8
import json
#for urllib
import urllib2
#for requests 
import requests

def client_urllib():
    data = {"info": "world"}
    data_json = json.dumps(data)
    client_url = "http://127.0.0.1:8000"
    request = urllib2.Request(client_url)
    request.add_header('content-TYPE', 'application/json')
    f = urllib2.urlopen(request, data=data_json)
    print f.read()
    return f.read()

#client_urllib()

def client_requests():
    client_url = "http://127.0.0.1:8000"
    data_json = json.dumps({'key1':'value1'})   #dumps：将python对象解码为json数据
    r_json = requests.post(client_url, data_json)
    print(r_json)
    print(r_json.text)
    return r_json.text

#client_requests()
