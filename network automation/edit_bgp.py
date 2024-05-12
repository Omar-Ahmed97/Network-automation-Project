import requests
from load_yaml_data import load_data as load_data
import json


def get_id_bgp(j_file):
  return json.loads(j_file).get("Cisco-IOS-XE-bgp:bgp")[0].get("id")




def delet_bgp():
  id = get_id_bgp(get_bgp())
  hosts = load_data("Configuration_Data/host.yaml")
  hostname = hosts.get("hosts")[0]['hostname']
  url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/router/bgp={id}"

  payload = ""
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }
  response = requests.request("DELETE", url, headers=headers, data=payload,verify=False)

def add_bgp(json_file):
  delet_bgp()
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


def edit_bgp1(json_file):
  id = get_id_bgp(get_bgp())
  hosts = load_data("Configuration_Data/host.yaml")
  hostname = hosts.get("hosts")[0]['hostname']
  url = f'https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/router/bgp={id}'

  payload = json_file
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }

  response = requests.request("PUT", url, headers=headers, data=payload,verify=False)


def get_bgp():

  hosts = load_data("Configuration_Data/host.yaml")
  hostname = hosts.get("hosts")[0]['hostname']
  url = f'https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/router/bgp'

  payload = ""
  headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic b21hcjpvbWFy'
  }

  response = requests.request("GET", url, headers=headers, data=payload,verify=False)
  return response.text

def edit_bgp(json_file):
  if("id" in get_bgp()):
    id_router = get_id_bgp(get_bgp())
    id_yaml = get_id_bgp(json_file)
    if (id_router == id_yaml):
      edit_bgp1(json_file)
      exit()

  add_bgp(json_file)