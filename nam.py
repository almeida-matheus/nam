#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

class colors:
    white = '\033[1;97m'
    grey = '\033[1;37m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    darkblue = '\033[94m'
    purple = '\033[1;94m'
    pink = '\033[35m'
    blue = '\033[96m'
    red_dark = '\033[0;91;40m'
    green_dark = '\033[0;92;40m'
    green_grey = '\033[0;92;100m'
    end = '\033[0m'

pathCurrentDir = os.path.dirname(os.path.realpath(__file__))
pathCommandsDir = os.path.abspath(os.path.realpath(
    os.path.join(pathCurrentDir, './commands/')))

def HelpScript():
    print('\n','nam'.center(70))
    print(' '+'—' * 68 + ' ')
    print('│ how to use: nam command'.ljust(68), '│')
    print('│ example: nam zip'.ljust(68), '│')
    print(' '+'—' * 68 + ' ')
    print('│ -h, --help '.ljust(14), '│ display this help text '.ljust(53), '│')
    print('│ -l, --list '.ljust(14), '│ show all commands of nam '.ljust(53), '│')
    print('│ -s, --show '.ljust(14), '│ show all markdown commands in vscode '.ljust(53), '│')
    print(' '+'—' * 68 + ' ')
    print('1.1.0\n'.rjust(70))

def ShowMarkdown():
    os.system(f'coded {pathCommandsDir}')
    print(f'{colors.yellow}edit:\n{pathCommandsDir}{colors.end}')
    print(f'{colors.yellow}obs: you must have vscode installed and variable environment "code" enabled{colors.end}')

def ScanCommands():
    try:
        commands = [f[:-3] for f in os.listdir(
            pathCommandsDir) if os.path.isfile(os.path.join(pathCommandsDir, f))]
        # print(f'{colors.white}all commands:{colors.end}')
        for command in commands:
            print(command)
    except (OSError, FileNotFoundError):
        print(f'{colors.red}cannot open commands.json{colors.end}')
    except Exception as e:
        print(f'{colors.red}something went wrong:\n{e} {colors.end}\n')

def VerifyCommandExist(command):
    try:
        commands = [f[:-3] for f in os.listdir(
            pathCommandsDir) if os.path.isfile(os.path.join(pathCommandsDir, f))]
        if command not in commands:
            print(f'{colors.red}command not found, maybe try with man or --help{colors.end}')
            sys.exit()
        return command
    except (OSError, FileNotFoundError):
        print('cannot open: ', pathCommandsDir)
    except Exception as e:
        print('something went wrong:\n',e)

def ReadCommand(command):
    try:
        pathCommandFile = os.path.join(pathCommandsDir, command + '.md')
        pathCommandFile = os.path.abspath(os.path.realpath(pathCommandFile))
        file_command = open(pathCommandFile, 'r', encoding='utf-8')
        lines=file_command.readlines()
        lines=[line.strip() for line in lines]
        return lines
    except (OSError, FileNotFoundError):
        print('cannot open: ', pathCommandFile)
    except Exception as e:
        print('something went wrong:\n',e)
    finally:
        file_command.close()

def PrintLine(line):
    #? tipo - titulo {#}
    if (line[:1] == '#'):
        line = line.replace('#', ' ').strip().upper()
        return print(f'{colors.white}{line}{colors.end}')
    #? tipo - comentário sobre o comando {>}
    if (line[:1] == '>'):
        if (line[0:2] == '>>'):
            return
        line = line.replace('>', ' ').strip(' ')
        return print(f'{colors.white}{line}{colors.end}')
    #? tipo - descrição do código {:}
    if (line[-1::] == ':'): #* ultima posição da string
        return print(f'{colors.white}{line}{colors.end}', end='')
    #? tipo - linha de código {``}
    if (line[:1] == '`'):
        line = line.replace('`', '')
        if ('[' or ']' in line):
            line = line.replace('[', f'{colors.blue}').replace(']', f'{colors.end}{colors.green}')
        # if ('<' or '>' in line):
        #     line = line.replace('[', f'{colors.purple}').replace(']', f'{colors.end}{colors.green}')
        return print(f'  {colors.green}{line}{colors.end}')
    print(line)
    
if __name__ == '__main__':
    param = sys.argv[1:] 
    if param != []:
        param = str(param[0].lower().strip())
    if param == '--help' or param == '-h' or param == []:
        HelpScript()
    elif param == '--list' or param == '-l':
        ScanCommands()
    elif param == '--show' or param == '-s':
        ShowMarkdown()
    else:
        command = VerifyCommandExist(param)
        lines = ReadCommand(command)
        print('-' * 70)
        for line in lines:
            PrintLine(line)
        print('-' * 70)