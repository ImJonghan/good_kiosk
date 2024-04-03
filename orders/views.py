from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Menu, Category, Order
from django.shortcuts import get_object_or_404


# 메인 페이지 및 전체 메뉴 보기
class MenuListView(ListView):
    model = Menu
    template_name = 'orders/menu_list.html'
    context_object_name = 'menus'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            return Menu.objects.filter(category=category)
        return Menu.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category_id'] = int(self.kwargs.get('category_id', '0'))
        return context

# 카테고리 별 메뉴 보기
class CategoryMenuListView(DetailView):
    model = Category
    template_name = 'orders/category_menu_list.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(category=self.object)
        return context

# 주문 생성 페이지
class CreateOrderView(CreateView):
    model = Order
    template_name = 'orders/create_order.html'
    fields = ['menu', 'quantity', 'customer_name']  # 예시 필드, 실제 모델에 맞게 조정 필요
    success_url = reverse_lazy('order_list')

# 주문 내역 보기
class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
