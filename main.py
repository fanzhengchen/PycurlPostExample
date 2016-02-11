import os
import pycurl
import json

url = '127.0.0.1:8080/post'
data = json.dumps({"name": "fzc", "email": "fanzhengchen@gmail"})

curl = pycurl.Curl()
curl.setopt(pycurl.URL, url)
curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json']);
curl.setopt(pycurl.POST, 1)
curl.setopt(pycurl.POSTFIELDS, data)
curl.perform()
