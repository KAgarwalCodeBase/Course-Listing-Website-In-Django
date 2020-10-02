from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Allcourses
# Create your tests here.

class AllcourseModelTests(TestCase):
    def test_was_published_recently_with_future_course(self):
        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Allcourses(startedfrom = time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_course(self):
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_course = Allcourses(startedfrom = time)
        self.assertIs(old_course.was_published_recently(),False)
    def test_was_published_recetly_with_recet_coures(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        old_course = Allcourses(startedfrom = time)
        self.assertIs(old_course.was_published_recently(),True)

