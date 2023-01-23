import random
import locale

from view_breadcrumbs import ListBreadcrumbMixin
from view_breadcrumbs import DetailBreadcrumbMixin

from django.shortcuts import render
from django.conf import settings
from django.utils.translation import gettext as _, get_language
from django.utils.functional import cached_property
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .cron import ex_rates_update
from .models import Quote
from .models import DesiredPosition

def roundSalary(positions):
   
    ex_rates_update()
    langCode = get_language()
   
    if (langCode == 'ru'):
        for position in positions:
            position.salary = '{0:,}'.format(int(round(position.salary_rub, -2))).replace(',', ' ')
    else:
        for position in positions:
            position.salary = '{0:,}'.format(int(round(position.salary_usd, -2)))

    return positions


def index(request):

    app_name = request.resolver_match.app_name

    quotes = Quote.objects.all()
    publicQuote = quotes[random.randint(0, quotes.count()-1)].text
    desiredPositions = roundSalary(DesiredPosition.objects.filter(isActive=True))

    context = {
        'left_title': settings.MEDIA_URL + 'content/left-title.jpg',
        'randomQuote': publicQuote,
        'myself': {
            'photo': settings.MEDIA_URL + 'content/photo.jpg',
            'name': 'Vladislav Sokolov'
        },
        'desiredPositions': desiredPositions,
        'app_name': app_name
    }
    return render(request, app_name + '/index.html', context)


class positionDetail(DetailBreadcrumbMixin, DetailView):

    model = DesiredPosition
    template_name = "main/position.html"
    breadcrumb_use_pk = True

    
    @cached_property
    def crumbs(self):
        return [(_("Desired position") + ": " + self.get_object().name, reverse("index"))]
    

    def get_context_data(self, **kwargs):

        app_name = 'main'
        position = self.get_object()

        context = super(positionDetail, self).get_context_data(**kwargs)        

        if (get_language() == 'ru'):
            position.salary = '{0:,}'.format(int(round(position.salary_rub, -2))).replace(',', ' ')
        else:
            position.salary = '{0:,}'.format(int(round(position.salary_usd, -2)))

        context['position']     = position
        context['positions']    = DesiredPosition.objects.all()
        context['app_name']     = app_name

        return context


class Positions(ListBreadcrumbMixin , ListView):
    model = DesiredPosition
    template_name = "main/crumbs.html"