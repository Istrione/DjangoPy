from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse

from authapp.models import User
from mainapp.models import News


class StaticPagesSmokeTest(TestCase):
    def test_page_index_open(self):
        url = reverse('mainapp:index')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_contacts_open(self):
        url = reverse('mainapp:contacts')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)


class NewsTestCase(TestCase):

    def setUp(self) -> None:
        for i in range(10):
            News.object.create(
                title=f'News1{i}',
                intro=f'Intro{i}',
                body=f'Body{i}'
            )

        User.objecs.create_superuser(username='django', password='geekbrains')
        self.client_with_auth = Client()
        auth_url = reverse('authapp:login')
        self.client_with_auth.post(
            auth_url,
            {'username': 'django', 'password': 'geekbrains'}
        )

    def test_open_page(self):
        url = reverse('mainapp:news')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_failed_add_by_anonym(self):
        url = reverse('mainapp:news_create')

        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_create_news_item_by_admin(self):

        news_count = News.objects.all().count()

        url = reverse('mainapp:news_create')
        result = self.client_with_auth.post(
            url,
            data={
                'title': 'Title news',
                'intro': 'Test intro',
                'body': 'Test body'
            }
        )

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

        self.assertEqual(News.objects.all().count(), news_count + 1)