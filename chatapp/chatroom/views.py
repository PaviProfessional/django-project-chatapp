from django.shortcuts import render,redirect
from chatroom.models import Room,Message
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):                     #collect room name
    username= request.GET.get('username')    # get username from url request
    room_details=Room.objects.get(name=room)   #get a room name from database 
    return render(request,'room.html',{
        'username':username,
        'room':room,
        'room_details':room_details
    })                                      # sent a room detalis to html

def checkview(request):                                # this check view is check is the room is avalible or not
    room= request.POST['room_name']
    username= request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message=request.POST['message']
    username=request.POST['username']  
    room_id=request.POST['room_id']

    new_message=Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully!')


def getMessages(request,room):
    room_details=Room.objects.get(name=room)

    messages=Message.objects.filter(room__icontains=room_details.id)    # here we will filter the particular room id
    return JsonResponse({"messages":list(messages.values())})