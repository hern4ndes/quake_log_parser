import re 

def init_game(line = ""):
    init_game_regex = r"InitGame"
    if  re.search(init_game_regex, line):
        return True
    
def end_game(line = ""):
    end_game_regex = r"--------+"
    if  re.search(end_game_regex, line):
        return True

def jogador_info(line = ""):
    jogador_info =  r"ClientUserinfoChanged: (\d) n\\(.*?)\\"
    matches = re.search(jogador_info, line)
    if matches:
        return(matches.group(1),matches.group(2))

def kill_line(line = ""):
    matou_morreu_causa = r":\s([^:]+)\skilled\s(.*?)\sby\s(.*)"
    matches = re.search(matou_morreu_causa, line)
    if matches:
        return(matches.group(1),matches.group(2),matches.group(3))
    
