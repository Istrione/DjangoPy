#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
            'map': 'https://yandex.ru/maps/org/petropavlovskaya_krepost/146720535721/?utm_medium=mapframe&utm_source=maps',
            'city': 'Санкт-Петербург',
            'phone': '+7-999-11-11111',
            'email' : 'geeklab@spb.ru',
            'adress': 'территория Петропавловская крепость, 3Ж'
        },            {
            'map': 'https://yandex.ru/maps/org/kazanskiy_kreml/95813866834/?utm_medium=mapframe&utm_source=maps',
            'city': 'Казань',
            'phone': '+7-999-22-22222',
            'email' : 'geeklab@kz.ru',
            'adress': 'территория Кремль, 11, Казань, Республика Татарстан, Россия'
        },            {
            'map': 'https://yandex.ru/maps/org/sobor_pokrova_presvyatoy_bogoroditsy_na_rvu/175159255687/?utm_medium=mapframe&utm_source=maps',
            'city': 'Москва',
            'phone': '+7-999-33-33333',
            'email' : 'geeklab@msk.ru',
            'adress': 'Красная площадь, 7, Москва, Россия'
        }
        ]
        return context_data

class CourserListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость',
                'preview': 'Превью к новости',
                'date': '2022-01-01'
            }, {
                'title': 'Новость',
                'preview': 'Превью к новости',
                'date': '2022-01-01'
            }, {
                'title': 'Новость',
                'preview': 'Превью к новости',
                'date': '2022-01-01'
            }, {
                'title': 'Новость',
                'preview': 'Превью к новости',
                'date': '2022-01-01'
            }, {
                'title': 'Новость',
                'preview': 'Превью к новости',
                'date': '2022-01-01'
            }
        ]
        context_data["range"] = range(5)
        return context_data
