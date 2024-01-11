from django.shortcuts import render, get_object_or_404
from .models import Fruit

# Create your views here.
def index(request):
    return render(request, 'common\index.html')


def dashboard(request):
    return render(request, 'common\dashboard.html')


def create_fruit(request):
    return render(request, 'fruits\create-fruit.html')


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)
    # fruit = get_object_or_404(Fruit, pk=fruit_id)
    context = {'fruit': fruit}
    return render(request, 'fruits\details-fruit.html', context=context)


def edit_fruit(request, fruit_id):
    return render(request, 'fruits\edit-fruit.html')


def delete_fruit(request, fruit_id):
    return render(request, 'fruits\delete-fruit.html')


def create_category(request):
    return render(request, 'categories\create-category.html')