class SparseMatrixNode:
    def __init__(self, position, value, right=None, bottom=None):
        self.position = position
        self.value = value
        self.right = right
        self.bottom = bottom

    def __repr__(self):
        return str(self.value)

    def get_right(self):
        return self.right

    def get_bottom(self):
        return self.bottom

class SparseMatrix:
    def __init__(self, rows_count=0, columns_count=0):
        self.columns_count = columns_count
        self.rows_count = rows_count
        self.columns = [None] * self.columns_count
        self.rows = [None] * self.rows_count

    @classmethod
    def from_matrix(cls, matrix=[]):
        rows_count = len(matrix)
        columns_count = len(matrix[0]) if rows_count > 0 else 0

        created = cls(rows_count, columns_count)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    created._insert(SparseMatrixNode((i, j), matrix[i][j]))

        return created

    @classmethod
    def from_elements(cls, elements=[], rows_count=0, columns_count=0):
        created = cls(rows_count, columns_count)
        for x in elements:
            created._insert(SparseMatrixNode(x[0], x[1]))
        return created

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

    def _insert(self, node):
        self._insert_node(node, in_row=True)
        self._insert_node(node, in_row=False)

    def _insert_node(self, node, in_row):
        COORDINATE = 0 if in_row else 1

        def get_node(matrix, position, in_row):
            if in_row:
                return matrix.rows[position]
            else:
                return matrix.columns[position]

        def get_next(node, in_row):
            if in_row:
                return node.right
            else:
                return node.bottom

        def set_node(matrix, position, in_row, value):
            if in_row:
                matrix.rows[position] = value
            else:
                matrix.columns[position] = value

        def set_next(node, in_row, value):
            if in_row:
                node.right = value
            else:
                node.bottom = value

        curr_node = get_node(self, node.position[COORDINATE], in_row)

        if curr_node is None:
            set_node(self, node.position[COORDINATE], in_row, node)
            return

        if node.position[COORDINATE ^ 1] < curr_node.position[COORDINATE ^ 1]:
            set_node(self, node.position[COORDINATE], in_row, node)
            set_next(node, in_row, curr_node)
            return

        while get_next(curr_node, in_row) is not None:
            if node.position[COORDINATE ^ 1] < get_next(curr_node, in_row).position[COORDINATE ^ 1]:
                set_next(node, in_row, get_next(curr_node, in_row))
                set_next(curr_node, in_row, node)
                return
            curr_node = get_next(curr_node, in_row)

        set_next(curr_node, in_row, node)
        set_next(node, in_row, None)

    def _find_element(self, position):
        for i in range(self.rows_count):
            node = self.rows[i]
            while node is not None:
                if node.position == position:
                    return node
                node = node.right
        return None

    def change_element(self, position, value):
        search_result = self._find_element(position)
        if search_result is None:
            self._insert(SparseMatrixNode(position, value))
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
    
    def get_first(self, row_idx=-1, col_idx=-1):
        if row_idx != -1:
            return self.rows[row_idx]
        else:
            return self.columns[col_idx]

elems = [((0, 0), -2), ((3, 3), 11), ((2, 3), 23),
         ((4, 3), 22), ((1, 1), 24), ((0, 1), -12), ((9, 0), 666), ((0, 9), 1388)]
# matrix = [[0, 0, 0, 0], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

mt = SparseMatrix.from_elements(elems, 10, 10)
# mt.change_element((1, 1), 101)

print(mt)
print(mt.get_non_zeros())