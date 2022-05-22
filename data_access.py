import requests
from datetime import datetime

DATA_SOURCE = "hidden stream api"
base_url = "https://hidden-stream-21468.herokuapp.com/"

def get_earthquake_count_by_years():
    xs = []
    ys = []
    resource = "api/earthquakes"
    res = requests.get(base_url + resource)
    if res.status_code == 200:
        dict_temp = res.json()
        xs = dict_temp["xs"]
        ys = dict_temp["ys"]
    return xs, ys