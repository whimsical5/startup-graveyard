import random
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from startups.models import Startup

def get_latest_news():
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": "startup company AND (failed OR shutdown OR closed OR bankruptcy)",
            "domains": "techcrunch.com,wired.com,businessinsider.com,thenextweb.com",
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 6,
            "apiKey": "3ee44d505fb3442792c76c386e8e160d"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
    except Exception as e:
        print("News API Error:", e)
    return []

@login_required
def dashboard_view(request):
    recent_startups = Startup.objects.filter(is_approved=True).order_by('-created_at')[:5]

    startups = Startup.objects.filter(is_approved=True).order_by('industry', '-created_at')
    categories = {}
    for startup in startups:
        industry = startup.industry or "Uncategorized"
        categories.setdefault(industry, []).append(startup)

    quotes = [
        "“Failure is simply the opportunity to begin again, this time more intelligently.” — Henry Ford",
        "“Success is not final, failure is not fatal: It is the courage to continue that counts.” — Winston Churchill",
        "“I have not failed. I've just found 10,000 ways that won't work.” — Thomas Edison",
        "“Only those who dare to fail greatly can ever achieve greatly.” — Robert F. Kennedy",
        "“The road to success is paved with failure.” — Unknown",
        "“In every failure, there is a lesson.” — Anonymous"
    ]

    quote = random.choice(quotes)
    news_articles = get_latest_news()

    return render(request, 'registration/dashboard.html', {
        'user': request.user,
        'recent_startups': recent_startups,
        'quote': quote,
        'news_articles': news_articles,
        'categories': categories
    })


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')