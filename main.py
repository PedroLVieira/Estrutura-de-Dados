from nodes import Nodes

class TaskManagement():
    def __init__(self):
        self.listas = []

    def AdicionarListaTarefas(self, lista_tarefas):
        self.listas.append(lista_tarefas)

    def RemoverListaTarefas(self, lista_tarefas):
        self.listas.remove(lista_tarefas)



class ListaDeTarefas():
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elemento):
        if self.head:
            pointer = self.head
            while(pointer.proximo):
                pointer = pointer.proximo
            pointer.proximo = Nodes(elemento)
        else:
            self.head = Nodes(elemento)
        self._size+=1
    def __len__(self):
        return self._size

    def _getNode(self, index):
        pointer = self.head
        for index in range(index):
            if pointer:
                pointer = pointer.proximo
            else:
                raise IndexError("A tarefa que está sendo acessada não existe nesta lista de tarefas.")
        return pointer

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.valor
        else:
            raise IndexError("a tarefa a qual está tentando se referir não se encontra na lista de tarefas.")

    def __setitem__(self, index, elemento):
        pointer = self._getNode(index)
        if pointer:
            pointer.valor = elemento
        else:
            raise IndexError("a tarefa a qual está tentando se referir não se encontra na lista de tarefas.")

    def index(self, elemento):
        pointer = self.head
        indice = 0
        while(pointer):
            if pointer.valor == elemento:
                return indice
            pointer = pointer.proximo
            indice +=1
        raise ValueError(f"{elemento} não está na lista")

    def insert(self, index, elemento):
        new_Node = Nodes(elemento)
        if index == 0:
            new_Node.proximo = self.head
            self.head = new_Node
        else:
            pointer = self._getNode(index - 1)
            new_Node.proximo = pointer.proximo
            pointer.proximo = new_Node
        self._size += 1

    def remove(self, elemento):
        if self.head == None:
            raise ValueError(f"{elemento} não está na lista (lista vazia)")
        elif self.head.valor == elemento:
            self.head = self.head.proximo
            self._size -= 1
            return elemento
        else:
            antecessor = self.head
            pointer = self.head.proximo
            while(pointer):
                if pointer.valor == elemento:
                    antecessor.proximo = pointer.proximo
                    pointer.proximo = None
                antecessor = pointer
                pointer = pointer.proximo
            self._size -= 1
            return elemento


    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r += str(pointer.valor) + "->"
            pointer = pointer.proximo
        return r
    def __str__(self):
        return self.__repr__()



lista_teste = ListaDeTarefas()
lista_teste.append(5)
lista_teste.append(6)
lista_teste.append(10)
lista_teste.append(7)
print(lista_teste.remove(10))
print(lista_teste)



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

                

p1 = Pessoa()
p1.adicionar_atividade("test","testando")
p1.remover_atividade("test")