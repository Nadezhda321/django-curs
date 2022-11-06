from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'ydhcjnm', 121],
        'odj': {
            'car': 'hjk',
            'jk': 18,
            'jdk': 'jkl'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

