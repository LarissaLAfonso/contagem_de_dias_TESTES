import unittest
import contagem_dias
import datetime

class Testes(unittest.TestCase):

    def teste_diferenca_datas(self):
        data_1 = datetime.datetime(23, 8, 19)
        data_2 = datetime.datetime(24, 8, 19)
        self.assertEqual(contagem_dias.contagem_dias(data_1, data_2), 366)

if __name__ == "__main__":
    unittest.main()
