import requests
from load_yaml_data import load_data as load_data
import json


def get_id_ospf(j_file):
  return json.loads(j_file).get("Cisco-IOS-XE-ospf:ospf")[0].get("id")




def delet_ospf():
  id = get_id_ospf(get_ospf())

  url = f"https://192.168.75.128/restconf/data/Cisco-IOS-XE-native:native/router/ospf={id}"

  payload = ""
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }
  response = requests.request("DELETE", url, headers=headers, data=payload,verify=False)

def add_ospf(json_file):
  delet_ospf()
  hosts = load_data("Configuration_Data/host.yaml")
  hostname = hosts.get("hosts")[0]['hostname']
  url = f'https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/router/'

  payload = json_file
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }

  response = requests.request("POST", url, headers=headers, data=payload,verify=False)


def edit_ospf(json_file):
  id = get_id_ospf(get_ospf())
  hosts = load_data("Configuration_Data/host.yaml")
  hostname = hosts.get("hosts")[0]['hostname']
  url = f'https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/router/ospf={id}'

  payload = json_file
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }

  response = requests.request("PUT", url, headers=headers, data=payload,verify=False)



def get_ospf():

  url = "https://192.168.75.128/restconf/data/Cisco-IOS-XE-native:native/router/ospf"

  payload = ""
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }

  response = requests.request("GET", url, headers=headers, data=payload,verify=False)
  return response.text
