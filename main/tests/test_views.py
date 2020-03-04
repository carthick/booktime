from django.test import TestCase
from main import forms
from django.urls import reverse


# Create your tests here.

from django.test import TestCase
class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')
    def test_about_us_page_works(self):
         response = self.client.get("/about-me/")
         self.assertEqual(response.status_code,200)
         self.assertTemplateUsed(response, 'about_me.html')
         self.assertContains(response, 'Passion')
    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_me"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')
        self.assertContains(response, 'BookTime')
        self.assertIsInstance(
            response.context["form"], forms.ContactForm
        )