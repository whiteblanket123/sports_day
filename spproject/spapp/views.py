from django.shortcuts import render, get_object_or_404
from .models import Event
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def test1d(request):
    Information = Event.objects.filter(grade=1)
    return render(request,'sportsday/main.html', {'Information':Information})

                                       
def test2d(request):
    Information = Event.objects.filter(grade=2)
    return render(request,'sportsday/main.html', {'Information':Information})

def test3d(request):
    Information = Event.objects.filter(grade=3)
    return render(request,'sportsday/main.html', {'Information':Information})

def input_page(request):
    return render (request, 'sportsday/input.html')

def submit_input(request):
    if request.method == 'POST':
        grade = int(request.POST.get('grade', 0))  # 기본값을 0으로 설정
        classs = request.POST.get('classs')
        event = request.POST.get('event')
        score = request.POST.get('score')

        information = get_object_or_404(Event, grade=grade, classs=classs)
        
        event_scores = {
            'relay': 'relay',
            'performance': 'performance',
            'ssireum': 'ssireum',
            'basketball': 'basketball',
            'soccer': 'soccer',
            'dodge_ball': 'dodge_ball',
            'jump_rope': 'jump_rope'
        }

        if event in event_scores:
            setattr(information, event_scores[event], score)
        else:
            return render(request, 'error_template.html', {'error': 'Invalid event type'})

        information.save()

        if grade in [1, 2, 3]:
            return HttpResponseRedirect(reverse(f'{grade}grade'))
        else:
            return HttpResponse("잘못된 학년입니다.", status=400)
    
    return HttpResponse("잘못된 요청입니다.", status=400)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)