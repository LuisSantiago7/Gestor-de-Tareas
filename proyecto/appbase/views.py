from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea


class Login(LoginView):
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tareas')
    
class RegistroUser(FormView):
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroUser, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(RegistroUser, self).get(*args, **kwargs)
    
class listaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\tarea_list.html'
    context_object_name = 'Tareas'
    
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['Tareas'] = context['Tareas'].filter(user = self.request.user)
        context['count'] = context['Tareas'].filter(complete = False).count()
        
        search1 = self.request.GET.get('search') or ''
        if search1:
            context['Tareas'] = context['Tareas'].filter(title__icontains = search1)
        context['search1'] = search1
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\tarea.html'
    context_object_name = 'Tarea'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\tarea_from.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tareas')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearTarea, self).form_valid(form)
        
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\tarea_from.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tareas')
    
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'Tareas'
    template_name = 'C:\\Users\\luisa\\OneDrive\\Documentos\\misEntornos\\mi_Web\\src\\proyecto\\appbase\\templates\\base\\tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas')
    

