import os
import shlex
import subprocess
import time
from string import Template
import textfile
from os import walk
from template import robocup_template
import re
from helpers import localutils


def parsing_robocup(robocup_template, main_team, opponent_team):
    """Funcion que parsea el html y retorna los datos del usuario nuevo"""
    s = Template(robocup_template).safe_substitute(main_team=main_team, opponent_team=opponent_team)

    return s



# LEER ARCHIVOS DIRECTORIO

f = []
for (dirpath, dirnames, filenames) in walk('SoccerBots/teams'):
    f.extend(filenames)
    break

f = [x for x in f if x.endswith('.java')]
f = [x[:-5] for x in f]


# combinaotria de versus de la lista, donde no se repitan los versus
def combina(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            lista2.append([lista[i], lista[j]])
    return lista2


# lista de versus de la lista, donde no se repitan los versus
def versus(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            lista2.append([lista[i], lista[j]])
    return lista2


# lista de versus de la lista, donde no se repitan los versus
def versus2(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            lista2.append([lista[i], lista[j]])
    return lista2


x = combina(f)

v = versus(x)

v2 = versus2(f)

def extract_score():
    try:
        texto = localutils.read_file("logs/log.txt")
        texto = re.findall(r'(.*)trial number', texto, re.DOTALL)
        texto = texto[0]
        texto = texto.splitlines()
        texto = texto[-2].split(" ")
        texto = [int(i) for i in texto]
        return texto
    except:
        #extract last 26 0 separate numbers
        texto = localutils.read_file("logs/log.txt")
        texto = texto.splitlines()
        texto = texto[-26:]
        texto = [int(i) for i in texto]
        return texto

def extract_score_final():
    def extract_number_column(text):
        pattern = re.compile(r'^\d+')
        return [line for line in text.splitlines() if pattern.match(line)]

    texto = localutils.read_file("logs/log.txt")
    pattern = re.compile(r'^\d+\s\d+')
    x = extract_number_column(texto)
    x = [line for line in x if pattern.match(line)]
    if len(x)<2:
        return [0,0]
    else:
        x = x[-1]
        # split and convert in int
        x = [int(i) for i in x.split(" ")]
        return x





def timeout_play(counter):
    command_line = 'java -jar /Users/gabrielborges/Desktop/servco_abm/SoccerBots/teams/LabABM.jar /Users/gabrielborges/Desktop/servco_abm/SoccerBots/teams/robocup.dsc'
    #execute command with timeout but dont stop loop
    try:

        log=subprocess.run(shlex.split(command_line), timeout=10,capture_output=True)
        log=log.stdout.decode("utf-8")
        with open(f'/Users/gabrielborges/Desktop/servco_abm/logs/log{counter}.txt', 'w') as f:
            f.write(log)

        with open('/Users/gabrielborges/Desktop/servco_abm/logs/log.txt', 'w') as f:
            f.write(log)

        return True
    except subprocess.TimeoutExpired:
        print("Timeout")
        return False





for partido in range(0, len(v2)-1):
    final_file = parsing_robocup(robocup_template.robocup_template, v2[partido][0], v2[partido][1])
    print(f'Juegan {v2[partido][0]} vs {v2[partido][1]}')
    textfile.write("SoccerBots/teams/robocup.dsc", final_file)
    #os.system(f'java -jar /Users/gabrielborges/Desktop/servco_abm/SoccerBots/teams/LabABM.jar /Users/gabrielborges/Desktop/servco_abm/SoccerBots/teams/robocup.dsc > /Users/gabrielborges/Desktop/servco_abm/logs/log.txt')
    if timeout_play(partido):
        score = extract_score_final()
        print(f'partido numero: {partido}')
        print(f'score: {score[0]}-{score[1]}')

    else:
        print('no se pudo jugar el partido, se salta')
        continue









