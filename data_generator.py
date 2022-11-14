import json
import random
from datetime import timedelta


class DataGenerator:
    def __init__(self, beginning_date, duration_range, titles, descriptions, users, reminder=False, workshop=False):
        self.beginning_date = beginning_date
        self.duration_range = duration_range
        self.titles = titles
        self.descriptions = descriptions
        self.users = users
        self.reminder = reminder
        self.workshop = workshop

    def generate_data(self, amount):
        events = []

        for idx in range(amount):
            event = {
                'idx': idx,
                'start_date': f'{(self.beginning_date + timedelta(hours=random.randint(1, 5000))):%Y/%m/%d %H:%M}',
                'duration': random.randint(*self.duration_range),
                'title': random.choice(self.titles),
                'description': random.choice(self.descriptions),
                'owner': random.choice(self.users),
            }

            if self.reminder:
                event['reminder'] = random.choice([True, False])

            if self.workshop:
                event['workshop'] = random.choices(self.users, k=random.randint(3, 20))

            events.append(event)

        return events

    @staticmethod
    def save_data(data, path):
        with open(path, 'w') as file:
            json.dump(data, file)
