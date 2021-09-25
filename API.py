import requests
import json


def startAPI(url, problem_id):
    x_auth_token = '35e4f0394f7fff6d61cf2cabc8dfe7ea'
    url = url + '/start'
    headers = {
            'X-Auth-Token': x_auth_token,
            'Content-Type': 'application/json'
    }
    params = {'problem': problem_id}
    resp = requests.post(url=url, headers = headers, params=params)
    resp = resp.json()
    return resp['auth_key']

def waitinglineAPI(url, auth_key):
    url = url + '/waiting_line'
    headers = {
            'Authorization': auth_key,
            'Content-Type': 'application/json'
    }
    resp = requests.get(url=url, headers = headers)
    resp = resp.json()
    return resp['waiting_line']

def gameresultAPI(url, auth_key):
    url = url + '/game_result'
    headers = {
            'Authorization': auth_key,
            'Content-Type': 'application/json'
    }
    resp = requests.get(url=url, headers = headers)
    resp = resp.json()
    return resp['game_result']

def userinfoAPI(url, auth_key):
    url = url + '/user_info'
    headers = {
            'Authorization': auth_key,
            'Content-Type': 'application/json'
    }
    resp = requests.get(url=url, headers = headers)
    resp = resp.json()
    return resp['user_info']

def matchAPI(url, auth_key, params):
    url = url + '/match'
    headers = {
            'Authorization': auth_key,
            'Content-Type': 'application/json'
    }
    params = {'pairs': params}
    resp = requests.put(url=url, headers = headers, data = json.dumps(params))
    resp = resp.json()
    return resp

def changegradeAPI(url, auth_key, params):
    url = url + '/change_grade'
    headers = {
            'Authorization': auth_key,
            'Content-Type': 'application/json'
    }
    params = {'commands': params}
    resp = requests.put(url=url, headers = headers, data = json.dumps(params))
    resp = resp.json()

    return resp

def scoreAPI(url, auth_key):
    url = url + '/score'
    headers = {
            'Authorization': auth_key,
            'Content-Type': 'application/json'
    }
    resp = requests.get(url=url, headers = headers)
    resp = resp.json()
    return resp

if __name__=='__main__':
    url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
    problem_id = 1
    auth_key = startAPI(url, problem_id)
    a = waitinglineAPI(url, auth_key)
    print(a)
    a = gameresultAPI(url, auth_key)
    print(a)
    a = userinfoAPI(url, auth_key)
    print(a)
