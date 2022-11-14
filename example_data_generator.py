from datetime import date, timedelta

from data_generator import DataGenerator

event_data = DataGenerator(
    date.today() + timedelta(days=10),
    (15, 180),
    ['breakfast', 'lunch', 'meeting', 'call', 'pay bills'],
    ['eat breakfast', 'eat lunch', 'meeting with boss', 'call to dad', 'electricity'],
    ['ala', 'ola', 'john', 'sam', 'tom'],
    False,
    False
)

events = event_data.generate_data(150)
event_data.save_data(events, 'events_data.json')

reminder_data = DataGenerator(
    date.today() + timedelta(days=10),
    (15, 180),
    ['breakfast', 'lunch', 'meeting', 'call', 'pay bills'],
    ['eat breakfast', 'eat lunch', 'meeting with boss', 'call to dad', 'electricity'],
    ['ala', 'ola', 'john', 'sam', 'tom'],
    True,
    False
)
reminders = reminder_data.generate_data(50)
reminder_data.save_data(reminders, 'reminder_data.json')

workshop_data = DataGenerator(
    date.today() + timedelta(days=10),
    (15, 180),
    ['breakfast', 'lunch', 'meeting', 'call', 'pay bills'],
    ['eat breakfast', 'eat lunch', 'meeting with boss', 'call to dad', 'electricity'],
    ['ala', 'ola', 'john', 'sam', 'tom'],
    True,
    False
)

workshops = workshop_data.generate_data(50)
workshop_data.save_data(workshops, 'workshop_data.json')
