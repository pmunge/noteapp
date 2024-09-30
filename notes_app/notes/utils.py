#response that will be returned

from rest_framework.response import Response
#model to be used
from .models import Note
#serializer we will use
from .serializers import NoteSerializer

# function that returns the notes list
def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
#function that returns the note detail
def getNotesList(request, pk):
    notes= Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

#function that creates a note
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
#function that updates a note
def updateNote(request, pk):
    data = request.data
    note = Note.Objects.get(id=pk)
    serializer = NoteSerializer(instance =note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#function that deletes a note
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response ('Note deleted!')



