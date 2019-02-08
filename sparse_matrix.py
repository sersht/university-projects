# Need: errors handling, refactor, increase scalability of D/S (for greater dimensions),
# check in insertion if element exists, add tests


class SparseMatrixNode:
    def __init__(self, position, value, right=None, bottom=None):
        self.position = position
        self.value = value
        self.right = right
        self.bottom = bottom


class SparseMatrix:
    def __init__(self, rows_count=0, columns_count=0):
        self.columns_count = columns_count
        self.rows_count = rows_count
        self.columns = [None] * self.columns_count
        self.rows = [None] * self.rows_count


    @staticmethod
    def from_matrix(matrix=[]):
        rows_count = len(matrix)
        columns_count = len(matrix[0]) if rows_count > 0 else 0
        
        created = SparseMatrix(rows_count, columns_count)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    created._insert(SparseMatrixNode((i, j), matrix[i][j]))
        
        return created


    @staticmethod
    def from_elements(elements=[], rows_count=0, columns_count=0):
        created = SparseMatrix(rows_count, columns_count)
        for x in elements:
            created._insert(SparseMatrixNode(x[0], x[1]))
        return created


    # Assume that columns_count * rows_count fits in memory
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


    def _insert(self, node):
        self._insert_node(node)
        self._insert_node(node, in_row=False)


    def _insert_node(self, node, in_row=True):
        COORDINATE = 0 if in_row else 1
        
        if in_row:
            curr_node = self.rows[node.position[COORDINATE]]
        else:
            curr_node = self.columns[node.position[COORDINATE]]

        if curr_node is None:
            if in_row:
                self.rows[node.position[COORDINATE]] = node
            else:
                self.columns[node.position[COORDINATE]] = node
            return
            
        if node.position[COORDINATE] < curr_node.position[COORDINATE]:
            if in_row:
                self.rows[node.position[COORDINATE]] = node
                node.right = curr_node
            else:
                self.columns[node.position[COORDINATE]] = node
                node.bottom = curr_node
            return

        if in_row:
            while curr_node.right is not None:
                if node.position[COORDINATE] < curr_node.right.position[COORDINATE]:
                    node.right = curr_node.right
                    curr_node.right = node
                    return
                curr_node = curr_node.right
        else:
            while curr_node.bottom is not None:
                if node.position[COORDINATE] < curr_node.bottom.position[COORDINATE]:
                    node.bottom = curr_node.bottom
                    curr_node.bottom = node
                    return
                curr_node = curr_node.bottom

        if in_row:
            curr_node.right = node
            node.right = None
        else:
            curr_node.bottom = node
            node.bottom = None    


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

    
elems = [((0, 0), -2), ((3, 3), 11), ((2, 3), 23),
         ((4, 3), 22), ((1, 1), 24), ((0, 1), -12)]
matrix = [[0, 0, 0, 0], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

mt = SparseMatrix.from_elements(elems, 10, 10)
# mt.change_element((1,1), 101)

print(mt)
# print(mt.get_non_zeros())