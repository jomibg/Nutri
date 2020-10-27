from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestAuth(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass",is_superuser=True,is_staff=True)
    def setUp(self):
        self.client=Client()
    def test_email_backend(self):
        data={'username':'juliana@dev.io','password':'some_pass'}
        response=self.client.post('/accounts/login',data=data)
        self.assertEqual(response.status_code,301)



