from django.shortcuts import render
from .forms import EmailForm
from .models import Email
from .spam_classifier import classify_email

def classify_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.is_spam = classify_email(email.subject, email.body)
            email.save()
            return render(request, 'result.html', {'email': email})
    else:
        form = EmailForm()
    return render(request, 'classify.html', {'form': form})