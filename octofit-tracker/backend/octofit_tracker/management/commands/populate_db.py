
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test123'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='test123'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test123'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test123'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', type='run', duration=30)
        Activity.objects.create(user='batman', type='cycle', duration=45)
        Activity.objects.create(user='superman', type='swim', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='batman', team='DC', score=90)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
