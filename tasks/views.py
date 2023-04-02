from random import choice
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from tasks.models import *

import pickle

NUMBER_OF_GAMES = 10

plane_groups = ['p1', 
                'p2', 
                'pm', 'pg', 'cm', 'p2mm', 'p2mg', 'p2gg', 'c2mm', 
                'p4', 'p4mm', 'p4gm', 
                'p3', 'p3m1', 'p31m', 'p6', 'p6mm'
                ]

@login_required
def task1play(request):
    task = Task1Play.objects.filter(user=request.user).latest('start')
    if request.method == "POST":
        if request.is_ajax():
            answer = request.POST.get('pg')
            right_answer = request.POST.get('right_answer')
            if answer == right_answer:
                task.right += 1
                if task.right >= NUMBER_OF_GAMES:
                    task.end = datetime.now()
                    task.finished = True
                    task.duration = task.end - task.start
                task.save()
                return redirect('task1play')
            else:
                task.wrong += 1
                task.save()
                return JsonResponse({'right':task.right, 'wrong': task.wrong})
    else:
        if task.right >= NUMBER_OF_GAMES:
            finished_tasks = Task1Play.objects.filter(user=request.user).filter(finished=True)
            return render(request,'task1complete.html', 
                           {'task':task,
                            'num_of_games':NUMBER_OF_GAMES,
                            'finished_tasks':finished_tasks})
        return render(request, 'task1play.html', 
                {'group': choice(plane_groups), 
                 'plane_groups':plane_groups,
                 'right':task.right,
                 'wrong':task.wrong,
                 'start':task.start,
                })

@login_required
def task1complete(request):
    return render(request, 'task1complete.html')

@login_required
def task1_view(request):
    return render(request, 'task1.html', { 'group': choice(plane_groups), 'plane_groups':plane_groups})

@login_required
def packmol(request):
    molecules = pickle.load(open('/home/huk/apps/tgk/project/molecules.pkl','rb'))
    k = choice(list(molecules.keys()))
    molecule = molecules[k]
    return render(request, 'packmol.html', { 
            'group': choice(plane_groups), 
            'plane_groups':plane_groups,
            'molecule': molecule,
            'chebi_id': k,
            })

@login_required
def task1replay(request):
    Task1Play.objects.create(user=request.user)
    return redirect('task1play')

@login_required
def scoreboard(request):
    all_tasks = Task1Play.objects.filter(finished=True) 
    return render(request, 'scoreboard.html', { 'tasks':all_tasks})
