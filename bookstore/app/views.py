from django.shortcuts import render, redirect
from .forms import login
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'app_templates/index.html')


# def form(request):
# 	if request.method =="POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		if book.objects.filter(username=user_name).exists():
# 			user=book.objects.get(username=user_name)
# 			if password==name.password:
# 				request.session[name.username]=name.user_name
# 				return redirect('form',pk=name.id)
# 			else:
# 				messages.error(request,'Password not correct')
# 				return redirect('form_redirect')
# 		else:
# 			messages.error(request,'Username not correct')
# 			return redirect('form_redirect')
# 	else:
# 		return render(request,'app_templates/form.html')
def app(request):
    return HttpResponse("ok")

def index2(request):
	return render(request,'app_templates/index2.html')

def form(request):
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']

	else:
		form = login()
		return render(request,'app_templates/form.html',{'form':form})
