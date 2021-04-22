import jogador

class Jogadores:
    def __init__(self):
        self.jogadores = []

    def criar_jogador(self,info = (),line=""):
        j = jogador.Jogador()
        # print("jogador_id = {}, jogador nome {}".format(info[0], info[1]))
        # print(len(self.jogadores))
        j.id = info[0]
        j.nome = info[1]
        if(len(self.jogadores) == 0 ):
            self.jogadores.append(j)
        else:
            for i in range(0,len(self.jogadores)):
                if(self.jogadores[i].id == j.id):
                    # print("{} mudou para {}".format(self.jogadores[i].nome,j.nome))
                    self.jogadores[i].nome = j.nome
                    # print(self.jogadores[i].nome)
                    lista = [ (x.id,x.nome) for x in self.jogadores]
                    # print(lista)
                    return
            self.jogadores.append(j)
                                         
    def fim_de_jogo(self):
        
        self.jogadores.clear()
       
        print(self.jogadores)

    def kill_register(self,data=[]):
        if data[0] == "<world>":
            for i in range(0,len(self.jogadores)):
                if(data[1] == self.jogadores[i].nome):
                    self.jogadores[i].kills_count -= 1
        elif data[0] == data[1]:
            #jogador se matou, nao contoma como kill para ele mas conta no total kill
            pass

        else:
            for i in range(0,len(self.jogadores)):
                if(data[0] == self.jogadores[i].nome):
                    self.jogadores[i].kills_count += 1


