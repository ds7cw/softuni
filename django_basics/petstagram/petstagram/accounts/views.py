from django.shortcuts import render

# Create your views here.
def signup_user(request):
    return render(request, 'accounts/register-page.html')


def signin_user(request):

    return render(request, 'accounts/login-page.html')


def signout_user(request):

    pass


def details_user(request, pk):

    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):

    pass


def delete_user(request, pk):
    
    pass
