from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


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


@login_required  # decorator - adds login required to view
def profile(request):

    if request.method == 'POST':
        # pass in request.POST to keep instances set
        u_form = UserUpdateForm(request.POST, instance=request.user)

        # request.FILES image data coming in with POST request - only for p_form, not u_form
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been udpated!')

            # want to redirect here instead of letting it fall to render below because of POST-GET redirect pattern
            #
            # return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
