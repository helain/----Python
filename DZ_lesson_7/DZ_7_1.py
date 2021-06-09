"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m_line = ''
        for line in self.matrix:
            for el in line:
                m_line += f'{el} '
            m_line += '\n'
        return m_line

    def __add__(self, other):
        result_matrix = []
        if len(self.matrix) != len(other.matrix):
            print('Размерности матриц не совпадают. сложение невозможно')
            return None
        for line_a in self.matrix:
            for line_b in other.matrix:
                result_line = []
                if len(line_a) != len(line_b):
                    print('Размерности матриц не совпадают. сложение невозможно')
                    return None
                for i in range(len(line_a)):
                    result_line.append(line_a[i]+line_b[i])
                result_matrix.append(result_line)
            return Matrix(result_matrix)


a = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
b = Matrix([[30, 20, 10], [30, 20, 10], [30, 20, 10]])

print(f'Матрица "a"\n{a}')
print(f'Матрица "b"\n{b}')
print(f'Матрица "a + b"\n{a+b}')
