from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QHBoxLayout
from main import *

class TaskWidget(QWidget):
    def __init__(self, task):
        super().__init__()
        
        self.layout = QVBoxLayout(self)
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame_layout = QVBoxLayout(self.frame)
        self.label = QLabel(task.get('Disciplina'))  
        self.label1 = QLabel(task.get('Descrição'))
        self.button = QPushButton('Mark as Completed')
        self.frame_layout.addWidget(self.label)
        self.frame_layout.addWidget(self.label1)
        self.frame_layout.addWidget(self.button)
        self.layout.addWidget(self.frame)


class MainWindow(QWidget):
    def __init__(self, tasks):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.stacked_widgets = [QStackedWidget(self) for _ in range(3)]
        for i, stacked_widget in enumerate(self.stacked_widgets):
            self.layout.addWidget(stacked_widget)
            for j in range(i, len(tasks), 3):
                stacked_widget.addWidget(TaskWidget(tasks[j]))

        self.button_layout = QVBoxLayout()
        self.prev_button = QPushButton('Previous')
        self.prev_button.clicked.connect(self.prev_task)
        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.next_task)
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
        self.layout.addLayout(self.button_layout)

    def prev_task(self):
        for stacked_widget in self.stacked_widgets:
            current_index = stacked_widget.currentIndex()
            if current_index > 0:
                stacked_widget.setCurrentIndex(current_index - 1)

    def next_task(self):
        for stacked_widget in self.stacked_widgets:
            current_index = stacked_widget.currentIndex()
            if current_index < stacked_widget.count() - 1:
                stacked_widget.setCurrentIndex(current_index + 1)

if __name__ == '__main__':
    app = QApplication([])
    atividades_faculdade = ListaDeTarefas()
    atividade_1 = {"Disciplina":"Estrutura de Dados","Descrição": "Criar um projeto sobre estruturas encadeadas"}
    atividade_2 = {"Disciplina":"Redes", "Descrição": "Criar projeto no packet tracer"}
    atividade_3 = {"Disciplina":"Extensão" , "Descrição": "enviar resumo para o professor"}
    atividade_4 = {"Disciplina":"Extensão" , "Descrição": "enviar resumo para o professor"}
    atividades_faculdade.append(atividade_1, 1)
    atividades_faculdade.append(atividade_2, 2 )
    atividades_faculdade.append(atividade_3, 3 )
    atividades_faculdade.append(atividade_4, 1 )
    tasks = []
    for item in atividades_faculdade:
        tasks.append(item)
    
    current_node = atividades_faculdade.head
    while current_node is not None:
        tasks.append(current_node.valor) 
        current_node = current_node.proximo 
    window = MainWindow(tasks)
    window.show()
    app.exec_()