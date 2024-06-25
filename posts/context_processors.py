from django.utils import timezone

def current_date(request):
    return {"current_date": timezone.now()}