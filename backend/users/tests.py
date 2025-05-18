from django.test import TestCase

from django.test import TestCase
# from rest_framework.test import APIClient
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.librarian = User.objects.create_user(
            username="librarian", role=User.Roles.LIBRARIAN
        )
        self.member = User.objects.create_user(
            username="member", role=User.Roles.MEMBER
        )

    def test_librarian_permission(self):
        self.assertTrue(self.librarian.is_librarian)
        self.assertFalse(self.member.is_librarian)
