from django.shortcuts import render, redirect
from .models import todo_list_app
from .form import CreateToDoForm


def home(request):
    return render(request, "home.html")


def list(request):
    todo = todo_list_app.objects.all()
    context = {"todo": todo}
    return render(request, "list.html", context)


def create(request):
    if request.method == "POST":
        todo = CreateToDoForm(request.POST)
        if todo.is_valid():
            todo.save()
            return redirect("home")
    else:
        todo = CreateToDoForm()
    context = {"todo": todo}
    return render(request, "create.html", context)


def done(request):
    return render(request, "done.html")


def delete(request,pk):
    todo=todo_list_app.objects.get(id=pk)
    todo.delete()
    return redirect('list')





