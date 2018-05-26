from django.shortcuts import render


def hello_view(request):
    hello = "Nice to meet you!"
    context = {'data': hello}
    return render(request, 'index.html', context)
