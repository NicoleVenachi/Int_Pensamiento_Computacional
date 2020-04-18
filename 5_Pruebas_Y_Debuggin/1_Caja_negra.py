import unittest

def suma(num_1, num2_2):
    return num_1 + num2_2

class CajaNegraTest(unittest.TestCase):


    def test_suma_dos_positivos(self):
        num_1 = 10
        num2_2 = 5

        resultado = suma(num_1, num2_2)
        self.assertEqual(resultado, 15)  # Lo que espero

    def test_suma_dos_negativos(self):
        num_1 = -10
        num2_2 = -7
        resultado = suma(num_1, num2_2)
        self.assertEqual(resultado, -17)



if __name__ == '__main__':
    unittest.main()
