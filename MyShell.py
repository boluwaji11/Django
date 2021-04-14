import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django

django.setup()

from MainApp.models import Topic

topics = Topic.objects.all()

for t in topics:
    print(f"Topic ID: {t.id} and Topic Name: {t}")