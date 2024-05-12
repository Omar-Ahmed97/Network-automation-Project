import edit_bgp as bgp
import edit_ospf as ospf
from add_ststic_route import add_static_route
from ssh_invoke_shell import invoke_shell as invoke_shell
import time
from str_to_json import str_to_json as str_to_json
from load_yaml_data import load_data as load_data
from render_jinjaFile import render as render
import json
import urllib3
urllib3.disable_warnings()

network_object= {'protocol':0,'connection_method':0}

def menue():
    print("*" * 10)
    print("Welcome to Router configuration: ")
    print("*" * 10)

    print("Protocols :\n\
            1- bgp\n\
            2- ospf\n\
            3- static route \n")
    choice = 0
    while (True):
        choice = int(input("Please choose the number between 1-3 and 0 to quit :: "))
        if (choice >= 0 and choice <= 3):
            break
    return choice


conf_temp=["Configuration_Template/bgp.j2","Configuration_Template/ospf.j2","Configuration_Template/static_route.j2"]
conf_data=["Configuration_Data/bgp.yaml","Configuration_Data/ospf.yaml","Configuration_Data/static_route.yaml"]


while(True):
    choice = menue()
    if (choice == 0):
        break
    connection_method = int(input("how do you want to connect to your device using 1-ssh  2-restAPI :: "))
    protocol = load_data(conf_data[choice-1])
    print(protocol)
    network_object['connection_method'] = connection_method
    network_object['protocol']= protocol
    output1 = render(conf_temp[choice-1] , network_object=network_object)
    print(output1.strip())
    with open( "o.t",'w') as f:
        f.write(output1.strip())
    if(connection_method == 1):
        cli = invoke_shell()
        cli.send('en \n')
        cli.send('show ip interface brief \n')
        cli.send("conf ter \n")
        cli.send("\n")
        print(output1.strip())
        time.sleep(6)
        cli.send(output1.strip())
        cli.send("\n")
        print(output1.strip())
        time.sleep(6)
        output = cli.recv(999999).decode()
        cli.close()
        print(output)
    else:
        j_file = str_to_json(output1.strip())
        print(j_file)

        if ( choice  == 1) :

            bgp.edit_bgp(j_file)
            print(bgp.get_bgp())
        elif(choice  == 2):
            ospf.edit_ospf(j_file)
            print(ospf.get_ospf())
        else :
            add_static_route(j_file)















