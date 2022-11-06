from django.shortcuts import render, redirect
from .models import Articales
from .forms import ArticalesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articales.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = Articales
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articales
    template_name = 'news/create.html'
    form_class = ArticalesForm

class NewsDeleteView(DeleteView):
    model = Articales
    template_name = 'news/news-delete.html'
    success_url = '/news'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = ArticalesForm()
    data = {
        'form': form,
        'eror': error
    }
    return render(request, 'news/create.html', data)
