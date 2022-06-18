from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator

def blog_list(request):
	ordering = request.GET.get('ordering', '-id')
	blogs = Blog.objects.all()
	q = request.GET.get('q')
	q_user = request.GET.get('q_user')
	if q or q_user:
		blogs = Blog.objects.filter((Q(title__icontains=q) | Q(text__icontains=q)) & Q(author__username__icontains=q_user)).distinct()
	if ordering == 'id':
		blogs = blogs.order_by('id')
		ordering = '-id'
	else:
		blogs = blogs.order_by('id')
		ordering = '-id'
	page_number = request.GET.get('page')
	paginator = Paginator(blogs, 5)
	page = paginator.get_page(page_number)

	context = {
		'ordering': ordering,
		'q': q,
		'q_user': q_user,
		'blogs': page
	}
	return render(request, 'blogs/blog_list.html', context)

@login_required()
def blog_create(request):
	return render(request, 'blogs/blog_create.html')






# def blogs_list(request):
# 	blogs = Blog.objects.all()
# 	page_number = request.GET.get('page')
# 	paginator = Paginator(blogs, 5)
# 	page = paginator.get_page(page_number)
	
# 	context = {'blogs': page1}
# 	return render(request, 'page/page1.html', context)


def list_blogs(request):
	blogs = Todo.objects.all().order_by('-id')
	q = request.GET.get('q', '')
	# получаем номер страницы на которую юзер хочет посмотреть
	page_number = request.GET.get('page')
	# если при этом есть поиск
	if q:
	# то отфильтруем
		orders = orders.filter(Q(title__icontains=q) | Q(assignee__name__icontains=q))
	# создаем объект Paginator и берем данные по номеру страницы
		paginator = Paginator(blogs, BLOGS_PER_PAGE)
		blogs = paginator.get_page(page_number)
	# дальше стандартный код - контекст и return
	pass