#!/usr/bin/env python

import yaml
import string
import random


def ask_question(question, config, key):
    current = ''
    if key in config:
        current = config[key]

    question = question + ' [' + current + ']: '
    try:
        response = raw_input(question)
    except NameError:
        # Python 3
        response = input(question)
    if response == '':
        return
    config[key] = response


def random_password():
    chars = string.letters
    chars = chars + '0123456789'
    password = ''
    for i in range(0, 16):
        password = password + random.choice(chars)
    return password

with open("provisioning/user_vars.yml", 'r') as stream:
    config = yaml.load(stream)
    stream.close()

ask_question('What is your github username?', config, 'gh_user')

if 'mysql_password' not in config:
    print('Generating random MySQL password')
    config['mysql_password'] = random_password()

print('MySQL dw password is ' + config['mysql_password'])

if 'system_password' not in config:
    print('Generating random system password')
    config['system_password'] = random_password()

print('System password is ' + config['system_password'])


with open("provisioning/user_vars.yml", 'w') as f:
    f.write(yaml.dump(config, default_flow_style=False))
