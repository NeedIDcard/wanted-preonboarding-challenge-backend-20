from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User
from django.contrib.auth import authenticate, login, logout
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/posts/feeds/')
            else:
                form.add_error(None,'Invalid username or password')

        print(form.cleaned_data)
        context = {'form': form}
        return render(request, 'users/login.html', context)
    else :
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/users/login/')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            profile_image = form.cleaned_data.get('profile_image')
            short_description = form.cleaned_data.get('short_description')
            user = User.objects.create_user(
                username=username,
                password=password1,
                profile_image=profile_image,
                short_description=short_description,
            )

            login(request, user)
            return redirect('/posts/feeds/')

    else:
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)
