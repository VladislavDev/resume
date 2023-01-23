from django.shortcuts import render
from .models import KeySkill, KeySubSkill


def index(request):
   context = {
      'skill_list': KeySkill.objects.all(),
      'sub_skill_list': KeySubSkill.objects.all()
   }
   return render(request, 'exp/index.html', context)