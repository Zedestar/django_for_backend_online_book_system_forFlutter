from rest_framework.serializers import ModelSerializer
from .models import *

# Creating the models here

class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UpdateBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class DeleteBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        
class CreateBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
################################################################
# Models for teacher work
################################################################

class TeacherListSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        

        