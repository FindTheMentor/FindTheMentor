from django.utils.translation import activate
from django.test import TestCase
from django.core.urlresolvers import reverse
 
 
class TestHomePage(TestCase):
 
    def test_uses_index_template(self):
        activate('en-us')
	response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "FindTheMentor/index.html")
 
    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")
