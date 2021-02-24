from django.urls import path
from .views import ExpenseListView, ExpenseDetailView

urlpatterns = [
    path('', ExpenseListView.as_view(), name="expenses list"),
    path('<int:id>', ExpenseDetailView.as_view(), name="expenses detail")
]