from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.response import Response
from rest_framework import status

class TareaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class ActualizarEstadoTarea(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'partial': True})
        return context
