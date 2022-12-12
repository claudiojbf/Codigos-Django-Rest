from django.test import TestCase
from aluraflix.models import Programa

class ProgamaModelTestCase(TestCase):

    def setUp(self):
        self.progama = Programa(
            titulo = 'Procurando ninguem em latim',
            data_lancamento = '2003-07-04'
        )

    def test_verifica_atributos_do_progama(self):
        """Teste que verifica os atributos de um progama com valor default"""
        self.assertEqual(self.progama.titulo, 'Procurando ninguem em latim')
        self.assertEqual(self.progama.tipo, 'F')
        self.assertEqual(self.progama.data_lancamento, '2003-07-04')
        self.assertEqual(self.progama.likes, 0)
        self.assertEqual(self.progama.dislikes, 0)