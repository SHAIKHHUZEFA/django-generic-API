from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('addbook',views.AddBook.as_view()),
    path('retrieveaddbook',views.retrieveAdddbook.as_view()),
    path('viewallbook',views.viewAllBook.as_view()),
    path('updatebook/<int:id>',views.UpdateBook.as_view()),
    path('deletebook/<int:id>',views.DeleteBook.as_view()),

]