


from load_yaml_data import load_data as load_data
import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hosts = load_data("Configuration_Data/host.yaml")
print(hosts.get("hosts")[0])


def invoke_shell():
    ssh.connect(**(hosts.get("hosts")[0]))
    return ssh.invoke_shell()

