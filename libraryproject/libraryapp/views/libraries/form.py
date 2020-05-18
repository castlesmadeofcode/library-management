from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library


def get_libraries():
    return Library.objects.all()

@login_required
def library_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'libraries/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)

        