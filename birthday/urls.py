from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('memories/',views.memories,name="memories"),
    path('videos/',views.videos,name="videos"),
    path('stories/',views.stories,name="stories"),
    path('addmemories/',views.addmemories,name="addmemories"),
    path('addvideos/',views.addvideos,name="addvideos"),
    path('addstories/',views.addstories,name="addstories"),
    path('about/',views.about,name="about"),
    path('logout/',views.logout,name="logout"),
    path('DeleteVideo/<int:v_id>/',views.DeleteVideo,name="DeleteVideo"),
    path('DeleteMemory/<int:m_id>/',views.DeleteMemory,name="DeleteMemory"),
    path('DeleteStory/<int:s_id>/',views.DeleteStory,name="DeleteStory"),


]
