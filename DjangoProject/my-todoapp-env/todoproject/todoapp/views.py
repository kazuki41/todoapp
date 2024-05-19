from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from todoapp.models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
 model = Task
 context_object_name = "tasks"
 def get_context_data(self,**kwargs):
  context = super().get_context_data(**kwargs)
  context['tasks'] = context['tasks'].filter(user=self.request.user)

  #print(context)
  return context
  

class TaskDetail(LoginRequiredMixin,DetailView):
 model = Task
 context_object_name = "task"

class TaskCreate(LoginRequiredMixin,CreateView):
 model = Task
 fields = ['title', 'description' ,'completed']
 success_url = reverse_lazy('tasks')
 def form_valid(self, form):
  form.instance.user = self.request.user
  return super().form_valid(form)
  

class TaskUpdate(LoginRequiredMixin,UpdateView):
 model = Task
 fields = "__all__"
 success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
 model = Task
 fields = "__all__"
 success_url = reverse_lazy('tasks')
 context_object_name = "task"

class TaskListLoginView(LoginView):
 fields = "__all__"
 template_name = "todoapp/login.html"
 def get_success_url(self):
  return reverse_lazy('tasks')