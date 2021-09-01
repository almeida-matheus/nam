#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

class colors:
    white = '\033[1;97m'
    red = '\033[0;91m'
    green = '\033[38;5;77m'
    yellow = '\033[38;5;227'
    purple = '\033[38;5;147m'
    blue = '\033[38;5;81m'
    end = '\033[0m'

COMMANDS_DIR = os.path.abspath(os.path.realpath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), './commands/')))

def HelpScript():
    print('')
    print('NAM'.center(70))
    print(' '+'—' * 68 + ' ')
    print('│ command line tool to view simpler command help pages'.ljust(68), '│')
    print('│ with a focus on practical examples'.ljust(68), '│')
    print(' '+'—' * 68 + ' ')
    print('│ how to use: nam command'.ljust(68), '│')
    print(' '+'—' * 68 + ' ')
    print('│ -h, --help '.ljust(14), '│ display this help text '.ljust(53), '│')
    print('│ -l, --list '.ljust(14), '│ show all available commands '.ljust(53), '│')
    print('│ -s, --show '.ljust(14), '│ show all markdown commands in vscode '.ljust(53), '│')
    print(' '+'—' * 68 + ' ')
    print('1.1.0\n'.rjust(70))

def ShowMarkdown():
    os.system(f'code {COMMANDS_DIR}')
    print(f'{colors.yellow}edit: {COMMANDS_DIR}{colors.end}')
    print(f'{colors.yellow}obs: you must have vscode installed and variable environment "code" enabled{colors.end}')

def ScanCommands():
    try:
        commands = [f[:-3] for f in os.listdir(
            COMMANDS_DIR) if os.path.isfile(os.path.join(COMMANDS_DIR, f))]
        print(f'{colors.yellow}all commands:{colors.end}')
        for command in commands:
            print(command)
    except (OSError, FileNotFoundError):
        print(f'{colors.red}cannot open commands.json{colors.end}')
    except Exception as e:
        print(f'{colors.red}something went wrong:\n{e} {colors.end}\n')

def VerifyCommandExist(command):
    try:
        commands = [f[:-3] for f in os.listdir(
            COMMANDS_DIR) if os.path.isfile(os.path.join(COMMANDS_DIR, f))]
        if command not in commands:
            print(f'{colors.red}command not found, maybe try with man or --help{colors.end}')
            exit()
        return command
    except (OSError, FileNotFoundError):
        print('cannot open: ', COMMANDS_DIR)
    except Exception as e:
        print('something went wrong:\n', e)

def ReadCommand(command):
    try:
        path_command_file = os.path.join(COMMANDS_DIR, command + '.md')
        file_command = open(path_command_file, 'r', encoding='utf-8')
        lines = file_command.readlines()
        lines = [line.strip() for line in lines]
        return lines
    except (OSError, FileNotFoundError):
        print('cannot open: ', path_command_file)
    except Exception as e:
        print('something went wrong:\n', e)
    finally:
        file_command.close()

def PrintLine(line):
    #? type - title {#}
    if (line[:1] == '#'):
        line = line.replace('#', ' ').strip().upper()
        return print(f'{colors.white}{line}{colors.end}')
    #? type - comentary about command {>}
    if (line[:1] == '>'):
        if (line[0:2] == '>>'): return
        line = line.replace('>', ' ').strip(' ')
        return print(f'{colors.white}{line}{colors.end}')
    #? type - code description {:}
    if (line[-1::] == ':'): 
        return print(f'{colors.white}{line}{colors.end}', end='')
    #? type - line of code {``}
    if (line[:1] == '`'):
        line = line.replace('`', '')
        if ('[' or ']' in line):
            line = line.replace('[', f'{colors.blue}').replace(
                ']', f'{colors.end}{colors.green}')
        if ('{' or '}' in line):
            line = line.replace('{', f'{colors.purple}').replace(
                '}', f'{colors.end}{colors.green}')
        return print(f'  {colors.green}{line}{colors.end}')
    print(line)

if __name__ == '__main__':
    arg = sys.argv[1:]
    if arg != []:
        arg = str(arg[0].lower().strip())
    if arg == '--help' or arg == '-h' or arg == []:
        HelpScript()
    elif arg == '--list' or arg == '-l':
        ScanCommands()
    elif arg == '--show' or arg == '-s':
        ShowMarkdown()
    else:
        command = VerifyCommandExist(arg)
        lines = ReadCommand(command)
        print('-' * 70)
        for line in lines:
            PrintLine(line)
        print('-' * 70)