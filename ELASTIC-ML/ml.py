import requests
import json
from elasticsearch import Elasticsearch
import datetime,pytz
import time
ELK = Elasticsearch("http://your_url_of_elastic(route address):80")
CPU_USAGE_CORE={}

CLUSTER_TOKEN = dict({"cls_name1": "token",
                      "cls_name2": "token",
                      "cls_name3": "token"})
CLUSTER_LIST = "cls_name1", "cls_name2", "cls_name3"


def GET_CPU():
    EXIST = 0
    ENV = "PROD"
    for CLUSTER in CLUSTER_LIST:
        URL = "https://prometheus-k8s-openshift-monitoring.apps." + CLUSTER + "your_base_Domain"
        headers = {
            'Authorization': f'Bearer ' + CLUSTER_TOKEN[CLUSTER]
        }
        RESPONSE = requests.get(URL + '/api/v1/query', headers=headers, verify=False,
                                params={'query': 'sum(rate(container_cpu_usage_seconds_total{container!=""}[5m]))'})
        CONTENT = RESPONSE.content
        JSON_OBJECT = json.loads(CONTENT)
        CPU_CORE = JSON_OBJECT['data']['result'][0]['value'][1]
        #print(CPU_CORE)
        CPU_USAGE_CORE[CLUSTER] = CPU_CORE

    return CPU_USAGE_CORE


def ELK_INFO():
    client = ELK
    resp = client.info()
    print("ELK VERSION:", client.info()["version"]["number"], "\n")


def CREATE_INDEX():
    EXIST = 0
    try:
        INDEX_NAME = "prod"
        if ELK.indices.exists(index=INDEX_NAME):
            EXIST = 1
            print("INDEX IS EXIST----> " + INDEX_NAME)
        else:
            EXIST = 0
            ELK.indices.create(index=INDEX_NAME)
        if ELK.indices.exists(index=INDEX_NAME) and EXIST == 0:
            print("I HAVE BEEN CREATED INDEX----> " + INDEX_NAME)
    except Exception as e:
        print(e)

def CREATE_JSON():
    CPU=GET_CPU()
    INDEX_NAME = "prod"
    for VALUE in CLUSTER_LIST:
        try:
            DATA = {}
            DATA['kind'] = "CPU"
            DATA['name'] = VALUE
            DATA['cpu'] = CPU[VALUE]
            JSON = json.dumps(DATA)
            PUSH_DATA(JSON, INDEX_NAME)
        #print(JSON)
        except Exception as e:
            print(e)
        #print(JSON)


def PUSH_DATA(JSON,INDEX_NAME):
    try:
        JSONDOC = {"data": json.loads(JSON),"timestamp": datetime.datetime.now(pytz.timezone('Europe/Istanbul')).isoformat()}
        ELK.index(index=INDEX_NAME, doc_type='_doc', body=JSONDOC)
        print("finished upload: " + INDEX_NAME)
    except Exception as e:
        print(e)



ELK_INFO()
while True:
    CREATE_JSON()
    time.sleep(1)

#CREATE_INDEX()
#CREATE_JSON()
