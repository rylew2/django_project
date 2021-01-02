from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        # if it's a post:
        # 1) instantiate form with post data
        # 2) check if valid
        # 3) save form
        # 4) display a flash message - one-time alert (flash messages added to base.html template)
        # 5) redirect to home
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # validated data is in a cleaned_data dictionary
            form.save()
            username = form.cleaned_data.get('username')
            # flash message
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

        # if form is invalid, it renders the form again with the values
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
