import sys
import numpy as np

def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def check_usage(arg):
    if arg == "-h" or arg == "--help":
        print("USAGE\n\t./303make")
        sys.exit(0)

def isCommand(variable): 
    return variable[:2] == "cc"

def isRecipe(variable): 
    return variable != "" and variable [:2] != "cc"

def parseFile(path):
    try:
        content = open(path, 'r').read().split("\n")
    except:
        sys.exit(84)
    if content[0] == "":
        sys.exit(84)
    command = []
    recipe = []
    for s in filter(isCommand, content):
        command.append(s)
    for s in filter(isRecipe, content):
        recipe.append(s)
    return (command, recipe)

def parse(args):
    if len(args) == 1:
        check_usage(args[0])
    if len(args) < 1 or len(args) > 2:
        print("Invalid number of arguments. Try ./303make -h for usage")
        sys.exit(84)
    recipe, command = parseFile(args[0])
    if len(args) == 1:
        return recipe, command, ""
    else:
        return recipe, command, args[1]