# from django.shortcuts import render
from rest_framework import viewsets

from musics.models import Music
from musics.serializers import MusicSerializer

# def hello_view(request):
#     hello = "Nice to meet you!"
#     musics = Music.objects.all()
#     context = {'data': hello, 'musics': musics}
#     return render(request, 'index.html', context)


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
