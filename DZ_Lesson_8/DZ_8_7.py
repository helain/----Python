"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
#a+bi
class Complex:
    def __init__(self, number):
        self.number = number
        self.number_str = number.split('+')
        self.real_number = self.number_str[0]
        self.imaginary = self.number_str[1]

# (a+bi)+(c+di)=(a+c)+(b+d)i
    def __add__(self, other):
        a = int(self.real_number)
        b = int(self.imaginary.rstrip('i'))
        c = int(other.real_number)
        d = int(other.imaginary.rstrip('i'))
        result = f'{a+c}+{b+d}i'
        return Complex(result)
# (a+bi)*(c+di)=(ac-bd)+(bc+ad)i
    def __mul__(self, other):
        a = int(self.real_number)
        b = int(self.imaginary.rstrip('i'))
        c = int(other.real_number)
        d = int(other.imaginary.rstrip('i'))
        result = f'{a * c - b * d}+{b * c + a * d}i'
        return Complex(result)

n1 = Complex('1+2i')
n2 = Complex('2+3i')
result_add = n1+n2
result_mul = n1*n2
print('Сложение')
print(result_add.number)
print('Умножение')
print(result_mul.number)

