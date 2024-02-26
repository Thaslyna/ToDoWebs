from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm


# Create your views here.


def home(request):
    tasky = ToDo.objects.all()
    context = {'shw': tasky}
    if request.method == 'POST':
        task = request.POST.get('do', '')
        priority = request.POST.get('prio', '')
        date = request.POST.get('date', '')
        do_task = ToDo(do=task, prio=priority, date=date)
        do_task.save()
    return render(request, 'home.html', context)


def delete(request, delete_id):
    dota = ToDo.objects.get(id=delete_id)
    if request.method == 'POST':
        dota.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, update_id):
    data1 = ToDo.objects.get(id=update_id)
    data2 = ToDoForm(request.POST or None,instance=data1)
    if data2.is_valid():
        data2.save()
        return redirect('/')
    return render(request, 'edit.html', {'m': data1, 'f': data2})
