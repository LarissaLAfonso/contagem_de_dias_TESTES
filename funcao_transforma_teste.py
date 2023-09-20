import unittest
import datetime
import funcao_transforma

class Teste(unittest.TestCase):
    def teste_transformacao(self):
        self.assertEqual(funcao_transforma.transforma_em_data("25 de Fevereiro de 1929"), datetime.date(1929, 2, 25))
        self.assertEqual(funcao_transforma.transforma_em_data("12 de Abril de 58"), datetime.date(58, 4, 12))
        self.assertEqual(funcao_transforma.transforma_em_data("1 de NovEMbro de 2023"), datetime.date(2023, 11, 1))

    def teste_datas_inexistentes(self):
        self.assertRaises(ValueError, funcao_transforma.transforma_em_data, "40 de Abril de 89")
        self.assertRaises(ValueError, funcao_transforma.transforma_em_data, "29 de Fevereiro de 2005")

    def teste_datas_quebradas(self):
        self.assertRaises(Exception, funcao_transforma.transforma_em_data, "29 de Jamarço de 2005")
        self.assertRaises(Exception, funcao_transforma.transforma_em_data, "dois de Janeiro de 2005")
        self.assertRaises(Exception, funcao_transforma.transforma_em_data, "29 de Abril de Dois mil e cinco")


if __name__ == "__main__":
   unittest.main()
