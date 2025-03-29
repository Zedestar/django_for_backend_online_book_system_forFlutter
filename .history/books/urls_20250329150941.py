from django.urls import path
from . import views


urlpatterns = [
    path('bookList/', views.getBookList, name="bookList"),
    path('book/<int:id>/', views.getBook, name="book"),
    path('updateBook/<int:id>/', views.updateBook, name="updateBook"),
    path('deleteBook/<int:id>/', views.deleteBook, name="deleteBook"),
    # ###############################################################
    # Urls for teacher's work
    ###############################################################
    path('studentList/', views.getStudentList, name="studentList"),
    # path('courseList/', views.getCourseList, name="courseList"),
]
