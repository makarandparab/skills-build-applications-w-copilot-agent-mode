from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop all collections and their indexes to ensure a clean state
        collections = db.list_collection_names()
        for collection in collections:
            db[collection].drop()

        # Recreate collections with unique constraints
        db.create_collection('users')
        db.users.create_index('email', unique=True)

        db.create_collection('teams')
        db.teams.create_index('name', unique=True)

        db.create_collection('activity')
        db.activity.create_index('activity_id', unique=True)

        db.create_collection('leaderboard')
        db.leaderboard.create_index('leaderboard_id', unique=True)

        db.create_collection('workouts')
        db.workouts.create_index('workout_id', unique=True)

        # Insert data into MongoDB using pymongo
        db.users.insert_many([
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ])

        db.teams.insert_many([
            {"_id": ObjectId(), "name": "Blue Team"},
            {"_id": ObjectId(), "name": "Gold Team"},
        ])

        db.activity.insert_many([
            {"_id": ObjectId(), "user": "thundergod", "activity_type": "Cycling", "duration": "1:00:00"},
            {"_id": ObjectId(), "user": "metalgeek", "activity_type": "Crossfit", "duration": "2:00:00"},
            {"_id": ObjectId(), "user": "zerocool", "activity_type": "Running", "duration": "1:30:00"},
            {"_id": ObjectId(), "user": "crashoverride", "activity_type": "Strength", "duration": "0:30:00"},
            {"_id": ObjectId(), "user": "sleeptoken", "activity_type": "Swimming", "duration": "1:15:00"},
        ])

        db.leaderboard.insert_many([
            {"_id": ObjectId(), "user": "thundergod", "score": 100},
            {"_id": ObjectId(), "user": "metalgeek", "score": 90},
            {"_id": ObjectId(), "user": "zerocool", "score": 95},
            {"_id": ObjectId(), "user": "crashoverride", "score": 85},
            {"_id": ObjectId(), "user": "sleeptoken", "score": 80},
        ])

        db.workouts.insert_many([
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
