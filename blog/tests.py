from django.test import TestCase
from django.test.client import Client


class Main_functionsTest(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def user_login_and_logout_test(self):
        self.client = Client()
        login_response = self.client.login(username='vadim', password='ghjcnj41285')
        print('response={}'.format(login_response))
        self.assertEqual(login_response, True)
        logout_response = self.client.logout(username='vadim', password='ghjcnj41285')
        self.assertEqual(logout_response, True)

    def creating_post_test(self):
        self.client = Client()
        response = c.post('posts/addpost/', {'title': 'Just title', 'text': 'This is a text of our post'})
        self.assertEqual(response, 200)


class TemplateTest(TestCase):
    def main_page_template(self):
        self.client = Client()
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'post_list.html')

    def post_by_id_test(self):
        self.client = Client()
        response = self.client.get('posts/1/')
        self.assertTemplateUsed(response, 'post_list.html')
        print('ok = {}'.format(self.assertTemplateUsed(response, 'post_by_id.html')))
