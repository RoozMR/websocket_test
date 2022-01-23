from django.shortcuts import render

# Create your views here.
# def index_view(request):
#     return render(request, 'index.html', {
#         'rooms': Room.objects.all(),
#     })
#
#
# def room_view(request, room_name):
#     chat_room, created = Room.objects.get_or_create(name=room_name)
#     return render(request, 'room.html', {
#         'room': chat_room,
#     })


# def index(request):
#     return render(request, 'index.html')


# def room(request, room_name):
#     return render(request, 'room.html', {
#         'room_name': room_name
#     })


def echo(request):
    return render(request, 'echo.html')