from django import forms
from .models import Startup

class StartupSubmissionForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = [
            'name',
            'description',
            'industry',
            'failure_reason',
            'lessons_learned',
            'founded_year',
            'closed_year',
            'logo',  # ✅ Add this
        ]
