from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm

def login_page(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username, password)
			if user is not None:
				login(request, user) 
				return redirect('blog_list')
	form = AuthenticationForm()
	context = {
		'form': form
	}

	return render(request, 'users/login_page.html', context)
# Create your views here.
