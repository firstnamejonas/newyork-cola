from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm


class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client = Client()
        if not hasattr(self.user, 'userprofile'):
            self.profile = UserProfile.objects.create(user=self.user)
        else:
            self.profile = self.user.userprofile


    def test_user_profile_creation(self):
        """
        Test if a user profile is created for a new user.
        """
        self.assertEqual(UserProfile.objects.count(), 1)

    def test_user_profile_str_method(self):
        """
        Test the string representation of user profiles.
        """
        self.assertEqual(str(self.profile), self.user.username)

    def test_profile_view(self):
        """
        Test if the profile view returns a 200 status code.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_update(self):
        """
        Test if the profile update form updates the user profile.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {
            'default_street_address1': '123 Street',
            'default_street_address2': '',
            'default_postcode': '12345',
            'default_town_or_city': 'City',
            'default_country': 'US',
            'default_county': 'County',
        }
        form = UserProfileForm(data, instance=self.profile)
        self.assertTrue(form.is_valid())
        form.save()
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.default_street_address1, '123 Street')
