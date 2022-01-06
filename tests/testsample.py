from django.test import TestCase

from accounts.admin import UserAdmin


class UserAdminTest(TestCase):
    def test_credentials_section(self):
        title = UserAdmin.fieldsets[0][0]
        self.assertIsNone(title, '\ntitle بخش اول از fieldsets باید برابر None باشد.')
        fields = list(UserAdmin.fieldsets[0][1].get('fields'))
        expected_fields = ['username', 'password']
        self.assertListEqual(fields, expected_fields, '\nفیلدهای بخش اول از fieldsets باید برابر username و password باشند.')