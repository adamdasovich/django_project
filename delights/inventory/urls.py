from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredientlist'),
    path('ingredients/create/', views.IngredientCreateView.as_view(), name='ingredientcreate'),
    path('ingredients/<pk>/update', views.IngredientUpdateView.as_view(), name='ingredientupdate'),
    path('ingredients/<pk>/delete', views.IngredientDeleteView.as_view(), name='ingredientdelete'),
]