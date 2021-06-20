from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .forms import PhoneNumberForm
from .models import PhoneNumber
from django.core.serializers import serialize
import json
from twilio.twiml.voice_response import VoiceResponse, Gather
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data.get('phn_no')
            print(number)
            form.save()
            return HttpResponse('got tha')
    form = PhoneNumberForm()
    return render(request,'homepage.html',context={'form' : form})

# def api(request,key):
#     if request.method == "GET":
#         if key == 'abc':
#             foo = PhoneNumber.objects.all()
#             data = serialize('json',foo,fields=('phn_no'))
#             return HttpResponse(data,content_type='application/json')
#         data = {'response' : 'api key not correct'}
#         data = json.dumps(data)
#         return HttpResponse(data,content_type='application/json')
@csrf_exempt
def voice(request):
    resp = VoiceResponse()
    str1 = "Please take your medicines,"
    resp.say(str1,language='en-IN')
    gather = Gather(num_digits=1, action='/gather')
    gather.say(",To confirm you have took medicines please press 1",language='en-IN')
    resp.append(gather)
    resp.redirect('/voice')
    return HttpResponse(str(resp))
@csrf_exempt
def gather(request):
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()
    # If Twilio's request to our app included already gathered digits,
    # process them

    if request.POST.get('Digits') is not None:
        print('oks')
        # Get which digit the caller chose
        choice = request.POST.get('Digits')

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('Thank you for confirming , Take Care, Bye',language='en-IN')
            return HttpResponse(str(resp))
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.",language='en-IN')

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    # resp.redirect('/voice')

    return HttpResponse(str(resp))

