from django.urls import path
from .views import TareaListCreateAPIView, TareaDetailAPIView, ActualizarEstadoTarea

urlpatterns = [
    path('tareas/', TareaListCreateAPIView.as_view(), name='tarea-list-create'),
    #path('tareas/<int:pk>/', TareaDetailAPIView.as_view(), name='tarea-detail'),
    path('tareas/<int:pk>/', ActualizarEstadoTarea.as_view(), name='actualizar_tarea'),
]
