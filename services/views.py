import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import WaitlistEntry

def landing(request):
    return render(request, 'index.html')

@csrf_exempt
def waitlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            role = data.get('role', 'client')
            skill = data.get('skill', '').strip()

            if not name or not email:
                return JsonResponse({'success': False, 'error': 'Name and email are required.'})

            if WaitlistEntry.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'error': 'This email is already on the waitlist.'})

            WaitlistEntry.objects.create(name=name, email=email, role=role, skill=skill)

            # Send welcome email
            send_mail(
                subject='You\'re on the PlugZone waitlist 🎉',
                message=f'''Hi {name},

Thanks for joining the PlugZone waitlist!

We're building the easiest way to find and book trusted local service providers in Nigeria — barbers, chefs, nail techs, house agents and more.

You'll be among the first to know when we launch in Lagos, Abuja and Port Harcourt.

Stay tuned,
The PlugZone Team
''',
                from_email=None,
                recipient_list=[email],
                fail_silently=True,
            )

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request.'})