from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Message, Comment
import datetime
import bcrypt

def index(request):
    return render(request, 'wall_app/login.html')

def login(request):
    result = User.objects.filter(email = request.POST['email']).values()
    if len(result)>0:
        if bcrypt.checkpw(request.POST['password'].encode(), result[0]['password'].encode()):
            request.session['first_name'] = result[0]['first_name']
            request.session['userid'] = result[0]['id']
            request.session["type"] = "login"
            return redirect('/wall')
    messages.error(request, 'Login Failed', extra_tags = 'login')
# can call by messages".error" --> if message.level == DEFAULT_MESSAGE_LEVELS.ERROR
    return redirect('/')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        request.session["first_name"] = request.POST["first_name"]
        request.session["type"] = "register"
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        this_user = User.objects.filter(email = request.POST['email']).values()
        request.session['userid']= this_user[0]['id']
        return redirect('/wall')

def wall(request):

    print(Message.objects.get(id=1).messagepuser.first_name)
    if 'userid' in request.session:
        context = {
            "all_messages" : Message.objects.all().order_by('-id'),
            "all_comments" : Comment.objects.all(),
            "datetime1": datetime.datetime.now() - datetime.timedelta(minutes=20),
        }
        return render(request, 'wall_app/wall.html',context)
    else:
        messages.error(request, 'NOT LOGGED IN', extra_tags = 'login')
        return redirect('/')

def logoff(request):
    request.session.clear()
    return redirect('/')

def postmessage(request):
    Message.objects.create(message = request.POST['message'], messagepuser = User.objects.get(id= request.session['userid']))
    return redirect('/wall')

def postcomment(request):
    Comment.objects.create(comment = request.POST['comment'], commentpmessage = Message.objects.get(id=request.POST['messageid']), commentpuser = User.objects.get(id= request.session['userid']))
    return redirect('/wall')

def deletemessage(request):
    Message.objects.get(id=request.POST['messageid']).delete()
    return redirect('/wall')