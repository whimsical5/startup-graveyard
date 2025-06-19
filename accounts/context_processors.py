from startups.models import Startup

def recent_startups(request):
    return {
        'recent_startups': Startup.objects.filter(is_approved=True).order_by('-created_at')[:20]
    }
