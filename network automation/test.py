import requests
import json

url = "https://192.168.75.128/restconf/data/Cisco-IOS-XE-native:native/ip/route/ip-route-interface-forwarding-list[prefix=\"3.3.3.3\"][mask=\"255.255.255.255\"]"

payload = json.dumps({
  "Cisco-IOS-XE-native:ip-route-interface-forwarding-list": [
    {
      "prefix": "3.3.3.3",
      "mask": "255.255.255.255",
      "fwd-list": [
        {
          "fwd": "192.168.1.5"
        },
        {
          "fwd": "GigabitEthernet2"
        }
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic b21hcjpvbWFy'
}

response = requests.request("DELETE", url, headers=headers, data=payload,verify=False)

print(response.text)
