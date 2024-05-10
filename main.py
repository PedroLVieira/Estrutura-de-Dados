from nodes import Nodes

class ListaDeTarefas():
    def __init__(self):
        self.head = None
        self._size = 0
        self.priority_map = {}

    def criar_dicio(self, titulo, conteudo):
        bloco = {titulo: conteudo}
        return bloco
    
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

    def removerTarefaPrioritaria(self):
        for priority in range(1, 5):  # Verifica da maior para a menor prioridade
            if self.priority_map.get(priority):
                task = self.priority_map[priority].pop(0)
                return task
        return None

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
lista_teste.append(lista_teste.criar_dicio("test","testando"), 3)
lista_teste.append(lista_teste.criar_dicio("test2","testando2"), 1)
lista_teste.append(lista_teste.criar_dicio("test3","testando3"), 2)

print(lista_teste)

# Exemplo de uso para remover a tarefa mais prioritária
while True:
    tarefa = lista_teste.removerTarefaPrioritaria()
    if tarefa:
        print("Tarefa removida:", tarefa)
    else:
        break
