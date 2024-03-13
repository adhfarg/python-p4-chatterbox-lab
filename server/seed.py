
from random import choice as rc
from faker import Faker
from app import app, db, Message

fake = Faker()

def make_messages():
    Message.query.delete()

    messages = []

    for i in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(["Alice", "Bob", "Charlie"]),
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_messages()