import requests

post_data={
    "info":"hahaha",
}

res=requests.post(url="http://127.0.0.1:8000/",data=post_data)
print(res.text)
