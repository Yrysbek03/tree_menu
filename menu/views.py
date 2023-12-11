from django.shortcuts import render

from menu.models import Menu


def index(request, pk=None):
    context = {}
    if pk:
        item = Menu.objects.get(pk=pk)
        context = {'item': item}

    return render(request, 'menu/index.html', context)

