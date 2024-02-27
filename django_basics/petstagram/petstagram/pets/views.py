from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Pet
from .forms import PetCreateForm, PetEditForm, PetDeleteForm
from django.views import generic


# Create your views here.
# def pet_create(request):
#     pet_form = PetCreateForm(request.POST or None)
#     context = {
#         'pet_create_form': pet_form,
#     }

#     if pet_form.is_valid():
#         pet_form.save()
#         return redirect('home-page')
        
#     return render(request, 'pets/pet-add-page.html', context)


class PetCreateView(generic.CreateView):

    form_class = PetCreateForm
    # model = Pet
    # fields = ['name', 'date_of_birth', 'personal_photo',]
    template_name = 'pets/pet-add-page.html'
    
    def get_success_url(self) -> str:
        return reverse('details-pet', kwargs={'username': 'ddd', 'pet_slug': self.object.slug})
    



# def pet_details(request, username, pet_slug):
#     context = {
#         'pet': Pet.objects.get(slug=pet_slug),
#     }

#     return render(request, 'pets/pet-details-page.html', context)


class PetDetailView(generic.DetailView):

    model = Pet
    template_name = 'pets/pet-details-page.html'
    # slug_field = 'slug' # name of the field in the model
    slug_url_kwarg = 'pet_slug' # name of the param in the URL
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        return context


# def pet_edit(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).first()
#     pet_form = PetEditForm(instance=pet,)
#     context = {'pet_edit_form': pet_form, 'username': username, 'pet': pet}
#     print(f'--GET-- {request.GET}')
#     print(f'\n--POST-- {request.POST}')
#     if request.method == 'POST':
#         pet_form = PetEditForm(request.POST, instance=pet)
#         if pet_form.is_valid():
#             pet_form.save()

#             return redirect('details-pet', username=username, pet_slug=pet_slug)

#     return render(request, 'pets/pet-edit-page.html', context)


class PetEditView(generic.UpdateView):

    model = Pet
    # queryset = Pet.objects.all()
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'

    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'ddd' 

        return context
    
    def get_success_url(self) -> str:
    
        return reverse('details-pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug
        }) 


# def pet_delete(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).first()
#     pet_form = PetDeleteForm(instance=pet)
#     context = {'pet_delete_form': pet_form, 'username':username, 'pet':pet}

#     if request.method == 'POST':
#         # print(f'{pet} deleted!!!! {pet.slug}')
#         pet.delete()
#         return redirect('home-page')

#     return render(request, 'pets/pet-delete-page.html', context)


class PetDeleteView(generic.DeleteView):

    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        context['username'] = 'ddd'
        return context
    
    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)