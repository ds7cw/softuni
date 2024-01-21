from django.shortcuts import render, get_object_or_404, redirect
from .models import Fruit

from .forms import CategoryCreateForm, FruitCreateForm


# Create your views here.
def index(request):
    return render(request, 'common\index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {'fruits': fruits}

    return render(request, 'common\dashboard.html', context)


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'fruits\create-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)
    # fruit = get_object_or_404(Fruit, pk=fruit_id)
    context = {'fruit': fruit}
    return render(request, 'fruits\details-fruit.html', context=context)


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    if request.method == 'GET':
        form = FruitCreateForm(instance=fruit)
    else:
        form = FruitCreateForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'fruit': fruit, 'form': form}
    return render(request, 'fruits\edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    if request.method == 'GET':
        form = FruitCreateForm(instance=fruit)
    else:
        form = FruitCreateForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruits\delete-fruit.html', context)


def create_category(request):
    if request.method == 'GET':
        form = CategoryCreateForm()
    else:
        form = CategoryCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'categories\create-category.html', context)