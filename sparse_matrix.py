# Need: errors handling, refactor, increase scalability of D/S,
# check in insertion if element exists, add tests

class SparseMatrixNode:
    def __init__(self, position, value, right=None, bottom=None):
        self.position = position
        self.value = value
        self.right = right
        self.bottom = bottom


class SparseMatrix:
    def __init__(self, rows_count=0, columns_count=0, elements=[], matrix=[]):
        self.columns_count = columns_count
        self.rows_count = rows_count
        self.columns = [None] * self.columns_count
        self.rows = [None] * self.rows_count
        
        if (len(matrix) > 0):
            self.rows_count = len(matrix)
            self.columns_count = len(matrix[0]) if self.rows_count > 0 else 0

            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] != 0:
                        node = SparseMatrixNode((i, j), matrix[i][j])
                        self.__insert(node)
        
        if (len(elements) > 0):
            for x in elements:
                node = SparseMatrixNode(x[0], x[1])
                self.__insert(node)

        # Assume that columns_count * rows_count fits in memory
    def __repr__(self):
        view_list = [
            ["0"] * self.columns_count for i in range(self.rows_count)]

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
            if node.position[0] < curr_node.right.position[0]:
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
            if node.position[1] < curr_node.bottom.position[1]:
                node.bottom = curr_node.bottom
                curr_node.bottom = node
                return
            curr_node = curr_node.bottom

        curr_node.bottom = node
        node.bottom = None

    def __find_element(self, position):
        for i in range(self.rows_count):
            node = self.rows[i]
            while node is not None:
                if node.position == position:
                    return node
                node = node.right
        return None

    def change_element(self, position, value):
        search_result = self.__find_element(position)
        if search_result is None:
            self.__insert(SparseMatrixNode(position, value))
        else:
            search_result.value = value

    def get_non_zeros(self):
        non_zeros = list()
        for i in range(self.rows_count):
            node = self.rows[i]
            while node is not None:
                non_zeros.append((node.position, node.value))
                node = node.right
        return non_zeros


elems = [((0, 0), -2), ((3, 3), 11), ((2, 3), 23),
         ((4, 3), 22), ((1, 1), 24), ((0, 1), -12)]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mt = SparseMatrix(rows_count=5, columns_count=5, elements=elems)
mt.change_element((4, 2), 101)
print(mt)
