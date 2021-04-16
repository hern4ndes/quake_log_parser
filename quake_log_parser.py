import os
import re
#
matou_morreu_causa = r":\s([^:]+)\skilled\s(.*?)\sby\s(.*)"
comeco_jogo = r"InitGame"
fim_jogo = r"--------+"

local_path  = os.path.dirname(os.path.abspath(__file__))

with open("quake.log") as log_file:
    log_file = log_file.readlines()

game_count = 0 

for i, line in enumerate(log_file,start=1):
    matches = re.search(comeco_jogo, line)
    if matches:
        game_count += 1
        print("partida = {}".format(game_count))
   
    matches = re.search(matou_morreu_causa, line)
    if matches:
        print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
        
        for groupNum in range(0, len(matches.groups())):
            groupNum = groupNum + 1
            
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))
        
                

