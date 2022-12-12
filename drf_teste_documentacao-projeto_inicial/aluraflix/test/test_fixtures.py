from django.test import TestCase
from aluraflix.models import Programa

class FixturesDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        progama_bizarro = Programa.objects.get(pk = 1)
        todos_progamas = Programa.objects.all()
        self.assertEqual(progama_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_progamas), 9)