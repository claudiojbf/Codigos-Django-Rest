from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgamasSerializerTestCase(TestCase):
    
    def setUp(self):
        self.progama = Programa(
            titulo = 'Procurando ninguem em latim',
            data_lancamento = '2003-07-04',
            tipo = 'F',
            likes = 2340,
            dislikes = 40
        )
        self.serializer = ProgramaSerializer(instance = self.progama)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.progama.titulo)
        self.assertEqual(data['data_lancamento'], self.progama.data_lancamento)
        self.assertEqual(data['tipo'], self.progama.tipo)
        self.assertEqual(data['likes'], self.progama.likes)