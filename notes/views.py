from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

from notes.models import Note
from notes.serializers import NoteSerializer
from langchain.llms import OpenAI


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'], name='Get Summary')
    def get_summary(self, request, pk=None):
        note = self.queryset.filter(id=pk).first()
        if not note:
            raise ValidationError({'error': 'Invalid note ID provided.'})
        llm = OpenAI(openai_api_key=settings.OPENAI_API_KEY)

        try:
            response = llm.invoke(f'Please summarize the following notes for me and list down the important points: '
                                  f'{note.content}')
        except Exception as e:
            print(e)
            raise ValidationError({'error': 'Unable to communicate with OpenAI API.'})

        return Response({'summary': response}, status=status.HTTP_200_OK)
