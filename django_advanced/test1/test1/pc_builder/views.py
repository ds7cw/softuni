from django.shortcuts import render, redirect
from .models import Computer
from .forms import ComputerCreateModelForm

# Create your views here.
def create_pc(request):
    form = ComputerCreateModelForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index-page')

    elif request.method == 'GET':
        return render(request, 'pc_builder/create_pc.html', context)
