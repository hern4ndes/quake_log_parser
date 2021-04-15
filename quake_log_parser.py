import os
import re
#
matou_morreu_causa = r":\s([^:]+)\skilled\s(.*?)\sby\s(.*)"
comeco_jogo = r" InitGame:"
fim_jogo = r"--------+"

local_path  = os.path.dirname(os.path.abspath(__file__))

with open("quake.log") as log_file:
    log_file = log_file.read()
    
matches = re.finditer(matou_morreu_causa, log_file)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    print(match.groups())
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
