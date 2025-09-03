from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Coin, GlobalRank
from .forms import GlobalRankForm

# FUNCTION BASED VIEWS
def home(request):
    coins = Coin.objects.all()
    if request.user.is_authenticated:
        coins = coins.filter(owner=request.user)
        total_coins = coins.count()
        total_value = sum([coin.value for coin in coins])
        countries = coins.values_list('country', flat=True)
        unique_countries = len(set(countries))
        featured_coins = coins.order_by('-value')[:3]
    else:
        total_coins = 0
        total_value = 0
        unique_countries = 0
        featured_coins = Coin.objects.none()
    return render(request, 'home.html', {
        'total_coins': total_coins,
        'total_value': total_value,
        'unique_countries': unique_countries,
        'featured_coins': featured_coins,
    })

def about(request):
    return render(request, 'about.html')

def coin_index(request):
    coins = Coin.objects.all()
    if request.user.is_authenticated:
        coins = coins.filter(owner=request.user)
    return render(request, 'coins/index.html', { 'coins': coins })

def coin_detail(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    globalrank_form = GlobalRankForm(initial={'coin': coin})
    return render(request, 'coins/detail.html', { 'coin': coin, 'globalrank_form': globalrank_form })

@login_required
def add_globalrank(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    form = GlobalRankForm(request.POST)
    if form.is_valid():
        new_globalrank = form.save(commit=False)
        new_globalrank.coin = coin
        new_globalrank.save()
    return redirect('coin-detail', coin_id=coin_id)

class CoinCreate(LoginRequiredMixin, CreateView):
    model = Coin
    fields = ['name','year','country','description','value','image']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CoinUpdate(LoginRequiredMixin, UpdateView):
    model = Coin
    fields = ['year', 'country', 'description', 'value', 'image']
    def get_queryset(self):
        return Coin.objects.filter(owner=self.request.user)

class CoinDelete(LoginRequiredMixin, DeleteView):
    model = Coin
    success_url = '/coins/'
    def get_queryset(self):
        return Coin.objects.filter(owner=self.request.user)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
