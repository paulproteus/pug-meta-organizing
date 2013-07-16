import ConfigParser
import requests
import urllib

def get_settings(_config_cache=[]):
    config = ConfigParser.RawConfigParser()
    config.read(['settings.ini'])
    return config

def meetup_urls(method='groups.json'):
    base_url = 'http://api.meetup.com/'
    url = (base_url + method)
    return (url, {'key': get_settings().get('api_keys', 'meetup')})

def top_python_groups():
    url, data = meetup_urls()
    data['topic']='python'
    data['order'] = 'members'
    data['page'] = '200'
    response = requests.get(url + '?' + urllib.urlencode(data))
    return response
