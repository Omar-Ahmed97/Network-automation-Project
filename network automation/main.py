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
        choice = int(input("Please choose the number between 1-3 and 0 to quit"))
        if (choice >= 0 and choice <= 3):
            break
    return choice
def load_data(file):
    with open(file) as f:
        data = yaml.full_load(f)
        return data

conf_temp=["Configuration_Template/bgp.j2","Configuration_Template/ospf.j2"]
conf_data=["Configuration_Data/bgp.yaml","Configuration_Data/ospf.yaml"]



import yaml
from jinja2 import Environment,FileSystemLoader


env=Environment(loader=FileSystemLoader("."))




while(True):
    choice = menue()
    if (choice == 0):
        break
    temp=env.get_template(conf_temp[choice-1])
    protocol = load_data(conf_data[choice-1])
    output1 = temp.render(protocol=protocol)
    print(output1)













