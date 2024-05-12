import requests
from load_yaml_data import load_data as load_data
import json

def get_prefix_static(j_file):
  return [ x.get("prefix") for x in json.loads(j_file).get("Cisco-IOS-XE-native:ip-route-interface-forwarding-list")]
def get_mask_static(j_file):
  return [x.get("mask") for x in json.loads(j_file).get("Cisco-IOS-XE-native:ip-route-interface-forwarding-list")]

def get_static_route():
    hosts = load_data("Configuration_Data/host.yaml")
    hostname = hosts.get("hosts")[0]['hostname']
    url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/ip/route/ip-route-interface-forwarding-list/"
    payload = ""
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json',
        'Authorization': 'Basic b21hcjpvbWFy'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return(response.text)

def delet_static_route(prefix,mask):

    hosts = load_data("Configuration_Data/host.yaml")
    hostname = hosts.get("hosts")[0]['hostname']
    url = f"https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/ip/route/ip-route-interface-forwarding-list={prefix},{mask}"

    payload = ""
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json',
        'Authorization': 'Basic b21hcjpvbWFy'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)


def add_static_route(json_file):
    if( "prefix" in get_static_route() ):
        prefix = get_prefix_static(get_static_route())
        mask = get_mask_static(get_static_route())
        prefix_json = json.loads(json_file).get("Cisco-IOS-XE-native:ip-route-interface-forwarding-list").get("prefix")
        mask_json = json.loads(json_file).get("Cisco-IOS-XE-native:ip-route-interface-forwarding-list").get("prefix")
        if( prefix_json[0] in prefix  and mask_json[0] in  mask  ):
            hosts = load_data("Configuration_Data/host.yaml")
            hostname = hosts.get("hosts")[0]['hostname']
            url = f'https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/ip/route/ip-route-interface-forwarding-list={prefix_json[0]},{mask_json[0]}'

            payload = json_file
            headers = {
                'Accept': 'application/yang-data+json',
                'Content-Type': 'application/yang-data+json',
                'Authorization': 'Basic b21hcjpvbWFy'
            }
            response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
            print(response.text)
            exit()


    #delet_static_route(prefix, mask)
    hosts = load_data("Configuration_Data/host.yaml")
    hostname = hosts.get("hosts")[0]['hostname']
    url = f'https://{hostname}/restconf/data/Cisco-IOS-XE-native:native/ip/route/'

    payload = json_file
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
     'Authorization': 'Basic b21hcjpvbWFy'
        }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text)




