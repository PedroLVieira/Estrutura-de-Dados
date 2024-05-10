from nodes import Nodes

class ListaDeTarefas():
    def __init__(self):
        self.head = None
        self._size = 0
        self.priority_map = {}


    # CRIANDO O DICIONARIO CONTENDO O TITULO DA TAREFA E CONTEUDO DA TAREFA
    '''def criar_dicio(self, titulo, conteudo):
        bloco = {titulo: conteudo}
        return bloco'''
    


    # ADICIONANDO AS TAREFAS, COM A SUA PRIORIDADE
    def append(self, elemento, prioridade):
        if prioridade not in self.priority_map:
            self.priority_map[prioridade] = []
        if self.head:
            pointer = self.head
            while(pointer.proximo):
                pointer = pointer.proximo
            pointer.proximo = Nodes(elemento)
        else:
            self.head = Nodes(elemento)
        self.priority_map[prioridade].append(elemento)
        self._size+=1


    # FUNÇÃO QUE RETORNARÁ O TAMANHO DA LISTA DE TAREFAS
    def __len__(self):
        return self._size

    # FUNÇÃO PARA RODAR PELOS NODES DA LISTA, A FIM DE ACHAR O NODE INDICADOR PELO INDEX
    def _getNode(self, index):
        pointer = self.head
        for index in range(index):
            if pointer:
                pointer = pointer.proximo
            else:
                raise IndexError("A tarefa que está sendo acessada não existe nesta lista de tarefas.")
        return pointer


    # FUNÇÃO PARA RETORNAR DIRETAMENTE UMA TAREFA

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.valor
        else:
            raise IndexError("a tarefa a qual está tentando se referir não se encontra na lista de tarefas.")

    # FUNÇÃO PARA ALTERAR DIRETAMENTE UMA TAREFA

    def __setitem__(self, index, elemento):
        pointer = self._getNode(index)
        if pointer:
            pointer.valor = elemento
        else:
            raise IndexError("a tarefa a qual está tentando se referir não se encontra na lista de tarefas.")


    # FUNÇÃO PARA RETORNAR O INDEX DE UMA TAREFA, A PARTIR DA TARERFA
    def index(self, elemento):
        pointer = self.head
        indice = 0
        while(pointer):
            if pointer.valor == elemento:
                return indice
            pointer = pointer.proximo
            indice +=1
        raise ValueError(f"{elemento} não está na lista")

    # FUNÇÃO PARA INSERIR UMA TAREFA EM UM ÍNDICE ALEATÓRIO
    def insert(self, index, elemento, prioridade):
        new_Node = Nodes(elemento)
        if index == 0:
            new_Node.proximo = self.head
            self.head = new_Node
        else:
            pointer = self._getNode(index - 1)
            new_Node.proximo = pointer.proximo
            pointer.proximo = new_Node
        self.priority_map[prioridade].append(elemento)
        self._size += 1


    # REMOVENDO TAREFAS DA LISTA DE TAREFAS
    def remove(self, elemento):
        if self.head == None:
            raise ValueError(f"{elemento} não está na lista (lista vazia)")
        elif self.head.valor == elemento:
            self.head = self.head.proximo
            self._size -= 1
            for priority in self.priority_map:
                if elemento in self.priority_map[priority]:
                    self.priority_map[priority].remove(elemento)
            return elemento
        else:
            antecessor = self.head
            pointer = self.head.proximo
            while(pointer):
                if pointer.valor == elemento:
                    antecessor.proximo = pointer.proximo
                    pointer.proximo = None
                    self._size -= 1
                    for priority in self.priority_map:
                        if elemento in self.priority_map[priority]:
                            self.priority_map[priority].remove(elemento)
                    return elemento
                antecessor = pointer
                pointer = pointer.proximo
            raise ValueError(f"{elemento} não está na lista")

    # REMOVENDO TAREFAS DA LISTA DE TAREFAS, COM BASE NA LISTA DE PRIORIDADES NA QUAL ELE IRÁ REMOVER DO MENOR PARA O MAIOR NÚMERO
    def removerTarefaPrioritaria(self):
        for priority in sorted(self.priority_map.keys(), reverse=False): 
            if self.priority_map.get(priority):
                task = self.priority_map[priority].pop(0)
                pointer = self.head
                antecessor = None
                while pointer:
                    if pointer.valor == task:
                        if antecessor:
                            antecessor.proximo = pointer.proximo
                        else:
                            self.head = pointer.proximo
                        pointer.proximo = None
                        self._size -= 1
                        return task
                    antecessor = pointer
                    pointer = pointer.proximo
        return None

    # ADICIONANDO TAREFAS À LISTA DE CONCLUÍDOS (
    ''' 
        ESSA FUNÇÃO APENAS SERÁ UTILIZADA QUANDO UMA LISTA DE TAREFAS CONCLUÍDAS FOR CRIADA.
    '''
    def append_concluido(self, elemento):
        if self.head:
            pointer = self.head
            while(pointer.proximo):
                pointer = pointer.proximo
            pointer.proximo = Nodes(elemento)
        else:
            self.head = Nodes(elemento)

    # FUNÇÕES COMBINADAS PARA RETORNAR UM ELEMENTO NA FORMA DE STRING, DE FÁCIL VISUALIZAÇÃO, COM APONTADORES
    # A IMPRESSÃO DA LISTA SE DARÁ NA ORDEM EM QUE OS ELEMENTOS FORAM INSERIDOS, NÃO COM BASE EM SUAS PRIORIDADES
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r += str(pointer.valor) + "->"
            pointer = pointer.proximo
        return r

    def __str__(self):
        return self.__repr__()



# criando objtos do tipo lista de tarefas (cada lista possuirá objetivos e temas diferentes)

atividades_faculdade = ListaDeTarefas()
projetos_sociais = ListaDeTarefas()
metas_vida = ListaDeTarefas()

# ADICIONANDO ELEMENTOS EM CADA LISTA DE TAREFAS, COM SUA DESCRIÇÃO E SEU TÍTULO
atividade_1 = {"Estrutura de Dados" : "Criar um projeto sobre estruturas encadeadas"}
atividade_2 = {"Redes" : "Criar projeto no packet tracer"}
atividade_3 = {"Extensão" : "enviar resumo para o professor"}
atividades_faculdade.append(atividade_1, 1)
atividades_faculdade.append(atividade_2, 2 )
atividades_faculdade.append(atividade_3, 3 )

# MOSTRANDO A MINHA LISTA DE TAREFAS

for item in atividades_faculdade:
    print(item)
print()
print("-=" * 30)
print()
# REMOVENDO ELEMENTOS DA LISTA DE TAREFAS SEM SUA PRIORIDADE, EM SEGUIDA, MOSTRANDO O ESTADO ATUAL DA LISTA

atividades_faculdade.remove(atividade_1)
for item in atividades_faculdade:
    print(item)

print()
print("-=" * 30)
print()

# REMOVENDO ELEMENTOS DA LISTA DE TAREFAS COM SUA PRIORIDADE, EM SEGUIDA, MOSTRANDO O ESTADO ATUAL DA LISTA

atividades_faculdade.removerTarefaPrioritaria()



print()
print("-=" * 30)
print()
for item in atividades_faculdade:
    print(item)


# atvFaculdade_concluidas = ListaDeTarefas()
# atvFaculdade_concluidas.append_concluido(atividades_faculdade.removerTarefaPrioritaria())
# for item in atvFaculdade_concluidas:
#     print(item)

# for item in atividades_faculdade:
#     print(item)




    # lista_teste = ListaDeTarefas()
    # concluidos = ListaDeTarefas()
    # lista_teste.append(lista_teste.criar_dicio("test","testando"), 3)
    # lista_teste.append(lista_teste.criar_dicio("test2","testando2"), 1)
    # lista_teste.append(lista_teste.criar_dicio("test3","testando3"), 2)
    # concluidos.append_concluido(lista_teste.removerTarefaPrioritaria())
    # concluidos.append_concluido(lista_teste.removerTarefaPrioritaria())
    # print(lista_teste)
    # print(concluidos)
    
    # Exemplo de uso para remover a tarefa mais prioritária
    
    # while True:
    #     tarefa = lista_teste.removerTarefaPrioritaria()
    #     if tarefa:
    #         print("Tarefa removida:", tarefa)
    #     else:
    #         break 
            

