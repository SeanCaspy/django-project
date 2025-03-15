from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def index(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'food/index.html', context)

def item(request):
    items = Item.objects.all()
    return HttpResponse(items)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'food/detail.html', context)
