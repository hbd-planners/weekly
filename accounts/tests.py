from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestCustomUser(TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@wp.pl',
            password='password',
            goal='To be',
            is_staff=False,
        )

        self.user2 = get_user_model().objects.create_user(
            username='adminuser',
            email='adminuser@wp.pl',
            password='password',
            goal='To be admin',
            is_staff=True,
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
    
    def test_custom_user_is_staff(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.is_staff, False)
    
    def test_custom_user_on_admin_page(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_admin_user_username(self):
        user = get_user_model().objects.get(id=2)
        self.assertEqual(user.username, 'adminuser')
    
    def test_admin_user_email(self):
        user = get_user_model().objects.get(id=2)
        self.assertEqual(user.email, 'adminuser@wp.pl')
    
    def test_admin_user_goal(self):
        user = get_user_model().objects.get(id=2)
        self.assertEqual(user.goal, 'To be admin')
    
    def test_admin_user_is_staff(self):
        user = get_user_model().objects.get(id=2)
        self.assertEqual(user.is_staff, True)
    
    def test_custom_user_on_admin_page_valid_password(self):
        self.client.login(username='adminuser', password='password')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_custom_user_on_admin_page_wrong_password(self):
        self.client.login(username='adminuser', password='passwort')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)


class TestUserAuthentication(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@mail.com',
            password='password',
            goal='To be',
            is_staff=False,
        )

    def test_status_code_after_login(self):
        response = self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)

    def test_login_page_template(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_page_template(self):
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_home_page_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_reversed_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        
