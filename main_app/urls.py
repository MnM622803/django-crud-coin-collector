
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('coins/', views.coin_index, name='coin-index'),
  path('coins/<int:coin_id>/', views.coin_detail, name='coin-detail'),
  path('coins/create/', views.CoinCreate.as_view(), name='coin-create'),
  path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coin-update'),
  path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coin-delete'),
  path(
    'coins/<int:coin_id>/add-globalrank/',
    views.add_globalrank,
    name='add-globalrank'
  ),
  path('signup/', views.signup, name='signup'),
]