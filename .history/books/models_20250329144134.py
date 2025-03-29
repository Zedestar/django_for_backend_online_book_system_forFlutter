from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
    
    
class Subject(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    name = models.CharField(max_length=400, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    discount = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="picture_images", blank=False, null=False)
    preview = models.FileField(upload_to="book_previews")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=False, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=False, null=False)
    Publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank=False, null=False)
    
    def __str__(self):
        return f"{self.name} published by {self.Publisher}"
    
    
    
    # ##########################################################
    # Models for teacher work
    # ##########################################################
    
    
    
class Student(models.Model):
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
        
    def __str__(self):
        return f"self.name = {self.course}"
        

class Subject(models.Model):
    course_name = models.CharField(max_length=250)
    accademic_year = models.IntegerField()
    
    def __str__(self):
        return f"self.course_name = {self.accademic_year}"