from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
	return render(request, 'pages/contact-form.html')


def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		contact = Contact(name=name, email=email, subject=subject, message=message)
		contact.save()
		messages.success(request, 'Form has been submitted successfully.')
		return redirect('/contact')