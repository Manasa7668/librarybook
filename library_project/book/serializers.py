from rest_framework import serializers  # type: ignore
from .models import Book

class booksserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['id','Title','Author','Year','Genre']