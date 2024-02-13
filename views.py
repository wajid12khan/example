from django.conf import render


def home(request):
    return  render(request, 'index.html')
    