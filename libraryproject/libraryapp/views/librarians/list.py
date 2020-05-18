from django.shortcuts import render
from libraryapp.models import Librarian
from django.contrib.auth.decorators import login_required



@login_required
def librarian_list(request):
    if request.method == 'GET':
        all_librarians = Librarian.objects.all()

        template = 'librarians/list.html'
        context = {
            'all_librarians': all_librarians
        }

        return render(request, template, context)