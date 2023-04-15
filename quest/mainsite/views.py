import logging

from django.shortcuts import render, get_object_or_404

from .models import Team, Puzzle
from .forms import AnswerForm

def index(request, puzzle_pk):
    if not request.session or not request.session.session_key:
        request.session.save()

    puzzle = get_object_or_404(Puzzle, pk = puzzle_pk)
    code = request.GET.get('code')

    if code != puzzle.secret_code:
        return render(
            request,
            'error.html',
            {
                'error_text': "Неверный код доступа. Скорее всего, вы не сканировали QR"
            }
        )

    if not Team.objects.filter(session=request.session.session_key).exists() and puzzle.puzzle_id != 1:
        return render(
            request,
            'error.html',
            {
                'error_text': "Скорее всего, вы зашли не с телефона команды или еще не начали квест. " + \
                     "Вернитесь на первую точку."
            }
        )
    
    warning = False
    
    if puzzle.puzzle_id == 1 and not Team.objects.filter(session=request.session.session_key).exists():
        team = Team.objects.create(session=request.session.session_key, position=1)
        warning = True
    else:
        team = Team.objects.get(session=request.session.session_key)

    if team.position != puzzle.puzzle_id:
        return render(
            request,
            'error.html',
            {
                'error_text': 'Вы перепутали порядок. Вернитесь на нужную точку. Подсказка:',
                'tip': Puzzle.objects.get(pk = team.position).tip_this
            }
        )

    return render(
        request,
        'index.html',
        {
            'error': False,
            'letters': team.letters,
            'puzzle': puzzle,
            'warning': warning,
            'team': team
        }
    )


def answer(request, puzzle_pk):
    if not request.session or not request.session.session_key:
        request.session.save()

    if request.method != 'POST':
        form = AnswerForm()

    if not Team.objects.filter(session=request.session.session_key).exists():
        return render(
            request,
            'error.html',
            {
                'error_text': "Скорее всего, вы зашли не с телефона команды или еще не начали квест. " + \
                     "Ссылка в форме регистрации на точки CSTATI."
            }
        )
    
    form = AnswerForm(request.POST)
    team = Team.objects.get(session=request.session.session_key)
    puzzle = get_object_or_404(Puzzle, pk = puzzle_pk)

    if team.position != puzzle.puzzle_id:
        return render(
            request,
            'error.html',
            {
                'error_text': 'Вы перепутали порядок. Вернитесь на нужную точку. Подсказка:',
                'tip': Puzzle.objects.get(pk = team.position).tip_this
            }
        )
    
    if not form.is_valid():
        return render(
            request,
            'index.html',
            {
                'error': False,
                'letters': team.letters,
                'puzzle': puzzle,
                'team': team
            }
        )

    if form.cleaned_data['answer'] != puzzle.answer:
        return render(
            request,
            'index.html',
            {
                'error': True,
                'letters': team.letters,
                'puzzle': puzzle,
                'team': team
            }
        )
    
    team.letters.add(puzzle.letter)

    if team.position + 1 == 10:
        return render(
            request,
            'final.html',
            {
                'letters': team.letters,
                'team': team
            }
        )
    
    team.position = puzzle.puzzle_id + 1
    team.save()
    
    puzzle = get_object_or_404(Puzzle, puzzle_id = team.position)

    return render(
            request,
            'right.html',
            {
                'letters': team.letters,
                'puzzle': puzzle,
                'team': team
            }
        )


def error_404(request, exception):
   context = {}
   
   return render(request,'404.html', context)