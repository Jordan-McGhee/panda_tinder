from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_pandas": Panda.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == "GET":
        return redirect("/")

    new_panda = Panda.objects.create(name=request.POST['name'], age=request.POST['age'], favorite_food=request.POST['favorite_food'], knows_kungfu=request.POST['knows_kungfu'])

    return redirect('/')

def panda_profile(request, panda_id):
    context = {
        "all_pandas": Panda.objects.all(),
        "this_panda": Panda.objects.get(id=panda_id)
    }
    return render(request, "panda_profile.html", context)


def create_post(request):
    if request.method== "POST":
        this_panda = Panda.objects.get(id=request.POST['hidden_input'])
        
        # this_panda = Panda.objects.get(id=panda_id)
        # can do it this way ^ if you pass panda_id in arguments

        new_post = Post.objects.create(content=request.POST['panda_post'], author=this_panda)
        # print(new_post.content)
        return redirect(f"/panda/{this_panda.id}")
    return redirect("/")

def create_date(request):
    if request.method=="POST":
        this_panda = Panda.objects.get(id=request.POST["hidden_id"])
        other_panda = Panda.objects.get(id=request.POST['date'])

        new_date = Date.objects.create(date=request.POST['when'], location=request.POST['where'])
        new_date.pandas_on_date.add(this_panda, other_panda)
        
        # print(new_date.location)
        
        return redirect(f"/panda/{this_panda.id}")
    return redirect("/")