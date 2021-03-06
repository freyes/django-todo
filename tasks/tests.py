from django.test import TestCase, Client
from models import Task
from forms import TaskForm
from urllib import urlencode
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
        task = Task(description="Test")
        task.save()
        fetched_task = Task.objects.filter(description="Test")[0]
        self.assertEqual(fetched_task.id, task.id)

    def test_task_should_be_complete(self):
        """
        A Task should be able to completed via the ORM
        """
        task = Task(description="Test")
        self.assertFalse(task.completed)
        task.completed = True
        task.save()
        fetched_task = Task.objects.filter(description="Test")[0]
        self.assertTrue(fetched_task.completed)

    def test_task_should_be_deletable(self):
        """
        A Task should be deletable via the ORM
        """
        task = Task(description="Workout")
        task.save()
        self.assertTrue(Task.objects.all().exists())
        task.delete()
        self.assertFalse(Task.objects.all().exists())

    def test_task_should_be_updatable(self):
        """
        A Task should be updatable via the ORM
        """
        task = Task(description="Workout")
        task.save()
        self.assertTrue(Task.objects.all().exists())
        task.description = "Test"
        task.save()
        self.assertTrue(Task.objects.filter(description="Test").exists())


class TaskFormTest(TestCase):
    def test_should_be_invalid_from_blank_description(self):
        """
        A Task Form should be invalid, due to blank desc.
        """
        task = Task()
        task_form = TaskForm(instance=task)
        self.assertFalse(task_form.is_valid())

class TaskIndexView(TestCase):
    def test_post_should_create_task(self):
        """
        A POST to the tasks view should result in a new task being created.
        """
        response = Client().post('/tasks/', {
            'description': 'drink milk'
        })
        #self.assertEqual(response.status_code, 201)
        self.assertEquals(Task.objects.all()[0].description, 'drink milk')

    def test_delete_should_delete_task(self):
        """
        A DELETE request should result in the task being deleted.
        """
        task = Task(description="run")
        task.save()
        response = Client().delete('/tasks/' + str(task.id))
        self.assertFalse(Task.objects.all().exists())
    
    def test_put_should_update_task(self):
        """
        A PUT request should result in the task being updated.
        """
        task = Task(description="run")
        task.save()
        response = Client().put(
            path = "/tasks/{0}".format(task.id),
            data = urlencode({
                'description': 'swim'
            }),
            content_type = 'application/x-www-form-urlencoded'
        )

        self.assertTrue(Task.objects.filter(description="swim").exists())
