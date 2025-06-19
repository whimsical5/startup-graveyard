from django.shortcuts import render, get_object_or_404, redirect
from .models import Startup
from .forms import StartupSubmissionForm
from django.utils.text import slugify

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug=slug)
    return render(request, 'startups/startup_detail.html', {'startup': startup})

def submission_thanks(request):
    return render(request, 'startups/submission_thanks.html')

def startup_list_grouped(request):
    startups = Startup.objects.filter(is_approved=True).order_by('industry', '-created_at')

    categories = {}
    for startup in startups:
        industry = startup.industry or "Uncategorized"
        categories.setdefault(industry, []).append(startup)

    return render(request, 'startups/startup_magazine.html', {'categories': categories})

def submit_startup(request):
    if request.method == 'POST':
        form = StartupSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            startup = form.save(commit=False)
            startup.slug = slugify(startup.name)
            startup.is_approved = False
            startup.save()
            return redirect('submission_thanks')
    else:
        form = StartupSubmissionForm()
    return render(request, 'startups/startup_submit.html', {'form': form})