
class Matrix:
    def __init__(self):
        self.dim = [0,0]
        self.rows = []

    # Accepts an integer and returns that row. Rows are numbered starting at 1 from the top.
    def getRow(self, index):
        i = index-1
        return self.rows[i]

    # Accepts an integer and returns that column. Columns are numbered starting at 1 from the left.
    def getColumn(self, index):
        j = index-1
        column = []
        for i in range(0, self.dim[0]):
            column.append(self.rows[i][j])
        return column

    # Replaces a currently existing row with a new one.
    # 'index' accepts an integer which specifies the row to be replaced.
    # 'row' accepts a list of integers which is the row that will replace it.
    def setRow(self, index, row):
        i = index-1
        if len(row) == self.dim[1]:
            self.rows[i] = row
        else:
            print("Row does not fit matrix size")

    # Replaces a currently existing column with a new one.
    # 'index' accepts an integer which specifies the column to be replaced.
    # 'row' accepts a list of integers which is the column that will replace it.
    def setColumn(self, index, column):
        j = index-1
        if len(column) == self.dim[0]:
            for i in range(0, self.dim[0]):
                self.rows[i][j] = column[i]
        else:
            print("Column does not fit matrix size")

    # Accepts a list and appends it to the bottom of the matrix as a row
    def addRow(self, row):
        if len(row) == self.dim[1]:
            self.dim[0] = self.dim[0] + 1
            self.rows.append(row)
        else:
            print("Row does not fit matrix size")

    # Accepts a list and appends it to the right of the matrix as a column
    def addColumn(self, column):
        if len(column) == self.dim[0]:
            self.dim[1] = self.dim[1] + 1
            for i in range(0, self.dim[0]):
                self.rows[i].append(column[i])
        else:
            print("Column does not fit matrix size")

    # Replaces the value at an exact coordinate with a new one
    # 'coordinate' accepts a point in the matrix formatted as a list: [i,j]
    # i is the row number and j is the column number
    # 'replacement' accepts an integer which will replace the old value
    def replaceAt(self, coordinate, replacement):
        coordinate[0] = coordinate[0] - 1
        coordinate[1] = coordinate[1] - 1
        self.rows[coordinate[0]][coordinate[1]] = replacement

    # Returns the value at a point in the matrix. 
    # The input is a point formatted as a list: [i,j]
    # i is the row number and j is the column number
    def getAt(self, coordinate):
        coordinate[0] = coordinate[0] - 1
        coordinate[1] = coordinate[1] - 1
        return self.rows[coordinate[0]][coordinate[1]]

    # Displays the full matrix
    def print(self):
        for row in self.rows:
            print(row)

# This creates a new Matrix object with the dimensions m x n, filled with zeros.
# m is the number of rows and n is the number of columns.
def newMatrix(m,n, *args):
    newMatrix = Matrix()
    newMatrix.dim[1] = n
    for i in range(0, m):
        blankRow = []
        for i in range(0, n):
            blankRow.append(0)
        newMatrix.addRow(blankRow)
    return newMatrix



