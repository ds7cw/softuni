from django.shortcuts import render
from .models import Pet


# Create your views here.
def pet_create(request):
    context = {}

    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug),
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_slug):
    context = {}

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):
    context = {}

    return render(request, 'pets/pet-delete-page.html', context)

