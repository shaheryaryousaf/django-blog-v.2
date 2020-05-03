from django.shortcuts import render
from posts.models import Category, Post

def index(request):
	categories = Category.objects.all()
	posts = Post.objects.filter(is_published=True).order_by('-created_at')
	context = {
		'categories': categories,
		'posts': posts
	}
	return render(request, 'pages/index.html', context)

def about(request):
	return render(request, 'pages/about.html')

