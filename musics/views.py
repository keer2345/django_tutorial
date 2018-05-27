# from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from musics.models import Music, fun_raw_sql_query, fun_sql_cursor_update
from musics.serializers import MusicSerializer

# def hello_view(request):
#     hello = "Nice to meet you!"
#     musics = Music.objects.all()
#     context = {'data': hello, 'musics': musics}
#     return render(request, 'index.html', context)


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    # /api/music/raw_sql_query/
    @list_route(methods=['get'])
    def raw_sql_query(self, request):
        song = request.query_params.get('song', None)
        music = fun_raw_sql_query(song=song)
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # /api/music/{pk}/sql_cursor_update/
    @detail_route(methods=['put'])
    def sql_cursor_update(self, request, pk=None):
        song = request.data.get('song', None)
        if song:
            music = fun_sql_cursor_update(song=song, pk=pk)
            return Response(music, status=status.HTTP_200_OK)
