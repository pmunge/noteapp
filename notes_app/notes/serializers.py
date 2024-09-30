from rest_framework import serializers
from .models import Note

#create a serializers class
#it converts the note model into json

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'