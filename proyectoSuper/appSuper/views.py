from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def index(request):
  items = Item.objects.all()
  if request.method == 'POST':
    form = ItemForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = ItemForm()
  return render(request, 'appSuper/index.html', {'form': form, 'items': items})

def edit_item(request, pk):
  item = get_object_or_404(Item, pk=pk)
  if request.method == 'POST':
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = ItemForm(instance=item)
  return render(request, 'appSuper/edit_item.html', {'form': form})

def delete_item(request, pk):
  item = get_object_or_404(Item, pk=pk)
  if request.method == 'POST':
    item.delete()
    return redirect('index')
  return render(request, 'appSuper/delete_item.html', {'item': item})

def toggle_check(request, pk):
  item = get_object_or_404(Item, pk=pk)
  item.b_checked = not item.b_checked
  item.save()
  return redirect('index')
