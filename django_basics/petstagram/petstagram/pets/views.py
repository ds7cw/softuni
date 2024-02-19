from django.shortcuts import redirect, render
from .models import Pet
from .forms import PetCreateForm, PetEditForm, PetDeleteForm


# Create your views here.
def pet_create(request):
    pet_form = PetCreateForm(request.POST or None)
    context = {
        'pet_create_form': pet_form,
    }

    if pet_form.is_valid():
        pet_form.save()
        return redirect('home-page')
        
    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug),
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).first()
    pet_form = PetEditForm(instance=pet,)
    context = {'pet_edit_form': pet_form, 'username': username, 'pet': pet}
    print(f'--GET-- {request.GET}')
    print(f'\n--POST-- {request.POST}')
    if request.method == 'POST':
        pet_form = PetEditForm(request.POST, instance=pet)
        if pet_form.is_valid():
            pet_form.save()

            return redirect('details-pet', username=username, pet_slug=pet_slug)

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).first()
    pet_form = PetDeleteForm(instance=pet)
    context = {'pet_delete_form': pet_form, 'username':username, 'pet':pet}

    if request.method == 'POST':
        # print(f'{pet} deleted!!!! {pet.slug}')
        pet.delete()
        return redirect('home-page')

    return render(request, 'pets/pet-delete-page.html', context)

