# Оконное приложение "Сбалансированные деревья поиска"
## Данное оконное приложение создано как творческое задание по предмету "Алгоритмизация и программирование". 
Для использования программы скопируйте файлы проекта себе на компьютер, откройте файл `main.py` и запустите код. Перед вами откроется начальное пустое окно с тремя доступными кнопками `Add node`, `Generate Tree`, `Clear Tree` и пустое пространство, где будет отрисовываться дерево.

![start window](https://github.com/ivonki/binary_search_tree/blob/main/bst_start.jpg)

## Описание возможностей окна
У вас есть возможность добавить узлы дерева по одному, для этого напишите в строку под кнопкой `Add node` значение узла и нажмине на кнопку добавления. 
Также у вас есть возможность сгенерировать дерево, введя количество узлов для добавления под кнопкой `Genetare Tree`.
_Важно отметить, что при добавлении узлов или генерации дерева в непустое дерево, оно будет обновляться с старыми и новым узлом_
![tree rendering demonstration](https://github.com/ivonki/binary_search_tree/blob/main/bst_usual.jpg)

## Реализация приложения.
Для реализации оконного приложения использовалась библиотека `PyQt5`, также были использованы модули `sys` и `random`. 

## Реализация кода бинарного дерева.
Для реализации сбалансированного бинарного дерева был создан класс `Node`, состоящий из основной информации об узле дерева, а именно: значение узла, информация о его левом и правом потомке, информация о его родителе и фактор баланса. Код представлен ниже.

`class Node:
    def __init__(self, value, left_child=None, right_child=None, parent=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.balance_factor = 0
        `

Для хранения дерева как цельной структуры был создан класс `Tree`. В этом классе реализованы основные методы работы с деревом: добавление дерева методом `add`, отслеживание изменения фактора баланса и его обновление `update_balance`, проверка фактора баланса в методе `balance_tree`, который распределяет в заивимости от характера дисбаланса в другие методы, соответственно `rotate_left` и `rotate_right`, также есть метод печати `print`. Код этих методов для ознакомления ниже.

`class Tree:

    def __init__(self):
        self.root = None

    #рекурсивная фунция для добавления узлов дерева
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)
    
    def _add(self, cur_node, value):
        if value == cur_node.value:
            return

        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value, parent=cur_node)
                self.update_balance(cur_node.left_child)
            else:
                self._add(cur_node.left_child, value)

        else:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value, parent=cur_node)
                self.update_balance(cur_node.right_child)
            else:
                self._add(cur_node.right_child, value)

    #отслеживание дисбаланса, обновление баланса
    def update_balance(self, cur_node):
        if (cur_node.balance_factor == 2) or (cur_node.balance_factor == -2):
            self.balance_tree(cur_node)
            return 
        
        if cur_node.parent is not None:
            if cur_node.parent.left_child is cur_node:
                cur_node.parent.balance_factor += 1
            elif cur_node.parent.right_child is cur_node:
                cur_node.parent.balance_factor -= 1

            if cur_node.parent.balance_factor != 0:
                self.update_balance(cur_node.parent)

    #проверка фактора баланса
    def balance_tree(self, rotation_node):
        if rotation_node.balance_factor == 2:
            self.rotate_right(rotation_node)
        elif rotation_node.balance_factor == -2:
            self.rotate_left(rotation_node)

    def rotate_left(self, rotation_node):
        new_root = rotation_node.right_child
        rotation_node.right_child = new_root.left_child

        if new_root.left_child is not None:
            new_root.left_child.parent = rotation_node
        new_root.parent = rotation_node.parent

        if rotation_node.parent is None:
            self.root = new_root
        else:
            if rotation_node.parent.left_child is rotation_node:
                rotation_node.parent.left_child = new_root
            else:
                rotation_node.parent.right_child = new_root
        new_root.left_child = rotation_node
        rotation_node.parent = new_root
        rotation_node.balance_factor = rotation_node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rotation_node.balance_factor, 0)

    def rotate_right(self, rotation_node):
        new_root = rotation_node.left_child
        rotation_node.left_child = new_root.right_child

        if new_root.right_child is not None:
            new_root.right_child.parent = rotation_node
        new_root.parent = rotation_node.parent

        if rotation_node.parent is None:
            self.root = new_root
        else:
            if rotation_node.parent.left_child is rotation_node:
                rotation_node.parent.left_child = new_root
            else:
                rotation_node.parent.right_child = new_root
        new_root.right_child = rotation_node
        rotation_node.parent = new_root
        rotation_node.balance_factor = rotation_node.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(rotation_node.balance_factor, 0) 

    #вывод алгоритмом обхода в глубину
    def print(self):
        if self.root is None:
            return "empty tree"
        else:
            self._print(self.root)

    def _print(self, cur_node):
        if cur_node is not None:
            print("val ",cur_node.value, "bal", cur_node.balance_factor)
            self._print(cur_node.left_child)
            print("r")
            self._print(cur_node.right_child)
            `
## Заключение.
Мною было написана программа для отрисовки сбалансированных бинарных деревьев поиска. Теперь я осознаю фразу "В работе первые 90% проекта делаются за 10% времени, оставшиеся 10% — за 90%", надеюсь, что больше от нее не пострадаю.
