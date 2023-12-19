from django.test import TestCase
from supercreative.user.user import create_user_w_skill
from supercreative.models import User



class TestUserSkills(TestCase):
    #Pre-condition: User must exist, accept a string
    #post-condition User and only the user should have updated their skills, the skills should match the string
    def setUp(self):
        self.good_user = User(user_id=1, email="test@uwm.edu", password="Testp@ss", role="TA", first_name="testfirst",
                              last_name="testlast", phone_number="5555555555", address="123", skill="N/A")
        self.user_no_skills = User.objects.create(user_id=2, email='test2@example.com', password='testpassword',
                                                       role='user', first_name='Jane', last_name='Doe',
                                                       phone_number='9876543210', address='456 Oak St',)

    def test_correct_skill(self):
        self.assertEqual(self.good_user.user_id, 1)
        self.assertEqual(self.good_user.email, 'test@uwm.edu')
        self.assertEqual(self.good_user.password, 'Testp@ss')
        self.assertEqual(self.good_user.role, 'TA')
        self.assertEqual(self.good_user.first_name, 'testfirst')
        self.assertEqual(self.good_user.last_name, 'testlast')
        self.assertEqual(self.good_user.phone_number, '5555555555')
        self.assertEqual(self.good_user.address, '123')
        self.assertEqual(self.good_user.skill, 'N/A')
        self.assertTrue(create_user_w_skill(3, "test@uwm.edu", "Testp@ss", "TA", "testfirst", "testlast", "5555555555", "123", "N/A"))
        self.assertEqual(User.objects.get(user_id=3).user_id, 3)
        self.assertEqual(User.objects.get(user_id=3).email, "test@uwm.edu")
        self.assertEqual(User.objects.get(user_id=3).password, "Testp@ss")
        self.assertEqual(User.objects.get(user_id=3).role, "TA")
        self.assertEqual(User.objects.get(user_id=3).first_name, "testfirst")
        self.assertEqual(User.objects.get(user_id=3).last_name, "testlast")
        self.assertEqual(User.objects.get(user_id=3).phone_number, "5555555555")
        self.assertEqual(User.objects.get(user_id=3).address, "123")
        self.assertEqual(User.objects.get(user_id=3).skill, 'N/A')

    def test_user_no_skills(self):
        # Test if the user without skills was created successfully
        self.assertEqual(self.user_no_skills.user_id, 2)
        self.assertEqual(self.user_no_skills.email, 'test2@example.com')
        self.assertEqual(self.user_no_skills.password, 'testpassword')
        self.assertEqual(self.user_no_skills.role, 'user')
        self.assertEqual(self.user_no_skills.first_name, 'Jane')
        self.assertEqual(self.user_no_skills.last_name, 'Doe')
        self.assertEqual(self.user_no_skills.phone_number, '9876543210')
        self.assertEqual(self.user_no_skills.address, '456 Oak St')
        self.assertFalse(hasattr(self.user_no_skills, 'skills'))

    def test_bad_skill(self):
        self.assertFalse(create_user_w_skill(6, "test@uwm.edu", "Testp@ss", "TA", "testfirst",
                                            "testlast", "5555555555", "testaddress", 1))