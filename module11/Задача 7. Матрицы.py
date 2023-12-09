class Matrix:
    def __init__(self, matrix=None):
        self.matrix = matrix if matrix is not None else []

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы разных размеров не могут быть сложены")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы разных размеров не могут быть вычтены")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Матрицы не подходят для умножения")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))) for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

sum_matrix = matrix1 + matrix2
print("Сложение матриц:")
print(sum_matrix)

sub_matrix = matrix1 - matrix2
print("\nВычитание матриц:")
print(sub_matrix)

mul_matrix = matrix1 * matrix2
print("\nУмножение матриц:")
print(mul_matrix)

transposed_matrix = matrix1.transpose()
print("\nТранспонированная матрица:")
print(transposed_matrix)