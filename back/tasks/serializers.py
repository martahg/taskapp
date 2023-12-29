from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'done']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('partial'):
            self.fields['titulo'].required = False
            self.fields['descripcion'].required = False
