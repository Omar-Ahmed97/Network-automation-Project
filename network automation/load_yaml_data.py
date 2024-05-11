
import yaml
def load_data(file):
    with open(file) as f:
        data = yaml.full_load(f)
        return data