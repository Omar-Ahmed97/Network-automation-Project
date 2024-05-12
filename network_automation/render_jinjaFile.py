from jinja2 import Environment,FileSystemLoader
import time

env=Environment(loader=FileSystemLoader("."))



def render(file , network_object):
    temp = env.get_template(file)
    output = temp.render(network_object=network_object)
    return output