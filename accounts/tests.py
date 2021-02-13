from django.test import TestCase
from django.contrib.auth import get_user_model


class TestCustomUser(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@wp.pl',
            password='password',
            goal='To be'
        )

    def test_custom_user_username(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.username, 'testuser')
    
    def test_custom_user_email(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.email, 'testuser@wp.pl')
    
    def test_custom_user_goal(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.goal, 'To be')
