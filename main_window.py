from b_tree import Tree
import sys
import random
from PyQt5.QtWidgets import QApplication, \
                            QWidget, QPushButton, QHBoxLayout, \
                            QVBoxLayout, QGridLayout, \
                            QLabel, QLineEdit, QCheckBox, QMainWindow, \
                            QSpinBox, QInputDialog, QGraphicsScene, \
                            QGraphicsView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QBrush, QPen, QColor, QIntValidator


def F(x):
    return 250/((x+1)**(3/2))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.tree = Tree()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Binary Search Tree") #????
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(800,500)
        #self.setStyleSheet("background-imagine: url(background.jpg);")
        validator = QIntValidator(0,99, self)

        layout_upper = QGridLayout()
        layout_down = QGridLayout()

        self.btn_add = QPushButton("Add Node", self)
        self.btn_add.setToolTip("Add there value")
        self.btn_add.clicked.connect(self.add_node)
        self.text_add = QLineEdit()
        self.text_add.setValidator(validator)
        
        self.btn_generator = QPushButton("Generate Tree", self)
        self.btn_generator.setToolTip("Add there number of nodes")
        self.btn_generator.clicked.connect(self.generate_tree)
        self.text_generate = QLineEdit()
        self.text_generate.setValidator(validator)

        self.btn_clear_tree = QPushButton("Clear Tree", self)
        self.btn_clear_tree.setToolTip("Click here to remove tree")
        self.btn_clear_tree.clicked.connect(self.clear_tree)
        
        #self.btn_balance_tree = QPushButton("Balance tree", self)
        #self.btn_balance_tree.clicked.connect(self.balance_tree)
        
        layout_upper.addWidget(self.btn_add, 0, 0)
        layout_upper.addWidget(self.btn_generator, 0, 1)
        layout_upper.addWidget(self.btn_clear_tree, 0, 2, 2, 2)
        layout_upper.addWidget(self.text_add, 1, 0)
        layout_upper.addWidget(self.text_generate, 1, 1)
        #layout_upper.addWidget(self.btn_balance_tree, 1, 2)
        
        layout = QVBoxLayout(self)
        layout.addLayout(layout_upper)
        layout.addLayout(layout_down)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene) 
        layout.addWidget(self.view)

    #добавление узла дерева в дерево, связь с кнопкой "add"
    def add_node(self):
        value = int(self.text_add.text())
        print(value)
        self.text_add.setText("")

        self.tree.add(value)
        self.print_tree()

    #создание дерева-рисунка обходом в глубину
    def print_tree(self):
        self.scene.clear()

        x_0, y_0 = 100, 200
        
        if self.tree.root is None:
            return "empty"
        else:
            point = {
                "x": x_0,
                "y": y_0
            }
            level = 0

            return self._print_tree(self.tree.root, point, level)
        
    def _print_tree(self, node, point_from, level):
        self.print_node(node, point_from)
        
        if node.left_child:
            point_to = {
                "x": point_from["x"] - F(level),
                "y": point_from["y"] + 50
            }

            self.print_line(point_from, point_to)
            self._print_tree(node.left_child, point_to, level+1)
        
        if node.right_child:
            point_to = {
                "x": point_from["x"] + F(level),
                "y": point_from["y"] + 50
            }

            self.print_line(point_from, point_to)
            self._print_tree(node.right_child, point_to, level+1)

    #создание линий между узлами
    def print_line(self, p1, p2):
        self.scene.addLine(p1["x"]+25, p1["y"], p2["x"]+25, p2["y"] )

    #отдельный узел-рисунок
    def print_node(self, node, p):
        width = 50
        height = 50

        green_brush = QBrush(QColor(144,238,144))
        black_pen = QPen(Qt.black)
        black_pen.setWidth(3)

        ellipse = self.scene.addEllipse(p["x"], p["y"], width, height, black_pen, green_brush)
        text_item = self.scene.addText(str(node.value))
        text_item.setPos(p["x"]+12, p["y"]+12)

    #связь с кнопкой "Generate Tree"
    def generate_tree(self):
        value = int(self.text_generate.text())
        print(value)
        self.text_generate.setText("")

        for i in range(value):
            self.tree.add(random.randint(1,100))
        self.print_tree()

    #связь с кнопкой "Clear Tree"    
    def clear_tree(self):
        self.scene.clear()
        self.tree = None
        self.tree = Tree()
        
    # def balance_tree(self):
    #     self.tree.balance_tree(self.tree.root)
    #     self.scene.clear()
    #     self.print_tree()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())