from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),  # Default route
# ]
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('chatbot.urls')),  # Includes chatbot app URLs
# ]
# from django.urls import path
# from chatbot import views

urlpatterns = [
    path('', views.index, name='index'),  # Matches views.index
    path('chat/', views.chat, name='chat'),  # Matches views.chat
]