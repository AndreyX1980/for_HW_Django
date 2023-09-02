from django.urls import path

from hw_2.views import get_orders, get_history, add_product


urlpatterns = [
    path ('orders/<int:client_id>',get_orders, name = 'orders'),
    path('orders/history/<int:client_id>/<int:days_before>', get_history, name='history'),
    path ('product/',add_product, name ='product')
]