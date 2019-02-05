class SparseMatrixNode:
    def __init__(self, position, value, right=None, bottom=None):
        self.position = position
        self.value = value
        self.right = right
        self.bottom = bottom


class SparseMatrix:
    def __init__(self, rows_count=0, columns_count=0, elements_list=[]):
        self.columns_count, self.rows_count = columns_count, rows_count
        self.columns, self.rows = [None] * columns_count, [None] * rows_count

        for x in elements_list:
            node = SparseMatrixNode(x[0], x[1])
            self.__insert(node)

    def __repr__(self):
        view_list = [["0"] * self.columns_count for i in range(self.rows_count)]
        for i in range(self.rows_count):
            node = self.rows[i]
            while node is not None:
                view_list[node.position[0]][node.position[1]] = str(node.value)
                node = node.right

        view = str()
        for x in view_list:
            for y in x:
                view += y + " "
            view += "\n"

        return view

    def __insert(self, node):
        self.__insert_in_row(node)
        self.__insert_in_column(node)

    def __insert_in_row(self, node):
        curr_node = self.rows[node.position[0]]

        if curr_node is None:
            self.rows[node.position[0]] = node
            return

        if node.position[0] < curr_node.position[0]:
            self.rows[node.position[0]] = node
            node.right = curr_node
            return

        while curr_node.right is not None:
            if node.position[0] < curr_node.right:
                node.right = curr_node.right
                curr_node.right = node
                return
            curr_node = curr_node.right

        curr_node.right = node
        node.right = None

    def __insert_in_column(self, node):
        curr_node = self.columns[node.position[1]]

        if curr_node is None:
            self.columns[node.position[1]] = node
            return

        if node.position[1] < curr_node.position[1]:
            self.columns[node.position[1]] = node
            node.bottom = curr_node
            return

        while curr_node.bottom is not None:
            if node.position[0] < curr_node.bottom:
                node.bottom = curr_node.bottom
                curr_node.bottom = node
                return
            curr_node = curr_node.bottom

        curr_node.bottom = node
        node.bottom = None

    def get_non_zeros(self):
        non_zeros = list()
        for i in range(self.rows_count):
            node = self.rows[i]
            while node is not None:
                non_zeros.append((node.position, node.value))
                node = node.right
        return non_zeros

    # def __init__(self, matrix):
    #    pass


elems = [((0, 0), -2), ((3, 3), 11), ((2, 3), 23)]
mt = SparseMatrix(10, 10, elems)
print(mt.get_non_zeros())
