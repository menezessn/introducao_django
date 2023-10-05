from django.shortcuts import render



# Create your views here.

def blog(request):
    context = {
        'text': 'Estamos no blog',
        'title': 'blog'
    }
    return render(request, 'blog/index.html', context)

def exemplo(request):
    context = {
        'text': 'Estamos na exemplo',
        'title': 'Exemplo'
    }
    return render(request, 'blog/exemplo.html', context)
