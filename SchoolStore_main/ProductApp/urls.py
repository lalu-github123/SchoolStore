from django.urls import path
from .import views
app_name = 'ProductApp'

urlpatterns = [

    path('booksall/',views.booksall,name='booksall'),
    path('<slug:c_slug>/',views.booksall,name='books_by_category'),
    #path('categories/',views.categories,name='categories'),

]