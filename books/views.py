from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import *

# Create your views here.


def bookList(request):
    return JsonResponse(
        {
            "books":"This is the list of books",
            "author":"This is the list of authors",
        }
    )
    
    
    
@api_view(['GET'])
def getBookList(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)






@api_view(['PUT'])
def updateBook(request, id):
    book = Book.objects.get(pk=id)
    data = request.data
    
    serializer = UpdateBookSerializer(book, data=request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





@api_view(['DELETE'])
def deleteBook(reqest, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response("The book was deleted successfully")




@api_view(['POST'])
def createBook(request):
    data = request.POST
    Book.objects.create()
    
    
    
####### ##########################################################
# Models for teacher work
####### ##########################################################


@api_view(['GET'])
def getStudentList(request):
    students = Student.objects.all()
    serializer = StudentListSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCourseList(request):
    course = Course.objects.all()
    serializer = CourseListSerializer(course, many=True)
    return Response(serializer.data)
