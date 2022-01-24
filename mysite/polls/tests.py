import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
    def test_status_with_ending_today(self):
        time = timezone.now() + datetime.timedelta(hours=5)
        question = Question(end_date=time)
        self.assertEqual(question.status(), "Ending today")

    def test_status_with_published_today(self):
        end_time = timezone.now() + datetime.timedelta(days=1, hours=5)
        pub_time = timezone.now() - datetime.timedelta(hours=5)
        question = Question(end_date=end_time, pub_date=pub_time)
        self.assertEqual(question.status(), "Added today")

    def test_status_with_ending_soon(self):
        time = timezone.now() - datetime.timedelta(days=5)
        question = Question(end_date=time, pub_date=time)
        self.assertEqual(question.status(), "Ending soon")

    def test_status_with_published_recently(self):
        end_time = timezone.now() + datetime.timedelta(days=20)
        pub_time = timezone.now() - datetime.timedelta(days=5)
        question = Question(end_date=end_time, pub_date=pub_time)
        self.assertEqual(question.status(), "Added recently")

# def create_question(question_text, days):
#     time = timezone.now() + datetime.timedelta(days=days)
#     return Question.objects.create(question_text=question_text, pub_date=time)

# class QuestionIndexViewTests(TestCase):
#     def test_no_questions(self):
#         response = self.client.get(reverse('polls:index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No polls are available.")
#         self.assertQuerysetEqual(response.context['latest_question_list'], [])
 
#     def test_past_question(self):
#         question = create_question(question_text="Past question.", days=-30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             [question],
#         )

#     def test_future_question(self):
#         create_question(question_text="Future question.", days=30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertContains(response, "No polls are available.")
#         self.assertQuerysetEqual(response.context['latest_question_list'], [])

#     def test_future_question_and_past_question(self):
#         question = create_question(question_text="Past question.", days=-30)
#         create_question(question_text="Future question.", days=30)
#         response = self.client.get(reverse('polls:index'))
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             [question],
#         )

#     def test_two_past_questions(self):
#         question1 = create_question(question_text="Past_quesion1.", days=-30)
#         question2 = create_question(question_text="Past_quesion2.", days=-5)
#         response = self.client.get(reverse('polls:index'))
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             [question2, question1]
#         )

# class QuestionDetailViewTests(TestCase):
#     def test_future_question(self):
#         future_question = create_question(question_text='Future question.', days=5)
#         url = reverse('polls:detail', args=(future_question.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)

#     def test_past_question(self):
#         past_question = create_question(question_text='Past Question.', days=-5)
#         url = reverse('polls:detail', args=(past_question.id,))
#         response = self.client.get(url)
#         self.assertContains(response, past_question.question_text)
