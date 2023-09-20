from leitor_de_arquivos import leitor_de_arquivos
import unittest

class TesteLeitor(unittest.TestCase):
    def verify_if_file_readable(self):
        self.assertEqual(leitor_de_arquivos("data_testing.txt"), "12 de setembro de 2004 - 10 de agosto de 2021")
        self.assertEqual(leitor_de_arquivos("teste.txt"), "21 de Abril de 2022 - 30 de Setembro de 2005")