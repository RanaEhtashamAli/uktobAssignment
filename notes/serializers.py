from rest_framework import serializers

from notes.models import Note
from user.serializers import BaseUserSerializer


class NoteSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        depth = 1

    def to_internal_value(self, data):
        data = super(NoteSerializer, self).to_internal_value(data)
        data['user_id'] = self.context.get('request').user.id

        return data
