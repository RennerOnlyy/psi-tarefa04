from django.test import TestCase, Client
from django.urls import reverse
from .models import Tarefa

class TarefaTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.tarefa = Tarefa.objects.create(titulo="Teste Tarefa")

    def test_model_str(self):
        self.assertEqual(str(self.tarefa), "Teste Tarefa")

    def test_lista_tarefas_view(self):
        response = self.client.get(reverse('lista_tarefas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Minhas Tarefas")
        self.assertContains(response, "Teste Tarefa")

    def test_adicionar_tarefa(self):
        response = self.client.post(reverse('lista_tarefas'), {'titulo': 'Nova Tarefa'})
        self.assertEqual(response.status_code, 302) # Redirect
        self.assertEqual(Tarefa.objects.count(), 2)

    def test_concluir_tarefa(self):
        self.assertFalse(self.tarefa.concluida)
        response = self.client.get(reverse('concluir_tarefa', args=[self.tarefa.id]))
        self.assertEqual(response.status_code, 302)
        self.tarefa.refresh_from_db()
        self.assertTrue(self.tarefa.concluida)

    def test_excluir_tarefa(self):
        response = self.client.get(reverse('excluir_tarefa', args=[self.tarefa.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tarefa.objects.count(), 0)
