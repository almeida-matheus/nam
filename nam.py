import os
import sys
import json


class colors:
    white = '\033[97m\033[1m'
    green = '\033[92m'
    blue = '\033[34m'
    red_grey = '\033[0;31;40m'
    end = '\033[m'

currentDir = os.path.dirname(os.path.realpath(__file__))
dirCommands = os.path.join(currentDir, './commands')
dirCommands = os.path.abspath(os.path.realpath(dirCommands))
listCommands = os.path.join(currentDir, './settings/commands.json')
listCommands = os.path.abspath(os.path.realpath(listCommands))

def HelpProgram():
    print('\n')
    print('NAM'.center(60))
    print('-' * 60)
    print('| how to use: nam command'.ljust(58), '|')
    print('-' * 60)
    print('| -h, --help '.ljust(14), '| display this help text '.ljust(43), '|')
    print('| -l, --list '.ljust(14), '| show all commands of nam '.ljust(43), '|')
    print('| -a, --att '.ljust(14), '| update to add new commands '.ljust(43), '|')
    print('-' * 60)
    print('version: 0.01\n'.rjust(60))
    # print(f'\033[32 aaaa \033[m')
    # print(f'{colors.blue}erro: serviço não cadastrado{colors.end}')

def ListCommands():
    # * read json file to show commands avaible
    try:
        with open(listCommands, 'r') as fileJson:
            listJson = json.load(fileJson)
            print("\ncommands:")
            for command in listJson["commands"]:
                print(command)
    except (OSError, FileNotFoundError):
        print('cannot open commands.json')

def AttCommands():
    # * read name of archives inside of the command directory
    commands = [f for f in os.listdir(
        dirCommands) if os.path.isfile(os.path.join(dirCommands, f))]
    # ? python list => ['apt-get.md', 'django.md', 'tar.md', 'unzip.md']

    # * create new json with commands
    obj = ({
        'commands': commands,
    })

    with open(listCommands, 'w', encoding='utf8') as jsonFile:
        json.dump(obj, jsonFile, indent=4, ensure_ascii=False,
                  sort_keys=True, separators=(',', ':'))

def VerifyCommandExist(command):
    # * read json file to check if command exist
    try:
        mdcommand = command + ".md"
        fileJson = open(listCommands, 'r')
        arrayJson = json.load(fileJson)
        if mdcommand not in arrayJson["commands"]:
            print('command not found, maybe try with man or --help')
            sys.exit()
        ReadCommand(mdcommand)
    except (OSError, FileNotFoundError):
        print('cannot open: ', fileJson)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("something went wrong\n", e)
    finally:
        fileJson.close()

def ReadCommand(mdcommand):
    # * read command.md file
    try:
        localmdcommand = "./commands/" + mdcommand
        pathCommand = os.path.join(currentDir, localmdcommand)
        pathCommand = os.path.abspath(os.path.realpath(pathCommand))

        fileCommand = open(pathCommand, 'r', encoding='utf-8')
        print('-' * 60)
        for line in fileCommand:
            FormatPrint(line)
        print('-' * 60)
    except (OSError, FileNotFoundError):
        print('cannot open: ', fileCommand)
    finally:
        fileCommand.close()

def FormatPrint(line):
    #* retira \n desnecessários
    line = line.replace('\n', 'ä').strip('ä')
    #* titulo: retira o # e coloca em maiusculo
    if ('#' in line):
        line = line.replace('#', ' ').strip().upper()
        return print(f'{colors.white}{line}{colors.end}')
        # return print(f'\n{line}')
    #* comentários: retira \n entre eles e o >
    if (line[0:2] == '>>'):
        return
    line = line.replace('>', ' ').strip(' ')
    #* descrição:
    if (line[-1::] == ':'): #pega ultima posição da string
        return print(f'{colors.green}{line}{colors.end}', end="")
        # return print(line, end="")
    #* linha de código: retira `
    if (line[:1] == '`'): #pega a primeira posição da string
        line = line.replace('`', '  ')
        # print(line, end="")
        #* tag da linha de código: retira `
        #* arquivo
        if ('{{' or '}}' in line):
            line = line.replace('{{', '').replace('}}', '')
        return print(f'{colors.red_grey}{line}{colors.end}')
    if ('`' in line):
        line = line.replace('`', '')
    print(line)

if __name__ == "__main__":
    param = sys.argv[1:]  # list with the first param

    if param != []:
        if type(param[0]) is not str:
            raise ValueError("only string are allowed")
        param = str(param[0].lower().strip())

    if param == "--help" or param == []:
        HelpProgram()
    elif param == "--att" or param == "-a":
        AttCommands()
    elif param == "--list" or param == "-l":
        ListCommands()
    else:
        VerifyCommandExist(param)
