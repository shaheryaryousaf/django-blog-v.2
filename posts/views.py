from django.shortcuts import render
from .models import Category, Post


def index(request, slug):
	post = Post.objects.get(slug=slug)
	categories = Category.objects.all()
	posts = Post.objects.all().filter(is_published=True)
	context = {
		'post': post,
		'categories': categories,
		'posts': posts
	}
	return render(request, 'posts/single.html', context)
	pass


def category(request, slug):
	category = Category.objects.get(slug=slug)
	cposts = Post.objects.filter(category=category.id).filter(is_published=True)
	categories = Category.objects.all()
	posts = Post.objects.all().filter(is_published=True)
	context = {
		'category': category,
		'cposts': cposts,
		'categories': categories,
		'posts': posts
	}
	return render(request, 'posts/category.html', context)
	pass


def search(request):
	queryset_list = Post.objects.all()
	categories = Category.objects.all()
	posts = Post.objects.filter(is_published=True)

	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

	context = {
		'sposts': queryset_list,
		'categories': categories,
		'posts': posts,
		'keywords': keywords
	}
	return render(request, 'posts/search.html', context)




