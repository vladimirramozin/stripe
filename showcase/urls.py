from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_info, name='view_info'),
    path('item/<int:pk>', views.item, name='item'),
    path('buy/<int:pk>', views.create_checkout_session, name='checkout'),
    path('success.html/', views.success, name='success'),
    path('cancel.html/', views.cancel, name='cancel'),
]
