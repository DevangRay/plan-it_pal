from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


# Create your tests here.
class TestLoginAuthentication(TestCase):
    def test_admin_login(self):
        user = User.objects.create(username='foo', is_superuser=True)
        factory = RequestFactory()

        request = factory.delete('/')
        request.user = user

        permission = user.has_perm('global_permissions.is_advisor')

        self.assertTrue(permission)

    def test_student_login(self):
        user = User.objects.create(username='foo')
        factory = RequestFactory()

        request = factory.delete('/')
        request.user = user

        permission = user.has_perm('global_permissions.is_advisor')

        self.assertFalse(permission)

    # def test_login_with_user_in_advisor_group(self):
    #     user = User.objects.create(username='foo')
    #     factory = RequestFactory()
    #
    #     request = factory.delete('/')
    #     request.user = user
    #     permission = Permission.objects.create(codename='is_advisor', name="Is Advisor")
    #
    #     groups = Group.objects.get_or_create("Advisor")
    #     groups.permissions.add(permission)
    #     user.groups.add(groups)
    #
    #     permission = user.has_perm('global_permissions.is_advisor')
    #     self.assertTrue(permission)