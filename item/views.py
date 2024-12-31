from django.shortcuts import get_object_or_404, render

from item.models import Item



def detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {'item': item})