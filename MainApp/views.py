from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    context = {
        'pagename': 'Информация о сниппете',
        'snippet': snippet
    }
    return render(request, 'pages/snippet_detail.html', context)


def snippet_create(request):
    if request.method == "POST":
        form_data = request.POST
        snippet = Snippet(
            name=form_data["name"],
            lang=form_data["lang"],
            code=form_data["code"],
        )
        snippet.save()
        return redirect('snippets-list')


