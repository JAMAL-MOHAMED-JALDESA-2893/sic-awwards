from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def setUp(self):
        self.benard= User(username = 'Benard',email = 'benardakaka484@gmail.com')
        self.benard = Profile(user = Self.benard,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='jan,28.202')

    def test_instance(self):
        self.assertTrue(isinstance(self.benard,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.benard.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',projectscreenshot = 'test.jpg',description = 'testD',user = peris,projecturl = 'https://test.com',datecreated='Dec,01.2020')


    def test_save_project(self):
        self.new_post.save_project()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1)    

    
