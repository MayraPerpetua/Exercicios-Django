from django.urls import path
from.import views

app_name = "testepratico"

urlpatterns = [
    path('aluno/', views.IndexView.as_view(), name= 'aluno'),
    path('media/', views.Media.as_view(), name='media'),


    #path('testepratico/<int:media_id>/',
        #views.testepratico, name='testepratico'
   # ),
]
