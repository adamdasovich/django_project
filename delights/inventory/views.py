from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient
from .forms import IngredientForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients.html'

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_add.html'
    form_class = IngredientForm
    success_url = '/ingredients/'

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update.html'
    form_class = IngredientForm
    success_url = '/ingredients/'

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    success_url = '/ingredients/'
