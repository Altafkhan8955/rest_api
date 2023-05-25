from django.contrib import admin
from django.urls import path,include
from .views import CourseListView,courseDetailView
from restapp.views import courseview,Detailview,ListDetailview,courseDetailview
from rest_framework.authtoken.views import obtain_auth_token
'''from rest_framework.routers import DefaultRouter
from restapp.views import courseview

router = DefaultRouter()  #courseview:courseview
router.register('course', courseview, basename='course')'''

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/courses', CourseListView),
    path('api/courses/<int:pk>', courseDetailView),
    #path('api/', include(router.urls))
    path('api/view', courseview.as_view()),
    path('api/detailview', Detailview.as_view(), name=''),
    path('api/listdetail/<int:pk>',ListDetailview.as_view()),
    path('api/coursedetailView/<int:pk>', courseDetailview.as_view(), name="book-detail"),
    path('auth/logon', obtain_auth_token, name='create-token' ),
    path('auth/login', TokenObtainPairView.as_view(), name='create-token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')


]