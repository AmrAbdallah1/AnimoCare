from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from AnimoSound.functions import ANN_print_prediction
from django.http import JsonResponse
import random
from django.core.files.storage import FileSystemStorage



angry =  random.choice(['/fold1/Angr(425).wav',
         '/fold1/Angr(360).wav',
         '/fold1/Angr(400).wav',
         '/fold1/Angr(401).wav',
         '/fold1/Angr(426).wav'])

defense = random.choice(['/fold2/Defense(274).wav',
           '/fold2/Defense(275).wav',
           '/fold2/Defense(280).wav',
           '/fold2/Defense(320).wav',
           '/fold2/Defense(325).wav'])

fighting = random.choice(['/fold3/Fight(490).wav',
            '/fold3/Fight(495).wav',
            '/fold3/Fight(499).wav',
            '/fold3/Fight(500).wav',
            '/fold3/Fight(501).wav'])

happy = random.choice(['/fold4/Hpy(420).wav',
         '/fold4/Hpy(489).wav',
         '/fold4/Hpy(490).wav',
         '/fold4/Hpy(500).wav',
         '/fold4/Hpy(510).wav'])

HuntingMind = random.choice(['/fold5/HuntMnd(333).wav',
               '/fold5/HuntMnd(335).wav',
               '/fold5/HuntMnd(400).wav',
               '/fold5/HuntMnd(410).wav',
               '/fold5/HuntMnd(415).wav'])

mating = random.choice(['/fold6/Mate(340).wav',
          '/fold6/Mate(350).wav',
          '/fold6/Mate(351).wav',
          '/fold6/Mate(399).wav',
          '/fold6/Mate(420).wav'])

MotherCalling = random.choice(['/fold7/MCall(700).wav',
                 '/fold7/MCall(709).wav',
                 '/fold7/MCall(710).wav',
                 '/fold7/MCall(739).wav',
                 '/fold7/MCall(740).wav'])

paining = random.choice(['/fold8/Pain(395).wav',
           '/fold8/Pain(400).wav',
           '/fold8/Pain(409).wav',
           '/fold8/Pain(410).wav',
           '/fold8/Pain(484).wav'])

resting = random.choice(['/fold9/Rest(377).wav',
           '/fold9/Rest(397).wav',
           '/fold9/Rest(398).wav',
           '/fold9/Rest(399).wav',
           '/fold9/Rest(420).wav'])

warning = random.choice(['/fold10/Warn(280).wav',
           '/fold10/Warn(297).wav',
           '/fold10/Warn(340).wav',
           '/fold10/Warn(352).wav',
           '/fold10/Warn(353).wav'])



audio_test = [angry, defense, fighting, happy,
              HuntingMind, mating, MotherCalling,
              paining, resting, warning]



angry_emoji = "\U0001F620"
defense_emoji = "\U0001F624"
fighting_emoji = "\U0001F92C"
happy_emoji = "\U0001F604"
HuntingMind_emoji = "\U0001F60B"
mating_emoji = "\U0001F60D"
mothercall_emoji = "\U0001F408"
paining_emoji = "\U0001F912"
resting_emoji = "\U0001F634"
warning_emoji = "\U0001F631"




@csrf_exempt
@api_view(['GET'])
def Get_Emotion(request):
    
    random_sound = random.choice(audio_test)
    audio_dataset_path = "D:/Amr's Back End/audio"
    audio_path = audio_dataset_path + random_sound
    
    Emo = ANN_print_prediction(audio_path)

    def emoji_prediction():  
       if Emo == "Angry":
                 return "\U0001F620"
       elif Emo == "Defense":
                 return "\U0001F624"
       elif Emo == "Fighting":
                 return "\U0001F92C"
       elif Emo == "Happy":
                 return "\U0001F604"
       elif Emo == "HuntingMind":
                 return "\U0001F60B"
       elif Emo == "Mating":
                 return "\U0001F60D"
       elif Emo == "MotherCall":
                 return "\U0001F408"
       elif Emo == "Paining":
                 return "\U0001F912"
       elif Emo == "Resting":
                 return "\U0001F634"
       elif Emo == "Warning":
                 return "\U0001F631"
       else:
                 return "not defined"
       
    get_emoji = emoji_prediction()
    
    return JsonResponse({"Translation":'My emotion is ... ' + Emo + " " + get_emoji})








@csrf_exempt
@api_view(['POST'])
def upload_files(request):
    if request.method == 'POST':
        myfile = request.FILES['wavfile']
        fs = FileSystemStorage(location='sound test')
        filename = fs.save(myfile.name, myfile)
        audio_path = 'sound test/' + str(filename)
        Emo = ANN_print_prediction(audio_path)
        
        def emoji_test():
              if Emo == "Angry":
                 return "\U0001F620"
              elif Emo == "Defense":
                 return "\U0001F624"
              elif Emo == "Fighting":
                 return "\U0001F92C"
              elif Emo == "Happy":
                 return "\U0001F604"
              elif Emo == "HuntingMind":
                 return "\U0001F60B"
              elif Emo == "Mating":
                 return "\U0001F60D"
              elif Emo == "MotherCall":
                 return "\U0001F408"
              elif Emo == "Paining":
                 return "\U0001F912"
              elif Emo == "Resting":
                 return "\U0001F634"
              elif Emo == "Warning":
                 return "\U0001F631"
              else:
                 return "not defined"
              
              
        emoji = emoji_test()

        return JsonResponse({"Translation":'My emotion is ... ' + Emo + " " + emoji})
        
    return Response({
        "Value":"Error"})





 











# Create your views here.








