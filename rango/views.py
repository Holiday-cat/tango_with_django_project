from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse
from rango.forms import CategoryForm 
from django.shortcuts import redirect

def add_category(request):
	form = CategoryForm()


	if request.method == 'POST':
		form = CategoryForm(request.POST)


		if form.is_valid():
			form.save(commit=True)  
			return redirect('/rango/') 
		else:
			print(form.errors) 
			

	return render(request, 'rango/add_category.html', {'form': form})


def index(request):
    
    
	category_list = Category.objects.order_by('-likes')[:5] 

	context_dict = {}
	context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
	context_dict['categories'] = category_list

	return render(request, 'rango/index.html', context=context_dict)
def show_category(request, category_name_slug):

    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)


        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

