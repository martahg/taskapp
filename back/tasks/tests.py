# tasks/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tarea

class TareaAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_lista_tareas(self):
        response = self.client.get('/api/tareas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_tarea(self):
        data = {'titulo': 'Tarea de prueba', 'descripcion': 'Esta es una tarea de prueba.', 'done': False}
        response = self.client.post('/api/tareas/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_actualizar_tarea(self):
        tarea = Tarea.objects.create(titulo='Tarea a actualizar', descripcion='Descripción de tarea a actualizar', done=True)
        updated_data = {'titulo': 'Tarea actualizada', 'descripcion': 'Descripción actualizada', 'done': True}
        response = self.client.put(f'/api/tareas/{tarea.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_eliminar_tarea(self):
        tarea = Tarea.objects.create(titulo='Tarea a eliminar', descripcion='Descripción de tarea a eliminar', done=True)
        response = self.client.delete(f'/api/tareas/{tarea.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
