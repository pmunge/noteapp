# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# Function that returns the notes list
@api_view(['GET'])
def get_notes_list(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# Function that returns the note detail
@api_view(['GET'])
def get_note_detail(request, pk):
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found.'}, status=status.HTTP_404_NOT_FOUND)

# Function that creates a note
@api_view(['POST'])
def create_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        note = serializer.save()
        return Response(NoteSerializer(note).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function that updates a note
@api_view(['PUT'])
def update_note(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function that deletes a note
@api_view(['DELETE'])
def delete_note(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response({'message': 'Note deleted!'}, status=status.HTTP_204_NO_CONTENT)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found.'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_routes(request):
    routes = [
        {'Endpoint': '/notes/', 'Method': 'GET', 'Description': 'Returns a list of notes'},
        {'Endpoint': '/notes/<id>/', 'Method': 'GET', 'Description': 'Returns a single note'},
        {'Endpoint': '/notes/create/', 'Method': 'POST', 'Description': 'Creates a new note'},
        {'Endpoint': '/notes/update/<id>/', 'Method': 'PUT', 'Description': 'Updates an existing note'},
        {'Endpoint': '/notes/delete/<id>/', 'Method': 'DELETE', 'Description': 'Deletes a note'},
    ]
    return Response(routes)
