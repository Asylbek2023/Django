from django.http import HttpResponse


# установка куки
def set(request):
    username = request.GET.get('username', 'Undefined')
    response = HttpResponse(f"Hello{username}")
    response.set_cookie('username', username)
    return response

#получение куки
def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f"Hello{username}")
