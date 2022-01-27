from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("stadiums/", include("stadium.urls", namespace="stadiums")),
    path("matches/", include("matches.urls", namespace="matches")),
    
]
