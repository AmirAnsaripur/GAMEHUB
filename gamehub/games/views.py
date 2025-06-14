from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Review
from .forms import ReviewForm

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, id=pk)
    reviews = game.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()
            return redirect('game_detail', pk=pk.id)
    else:
        form = ReviewForm()

    return render(request, 'games/game_detail.html', {
        'game': game,
        'form': form,
        'reviews': reviews,
    })
