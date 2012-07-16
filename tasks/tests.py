"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Task

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class TaskTest(TestCase):
	def test_completed_should_be_false(self):
		"""
		Tests that completed is false.
		"""
		task = Task()
		self.assertEqual(task.completed, False)
	def test_description_should_allow_blank(self):
		"""
		Description field should allow blank value.
		"""
		task = Task()
		self.assertEqual(task.description, '')