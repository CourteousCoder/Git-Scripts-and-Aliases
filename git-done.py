#!/usr/bin/python3

import subprocess

# This script allows you to interactively add portions of your changes to
# a comit, commits the changes with an interactive message prompt, and
# repeats until there are no more changes. Then it pushes the branch.

def run(command):
    return subprocess.run(command.split(' '))

def has_changes():
    status = subprocess.run("git status --porcelain".split(' '),stdout=subprocess.PIPE)
    if status.stdout:
        return True
    else:
        return False

def git_commit():
    commit = run('git commit')
    if commit.returncode is 1:
        exit(1)

# Main Script

while has_changes():
    run('git add -p .')
    git_commit()

exit(run('git push').returncode)
