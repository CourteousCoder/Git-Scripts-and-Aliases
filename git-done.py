#!/usr/bin/python3

import subprocess

# This script allows you to interactively add portions of your changes to
# a comit, commits the changes with an interactive message prompt, and
# repeats until there are no more changes. Then it pushes the branch.

def run(command):
    return subprocess.run(command.split(' '))

def git_status():
    status = subprocess.run("git status --porcelain".split(' '),stdout=subprocess.PIPE)
    if status.stdout:
        return status.stdout.decode('utf-8')
    else:
        return ''

# Main Script

status = git_status()
while status:
    run('git add -p .')
    run('git commit')

