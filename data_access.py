import requests
from datetime import datetime

DATA_SOURCE = "hidden stream api"
base_url = "https://hidden-stream-21468.herokuapp.com/"
request_cache = {}

def get_earthquake_count_by_years():
    
    cached_result =  get_cached('get_earthquake_count_by_years')
    if cached_result is not None:
            return cached_result    
    
    xs = []
    ys = []
    resource = "api/earthquakes"
    res = requests.get(base_url + resource)
    if res.status_code == 200:
        print(res.json())
        dict_temp = res.json()
        xs = dict_temp["xs"]
        ys = dict_temp["ys"]
    
    update_cache('get_earthquake_count_by_years', (xs, ys))
    return xs, ys

def get_cached(key):
    if key in request_cache:
        if datediff(datetime.now(), request_cache[key][0]) < 300:
            return request_cache[key][1]
    return None

def update_cache(key, value):
    request_cache[key] = (datetime.now(), value)

def datediff(date1, date2):
    return abs((date1 - date2).seconds)