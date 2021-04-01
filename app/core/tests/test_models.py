from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "test@gmail.com"
        password = "Mwduioiw980"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        email = "aidu@sUIODIJ.Xpm"
        user = get_user_model().objects.create_user(email=email)
        self.assertEqual(user.email, email.lower())

    def test_user_email_not_valid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "afeuo2345")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            "aidfsikdjf@sufoijv.com",
            "sbdnvj2300"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)