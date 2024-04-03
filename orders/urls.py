from django.urls import path
from .views import MenuListView, CategoryMenuListView, CreateOrderView, OrderListView

app_name='orders'
urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('category/<int:category_id>/', MenuListView.as_view(), name='menu_by_category'),
    path('order/', CreateOrderView.as_view(), name='create_order'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]
