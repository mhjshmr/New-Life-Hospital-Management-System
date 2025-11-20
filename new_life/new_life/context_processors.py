from patient.models import Patient
from doctor.models import Doctor

def theme(request):
    # Optimize this or you are a noob.
    if 'is_dark_theme' in request.session:
        is_dark_theme = request.session.get('is_dark_theme')
        return {'is_dark_theme': is_dark_theme}
    
    return {'is_dark_theme': False}

def user_to_patient(request):
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
        return {'patient': patient}
    except Exception as e:
        return {'patient': []}

def user_to_doctor(request):
    user = request.user
    try:
        patient = Doctor.objects.get(user=user)
        return {'doctor': patient}
    except Exception as e:
        return {'doctor': []}