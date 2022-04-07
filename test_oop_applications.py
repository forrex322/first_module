from unittest import TestCase
from OopApplication import *


class TestAndroidApplication(TestCase):

    def setUp(self):
        self.android1 = AndroidApplication('Dota', '2007-07-14', 2.0)
        self.android2 = AndroidApplication('CS:GO', '2008-08-15', 3.0)
        self.android1_related_date = datetime.strptime(self.android1.release_date, "%Y-%m-%d")
        self.android2_related_date = datetime.strptime(self.android2.release_date, "%Y-%m-%d")
        self.android1.list_of_versions = [2.0, 3.0, 3.1]

    def test_str(self):
        self.assertEqual(self.android1.__str__(), f'Application: {self.android1.name}')

    def test_repr(self):
        self.assertEqual(self.android1.__repr__(), f'Application: {self.android1.name}, release date: {self.android1.release_date}, version: {self.android1.version}')

    def test_get_absolute_url(self):
        self.assertEqual(self.android1.get_absolute_url(), f'play.google.com/webstore/{self.android1.name.replace(" ", "_")}')

    def test_eq(self):
        self.assertEqual(self.android1 == self.android2, False)

    def test_gt(self):
        self.assertEqual((self.android1_related_date.year > self.android2_related_date.year) & (self.android1.version > self.android2.version), False)

    def test_lt(self):
        self.assertEqual((self.android1_related_date.year < self.android2_related_date.year) & (self.android1.version < self.android2.version), True)

    def test_getter_list_of_compatible_versions(self):
        self.assertEqual(self.android1.list_of_versions, [2.0, 3.0, 3.1])


class TestIOSApplication(TestCase):

    def setUp(self):
        self.ios1 = IOSApplication('CS:GO', '2012-08-20', 1.1)
        self.ios2 = IOSApplication('Minecraft', '2007-07-07', 2.2)

    def test_get_absolute_url(self):
        self.assertEqual(self.ios1.get_absolute_url(), f'apple.com/ua/app-store/{self.ios1.name.replace(" ", "_")}')

    def test_eq(self):
        self.assertEqual(self.ios1 == self.ios2, False)

    def test_gt(self):
        self.assertEqual(self.ios1.release_date > self.ios2.release_date, True)

    def test_lt(self):
        self.assertEqual((self.ios1.release_date < self.ios2.release_date), False)


class TestDesktopApplication(TestCase):

    def setUp(self):
        self.desktop1 = DesktopApplication('Among Us', '2020-09-10', 3.2)
        self.desktop2 = DesktopApplication('Speed Racer', '2021-10-10', 4.4)
        self.desktop1.description = '123456789012345678901234567890123456789012345678901234567890'
        self.desktop1.list_of_platforms = ['windows', 'linux', 'macos']

    def test_max_length_of_description(self):
        with self.assertRaises(Exception):
            self.desktop1.description = '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321' \
                                        '12321321321321321'

    def test_short_description(self):
        self.assertEqual(self.desktop1.short_description(), '1234567890')

    def test_getter_list_of_available_platforms(self):
        self.assertEqual(self.desktop1.list_of_platforms, ['windows', 'linux', 'macos'])
