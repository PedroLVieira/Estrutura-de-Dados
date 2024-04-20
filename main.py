class Pessoa():
    def __init__(self):
        self.atividades = []

    def adicionar_atividade(self, titulo, conteudo):
        bloco = {titulo: conteudo}
        self.atividades.append(bloco)
        
    def remover_atividade(self, titulo):
        for i in self.atividades:
            for chave in i.keys():
                if chave == titulo:
                    self.atividades.remove(i)
                    print(self.atividades)
                

p1 = Pessoa()
p1.adicionar_atividade("test","testando")
p1.remover_atividade("test")