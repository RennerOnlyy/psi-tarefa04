from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-data_criacao')
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            Tarefa.objects.create(titulo=titulo)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('lista_tarefas')

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')
