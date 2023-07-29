from django.urls import path
from .import views
app_name = 'SSapp'

urlpatterns = [

    path('',views.home,name='home'),
    path('allproducts/',views.Allproduct,name='allproducts'),
    path('student/', views.Student, name='student'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
    path('newpage/', views.Newpage, name='newpage'),
    path('prodetail/<int:id>',views.prodetail,name='prodetail'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('bookrent/', views.BookRent, name='bookrent'),
    path('reviews/',views.reviews,name='reviews'),
    path('add_reviews/',views.add_reviews,name='add_reviews'),
]
