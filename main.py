import os
from string import Template
import textfile
from os import walk
from template import robocup_template
import re

def parsing_robocup(robocup_template,main_team,opponent_team):
    """Funcion que parsea el html y retorna los datos del usuario nuevo"""
    s = Template(robocup_template).safe_substitute(main_team=main_team,opponent_team=opponent_team)

    return s


final_file=parsing_robocup(robocup_template.robocup_template,'BasicTeam','BasicTeam')


textfile.write("SoccerBots/teams/robocup.dsc",final_file)


#LEER ARCHIVOS DIRECTORIO

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
        for j in range(i+1,len(lista)):
            lista2.append([lista[i],lista[j]])
    return lista2

#lista de versus de la lista, donde no se repitan los versus
def versus(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            lista2.append([lista[i],lista[j]])
    return lista2

#lista de versus de la lista, donde no se repitan los versus
def versus2(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            lista2.append([lista[i],lista[j]])
    return lista2


x=combina(f)

v=versus(x)

v2=versus2(f)


#java -jar LabABM.jar robocup.dsc > /Users/gabrielborges/Desktop/servco_abm/logs/log.txt
#for recorrer in range(0,3):
#    os.system(f'java -jar /Users/gabrielborges/Desktop/servco_abm/SoccerBots/teams/LabABM.jar /Users/gabrielborges/Desktop/servco_abm/SoccerBots/teams/robocup.dsc > /Users/gabrielborges/Desktop/servco_abm/logs/log{recorrer}.txt')


def use_regex(input_text):
    pattern = re.compile(r"TeamBots 2\.0e \(c\)2000 Tucker Balch, CMU and GTRC 1771 maxtimestep statement read, treated as timestep 1 0 2 0 3 0 3 1 3 2 4 2 4 3 4 4 5 4 5 5 6 5 6 6 6 7 7 7 8 7 8 8 9 8 9 9 10 9 10 10 11 10 12 10 (13( 10)+) 13 11 13 12  trial number	: -1 \(counts down\)  sim time    	: 600000 milliseconds  timestep 		: 50 milliseconds  timeout      	: 600000 milliseconds  frames/second	: 21430\.35714285714  free memory	: 121622736  total memory	: 136314880  os\.name	: Mac OS X  os\.version	: 12\.6  os\.arch	: aarch64  java\.version	: 18\.0\.1\.1", re.IGNORECASE)
    return pattern.findall(input_text)[0][0].split(" ")










