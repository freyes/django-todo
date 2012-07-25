from django.test import TestCase
from models import Task


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