import os
import sys
import json
# from os import listdir
# from os.path import isfile, join
# se nao tiver no nam ira usar o --help

currentDir = os.path.dirname(os.path.realpath(__file__))
dirCommands = os.path.join(currentDir, '../commands')
dirCommands = os.path.abspath(os.path.realpath(dirCommands))
listCommands = os.path.join(currentDir, '../settings/commands.json')
listCommands = os.path.abspath(os.path.realpath(listCommands))


def HelpProgram():
    # passar --att como parametro invoca uma funcao q atualiza o json
    print('\n')
    print('NAM'.center(60))
    print('-' * 60)
    print('| how to use: nam command'.ljust(58), '|')
    print('-' * 60)
    print('| -h, --help '.ljust(15), '| display this help text '.ljust(42), '|')
    print('| -l, --list '.ljust(15), '| show all commands of nam '.ljust(42), '|')
    print('| -a, --att '.ljust(15), '| update to add new commands '.ljust(42), '|')
    print('-' * 60)
    print('version: 0.01\n'.rjust(60))

def AttCommands():
    # passar --att como parametro invoca uma funcao q atualiza o json
    # * read name of archives inside of the paste
    commands = [f for f in os.listdir(dirCommands) if os.path.isfile(os.path.join(dirCommands, f))]
    print(commands)

    listJson = []
    # commands = 'honda'

    listJson.append({
        'commands': commands,
    })

    with open('commands.json', 'w', encoding='utf8') as json_file:
        json.dump(listJson, json_file, indent=4, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def ListCommands():
    # passar --list mostra os comandos
    # * read json file
    try:
        with open(listCommands,'r') as fileJson:
            listJson = json.load(fileJson)
            for command in listJson.Commands:
                print("comandos:\n", command)
    except OSError:
        print('cannot open')

    # try:
    #     fileJson = open(listCommands, 'r')
    # finally:
    #     fileJson.close()

def VerifyCommandExist(param):
    # * read json file
    try:
        fileJson = open(listCommands, 'r')
        arrayJson = json.load(fileJson)
        if param not in arrayJson:
            return False
    except OSError:
        print('cannot open: ', fileJson)
    except Exception as e:
        print("Something went wrong", e)
    finally:
        fileJson.close()


def ReadCommand(param):
    # * read command.md file
    try:
        mdcommand = param + ".md"
        fileCommand = open(mdcommand, 'r')
        arrayJson = json.load(fileCommand)
        if param not in arrayJson:
            return False
    except OSError:
        print('cannot open: ', fileCommand)
    finally:
        fileCommand.close()

if __name__ == "__main__":
    param = sys.argv[1:]  # select only params
    if param != []:
        param = str(param[0].lower().strip())
    if param == "--help" or param == []:
        HelpProgram()
    elif param == "--att":
        AttCommands()
    elif param == "--list":
        ListCommands()
    elif param != type(str):
        raise ValueError("Only string are allowed")
    else:
        VerifyCommandExist(param)
        ReadCommand(param)
        #PrintCommand(param)

# if not type(arg) is str:
#   raise TypeError("Only string are allowed")

# def main():
#     try:
#         mdcommand = open("demofile.md")
#         for line in mdcommand:
#             print("teste")
#         mdcommand.write("Lorum Ipsum")
#     except OSError:
#         print('cannot open: ', mdcommand)
#     except ValueError as e:
#          print("Only string are allowed")
#     except Exception as e:
#         print("Something went wrong", e)
#     else:
#         print("caso não ocorra esse erro")
#     finally:
#         print("The 'try except' is finished")
#         mdcommand.close()
