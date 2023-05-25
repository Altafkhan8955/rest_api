from django.db import models
from rest_framework import serializers

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration = models.FloatField()

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Instructor(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return self.email

class Books(models.Model):
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='Books')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name="book-detail")
    class Meta:
        model = Instructor
        fields = '__all__'