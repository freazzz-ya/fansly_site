from django.shortcuts import render


def list_view(request):
    return render(request, "index.html")
