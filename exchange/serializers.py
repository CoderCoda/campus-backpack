from rest_framework import serializers
from .models import Textbook

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Textbook
        fields = ['title', 'author', 'ISBN', 'condition', 'notes', 'price']
