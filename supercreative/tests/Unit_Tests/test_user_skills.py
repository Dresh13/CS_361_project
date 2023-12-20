from django.test import TestCase
from supercreative.user.user import edit_user, create_user
from supercreative.models import User, UserRole


class TestUserSkills(TestCase):
    # Pre-condition: User must exist, accept a string
    # post-condition User and only the user should have updated their skills, the skills should match the string
    def setUp(self):
        create_user("test@uwm.edu", "Testp@ss", UserRole.objects.create(role_name="TA").role_name, "testfirst",
                                     "testlast", "5555555555", "123")
        self.user = User.objects.get(email="test@uwm.edu")
        
    def test_correct_skill(self):
        self.user = User.objects.get(user_id=self.user.user_id)
        self.assertEqual(self.user.email, 'test@uwm.edu')
        self.assertEqual(self.user.password, 'Testp@ss')
        self.assertEqual(self.user.role_id.role_name, 'TA')
        self.assertEqual(self.user.first_name, 'testfirst')
        self.assertEqual(self.user.last_name, 'testlast')
        self.assertEqual(self.user.phone_number, '5555555555')
        self.assertEqual(self.user.address, '123')
        self.assertEqual(self.user.skills, '')

    def test_edit_user_skill(self):
        self.assertTrue(edit_user(self.user.user_id, "Testp@ss", "TA", "testfirst",
                                     "testlast", "5555555555", "testaddress", "Some"))
        self.user = User.objects.get(user_id=self.user.user_id)
        self.assertEqual(self.user.skills, "Some")

    def test_user_no_skills(self):
        self.assertTrue(edit_user(self.user.user_id, "Testp@ss", "TA", "testfirst",
                                     "testlast", "5555555555", "testaddress", ""))

    def test_bad_skill(self):
        self.assertFalse(edit_user(self.user.user_id, "Testp@ss", "TA", "testfirst",
                                     "testlast", "5555555555", "testaddress", 1))
