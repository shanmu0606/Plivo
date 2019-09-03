import requests
from url import URLFinder
import json

class BaseAPI():
    #def __init__(self):
        #url =  URLFinder()

    def post(self,url,headers=None,data=None,**Kwargs):
        response = requests.post(url,headers=headers,data=None,**Kwargs)
        return response.content

    def get(self,url,params=None):
        response = requests.get(url,params=params)
        return response.content


