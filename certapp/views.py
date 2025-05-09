from django.shortcuts import render, redirect
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from . models import Enrolment
from django.db.models import Sum



def index(request):
    code = request.GET.get('code')
    if code:
        return redirect('verify_certificate', code=code)
    return render(request, 'index.html')

def verify_certificate(request, code):
    try:
        enrolment = Enrolment.objects.using('mysql_db').select_related('user', 'cohort').get(certificate_code=code)
        print(enrolment.id)
        return render(request, 'certificate_verification.html', {
            'enrolment': enrolment,
            'valid': True,
            
        })
    except Enrolment.DoesNotExist:
        return render(request, 'certificate_verification.html', {
            'valid': False,
            'code': code
        })





# def verify_certificate(request, code):
#     try:
#         enrolment = Enrolment.objects.select_related('user', 'cohort').get(certificate_code=code)
#         return render(request, 'certificate_verification.html', {
#             'enrolment': enrolment,
#             'valid': True
#         })
#     except Enrolment.DoesNotExist:
#         return render(request, 'certificate_verification.html', {
#             'valid': False,
#             'code': code
#         })






