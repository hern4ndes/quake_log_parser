import os
import re
import parser
import jogadores
#
matou_morreu_causa = r":\s([^:]+)\skilled\s(.*?)\sby\s(.*)"

jogador_info = r"ClientUserinfoChanged: \d n\\(.*?)\\"

local_path  = os.path.dirname(os.path.abspath(__file__))
game_count = 0 
total_kills = 0
jogadores_game = []

total_kills = 0


lista_de_jogadores  = jogadores.Jogadores()

with open("quake.log") as log_file:
    log_file = log_file.readlines()

players = []

for line_index, line in enumerate(log_file):
    if(parser.init_game(line)):
        print("game = {}".format(game_count))
        if(game_count > 0):
            players = []
            print("\ttotal_kills: {}".format(total_kills))
            print("\tplayers: {}".format([(x.nome, x.kills_count) for x in lista_de_jogadores.jogadores]))
            lista_de_jogadores.jogadores = []
            
        game_count += 1
        total_kills = 0           
   
    else:
        player = parser.jogador_info(line)
        if(player):
            lista_de_jogadores.criar_jogador(player)
        else:
           kill_data = parser.kill_line(line)
           if(kill_data):
               lista_de_jogadores.kill_register(kill_data)
               total_kills += 1

               



    






    
   
  

       
       
    
   
    # matches = re.search(matou_morreu_causa, line)
    # if matches:
    #     total_kills += 1
    #     # print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
    #     # print("matou")
    #     for groupNum in range(0, len(matches.groups())-1):
    #         groupNum = groupNum + 1
    #         if matches.group(groupNum) not in jogadores_game and  matches.group(groupNum)  != '<world>':
    #             jogadores_game.append(matches.group(groupNum))
            
        
                

    
    