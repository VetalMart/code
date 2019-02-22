from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Thi is docstring."""
    context_dict = {'boldmessage': "Crunchy, cookie, creamy, candy!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    """Function bla."""
    context_dict = {'name': 'Vetal Mart'}
    return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse("Rango says here is the about page\
     #   <br/> <a href='/rango/'>Index</a>")
