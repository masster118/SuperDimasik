class Node:
    """
    Класс узла дерева.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    """
    Класс для реализации двоичного дерева поиска.
    """
    def __init__(self):
        self.root = None
    def insert(self, key):
        """
        Вставка ключа в дерево.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    def _insert(self, current, key):
        """
        Вспомогательная рекурсивная функция для вставки.
        """
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)
    def search(self, key):
        """
        Поиск ключа в дереве.
        Возвращает True, если ключ найден, иначе False.
        """
        return self._search(self.root, key)
    def _search(self, current, key):
        """
        Вспомогательная рекурсивная функция для поиска.
        """
        if current is None:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)
    def inorder(self):
        """
        Обход дерева в порядке возрастания (in-order).
        """
        result = []
        self._inorder(self.root, result)
        return result
    def _inorder(self, current, result):
        """
        Вспомогательная рекурсивная функция для обхода.
        """
        if current:
            self._inorder(current.left, result)
            result.append(current.key)
            self._inorder(current.right, result)
    def delete(self, key):
        """
        Удаление ключа из дерева.
        """
        self.root = self._delete(self.root, key)
    def _delete(self, current, key):
        """
        Вспомогательная рекурсивная функция для удаления.
        """
        if current is None:
            return current
        # Поиск ключа
        if key < current.key:
            current.left = self._delete(current.left, key)
        elif key > current.key:
            current.right = self._delete(current.right, key)
        else:
            # Узел с одним ребёнком или без детей
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Узел с двумя детьми: находим минимальный в правом поддереве
            temp = self._min_value_node(current.right)
            current.key = temp.key
            # Удаляем минимальный узел в правом поддереве
            current.right = self._delete(current.right, temp.key)
        return current
    def _min_value_node(self, node):
        """
        Поиск узла с минимальным значением в дереве.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
# Пример использования
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
print("Обход дерева (in-order):", bst.inorder())
print("Поиск 40:", bst.search(40))
print("Поиск 25:", bst.search(25))
bst.delete(50)
print("Обход после удаления 50:", bst.inorder())
