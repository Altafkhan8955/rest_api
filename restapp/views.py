from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Course,CourseSerializer,Instructor,InstructorSerializer,Books,BookSerializer
from django.http import Http404
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication
# Create your views her stutae.

@api_view(['GET', 'POST'])
def CourseListView(request):
    if request.method == 'GET':
        course = Course.objects.all()
        courseSerializer = CourseSerializer(course, many=True)
        return Response(courseSerializer.data)
    
    elif request.method == 'POST':
        courseSerializer = CourseSerializer(data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def courseDetailView(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        courseSerializer = CourseSerializer(course)
        return Response(courseSerializer.data)
    
    elif request.method == "PUT":
        courseSerializer = CourseSerializer(course, data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)
    
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
############## class Based API ####################
class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        
        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False

class courseview(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class courseDetailview(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = [IsAuthenticated]
   #authentication_classes  = [BasicAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class Detailview(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all() 

class ListDetailview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

'''class courseview(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class courseview(ViewSet):
    def list(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        courseSerializer = CourseSerializer(data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)
    
    def retrieve(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def update(self, request, pk):
        course = Course.objects.get(pk=pk)
        courseSerializer = CourseSerializer(course, data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)
    
    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
    

    

'''class courseview(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class Detailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class courseview(generics.ListAPIView,generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class Detailview(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class courseview(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class Detailview(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)'''

'''class courseview(APIView):
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        courseSerializer = CourseSerializer(data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)

class Detailview(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        course = self.get_course(pk)
        seriliazer = CourseSerializer(course)
        return Response(seriliazer.data)
    
    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        course = self.get_course(pk)
        courseSerializer = CourseSerializer(course, data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)'''