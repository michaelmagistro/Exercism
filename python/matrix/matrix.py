class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string
        self.matrix2 = self.matrix.split('\n')
        self.matrix3 = []
        for x in self.matrix2:
            self.matrix3.append(x.split())
        self.matrix3 = [[int(s) for s in row] for row in self.matrix3]


    def row(self, index):
        result = []
        for x in self.matrix3[index - 1]:
            result.append(x)
        return result

    def column(self, index):
        result = []
        for x in self.matrix3:
            result.append(x[index - 1])
        return result