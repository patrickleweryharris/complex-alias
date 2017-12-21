#!/usr/bin/python

from sys import argv
import os


def make_script(name, command, eva):
    num_args = command.count('%')

    # Building the script file
    script_text = '#!/bin/bash \n'
    script_text += 'function execute(){\n   '
    script_text += command.replace('%', '$')

    # If you want to keep the result of this function i.e. in a cd command
    if eva is True:
        script_text += '\n   exec '
        script_text += os.environ['SHELL'] + '\n'

    script_text += '\n}\n'
    script_text += '\nexecute'
    arg_string = ' '
    i = 1
    while i < num_args + 1:
        arg_string += '$' + str(i) + ' '
        i += 1
    script_text += arg_string
    alias_dir = os.environ['HOME'] + '/.complex-alias/' + name
    script_file = open(alias_dir, 'w')
    script_file.write(script_text)
    script_file.close()


if __name__ == '__main__':
    if len(argv) < 3:
        print("Usage complex-alias <script name> <command> <flag>")
    eva = False
    if len(argv) == 4 and argv[3] == 'eva':
        eva = True
    make_script(argv[1], argv[2], eva)
