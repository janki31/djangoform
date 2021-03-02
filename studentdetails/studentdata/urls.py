from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('show/',views.show,name='show'),
    path('edit/<int:sid>',views.edit,name='edit'),
    path('update/<int:sid>',views.update,name='update'),
    path('delete/<int:sid>',views.delete,name='delete'),
]
