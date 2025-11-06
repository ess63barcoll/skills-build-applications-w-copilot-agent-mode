from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=10)
        self.assertEqual(activity.type, 'run')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user='testuser', team='Test Team', score=50)
        self.assertEqual(leaderboard.score, 50)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')
