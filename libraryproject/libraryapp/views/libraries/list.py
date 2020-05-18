from django.shortcuts import render, redirect, reverse
from libraryapp.models import Book, Library
from django.contrib.auth.decorators import login_required


@login_required
def library_list(request):
    if request.method == 'GET':
        all_libraries = Library.objects.all()

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)
      
    elif request.method == 'POST':
        form_data = request.POST
    
        
        new_library = Library.objects.create(
            title = form_data['title'],
            address = form_data['address']
        )
        

        return redirect(reverse('libraryapp:libraries'))