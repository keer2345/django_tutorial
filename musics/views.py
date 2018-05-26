from django.shortcuts import render

from musics.models import Music


def hello_view(request):
    hello = "Nice to meet you!"
    musics = Music.objects.all()
    context = {'data': hello, 'musics': musics}
    return render(request, 'index.html', context)
