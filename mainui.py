from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QHBoxLayout
from main import *
import mysql.connector
import json
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QComboBox

# ...

def adicionar_banco(json_data):
    cursor.execute("UPDATE tarefas set tarefas = %s where idtarefas = 1;", (json_data,))
    conn.commit()
def retirar_banco():
    cursor.execute("SELECT tarefas FROM tarefas WHERE idtarefas = 1;")
    for linha in cursor.fetchall():
        return linha[0]
    conn.commit()
class TaskWidget(QWidget):
    complete_task_signal = pyqtSignal(dict)

    def __init__(self, task):
        super().__init__()
        self.task = task
        
        self.layout = QVBoxLayout(self)
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setStyleSheet("background-color: #f5f5f5; border-radius: 10px; padding: 10px;")
        self.frame_layout = QVBoxLayout(self.frame)
        
        self.label = QLabel(task.get('Disciplina'))
        self.label.setStyleSheet("font-weight: bold; font-size: 16px; color: #333;")
        
        self.label1 = QLabel(task.get('Descrição'))
        self.label1.setStyleSheet("font-size: 14px; color: #666;")
        
        self.label2 = QLabel(f"Prioridade: {task.get('prioridade')}")
        self.label2.setStyleSheet("font-size: 12px; color: #999;")
        
        self.button = QPushButton('Completa')
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF; 
                color: white; 
                border-radius: 5px; 
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.button.clicked.connect(self.complete_task)
        
        self.frame_layout.addWidget(self.label2)
        self.frame_layout.addWidget(self.label)
        self.frame_layout.addWidget(self.label1)
        self.frame_layout.addWidget(self.button)
        self.layout.addWidget(self.frame)

    def complete_task(self):
        self.complete_task_signal.emit(self.task)

class AddTaskWindow(QDialog):
    task_added_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Adicionar Tarefa')
        self.setGeometry(150, 150, 400, 300)
        
        self.layout = QFormLayout(self)

        self.priority_combo = QComboBox()
        self.priority_combo.addItems(['1', '2', '3'])
        self.layout.addRow('Prioridade:', self.priority_combo)
        
        self.discipline_input = QLineEdit()
        self.layout.addRow('Disciplina:', self.discipline_input)
        
        self.description_input = QLineEdit()
        self.layout.addRow('Descrição:', self.description_input)
        
        self.add_button = QPushButton('Adicionar')
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745; 
                color: white; 
                border-radius: 5px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.add_button.clicked.connect(self.add_task)
        self.layout.addRow(self.add_button)
    
    def add_task(self):
        task = {
            'prioridade': self.priority_combo.currentText(),
            'Disciplina': self.discipline_input.text(),
            'Descrição': self.description_input.text()
        }
        self.task_added_signal.emit(task)
        tasks2.sort(key=lambda x: int(x.get('prioridade', 0)))
        self.close()

class MainWindow(QWidget):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks
        
        self.setWindowTitle("Gerenciador de Tarefas")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        self.layout = QHBoxLayout(self)
        self.stacked_widgets = [QStackedWidget(self) for _ in range(3)]
        for i, stacked_widget in enumerate(self.stacked_widgets):
            self.layout.addWidget(stacked_widget)
            for j in range(i, len(tasks), 3):
                task_widget = TaskWidget(tasks[j])
                task_widget.complete_task_signal.connect(self.remove_task)
                stacked_widget.addWidget(task_widget)

        self.button_layout = QVBoxLayout()
        
        self.add_task_button = QPushButton('Adicionar Tarefa')
        self.add_task_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8; 
                color: white; 
                border-radius: 5px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        self.add_task_button.clicked.connect(self.show_add_task_window)
        self.button_layout.addWidget(self.add_task_button)
        
        self.prev_button = QPushButton('Voltar')
        self.prev_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745; 
                color: white; 
                border-radius: 5px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.prev_button.clicked.connect(self.prev_task)
        
        self.next_button = QPushButton('Passar')
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #ffc107; 
                color: white; 
                border-radius: 5px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
        """)
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
        

    @pyqtSlot(dict)
    def remove_task(self, task):
        self.tasks.remove(task)
        
        # Atualizar o banco de dados
        json_data = json.dumps(self.tasks)
        adicionar_banco(json_data)
        
        # Atualizar a interface
        self.update_interface()

    @pyqtSlot(dict)
    def add_task(self, task):
        self.tasks.append(task)
        
        # Ordenar as tarefas por prioridade
        self.tasks.sort(key=lambda x: int(x.get('prioridade', 0)))
        
        # Atualizar o banco de dados
        json_data = json.dumps(self.tasks)
        adicionar_banco(json_data)
        
        # Atualizar a interface
        self.update_interface()
    
    def update_interface(self):
        for stacked_widget in self.stacked_widgets:
            while stacked_widget.count() > 0:
                widget = stacked_widget.widget(0)
                stacked_widget.removeWidget(widget)
                widget.deleteLater()
        
        for i, stacked_widget in enumerate(self.stacked_widgets):
            for j in range(i, len(self.tasks), 3):
                task_widget = TaskWidget(self.tasks[j])
                task_widget.complete_task_signal.connect(self.remove_task)
                stacked_widget.addWidget(task_widget)

    def show_add_task_window(self):
        self.add_task_window = AddTaskWindow()
        self.add_task_window.task_added_signal.connect(self.add_task)
        self.add_task_window.exec_()
config = {
    'user': 'root',
    'password': 'pedro12510',
    'host': '127.0.0.1',
    'port':'3306',
    'database': 'agenda'
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

if __name__ == '__main__':
    tasks = []
    arquivo = retirar_banco()
    tasks = json.loads(arquivo)
    tasks2 = []
    for item in tasks:
        tasks2.append(item)


    
    app = QApplication([])
    atividades_faculdade = ListaDeTarefas()
    # atividade_1 = {"Disciplina":"Estrutura de Dados","Descrição": "Criar um projeto sobre estruturas encadeadas","prioridade": "1"}
    # atividade_2 = {"Disciplina":"Redes", "Descrição": "Criar projeto no packet tracer","prioridade": "2"}
    # atividade_3 = {"Disciplina":"Extensão" , "Descrição": "enviar resumo para o professor","prioridade": "3"}
    # atividade_4 = {"Disciplina":"artes" , "Descrição": "enviar pintura para o professor","prioridade": "1"}
    # atividades_faculdade.append(atividade_1, 1)
    # atividades_faculdade.append(atividade_2, 2 )
    # atividades_faculdade.append(atividade_3, 3 )
    # atividades_faculdade.append(atividade_4, 1 )

    for item in atividades_faculdade:
        tasks2.append(item)
    tasks2.sort(key=lambda x: int(x.get('prioridade', 0)))

    print(tasks2)
    json_data = json.dumps(tasks2)
    adicionar_banco(json_data)
    window = MainWindow(tasks2)
    window.show()
    app.exec_()
