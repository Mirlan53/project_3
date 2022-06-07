from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def blog_list(request):
	return render(request, 'blogs/blog_list.html')

@login_required()
def blog_create(request):
	return render(request, 'blogs/blog_create.html')