from django.test import TestCase
from models import Task
from forms import TaskForm
from django.core.exceptions import ValidationError

class TaskTest(TestCase):
    def test_completed_should_be_false(self):
        """
        Tests that completed is false.
        """
        task = Task()
        self.assertEqual(task.completed, False)

    def test_description_should_not_allow_blank(self):
        """
        Description field should raise exception when value is blank.
        """
        task = Task()

        # @todo how to validate one field?
        with self.assertRaises(ValidationError):
            task.full_clean()


    def test_task_should_be_fetchable(self):
        """
        A Task should be fetchable via the ORM
        """
        task = Task(description="Bob")
        task.save()
        fetched_task = Task.objects.filter(description="Bob")[0]
        self.assertEqual(fetched_task.id, task.id)

class TaskFormTest(TestCase):
    def test_should_be_invalid_from_blank_description(self):
        """
        A Task Form should be invalid, due to blank desc.
        """
        task = Task()
        task_form = TaskForm(instance=task)
        self.assertFalse(task_form.is_valid())
        