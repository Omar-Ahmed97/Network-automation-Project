import json


def str_to_json(file):
    print(file)
    json_file = json.dumps(json.loads(file))
    print(type(json_file))
    return json_file

