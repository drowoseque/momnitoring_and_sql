import psycopg2
import random
from concurrent.futures import ThreadPoolExecutor

import requests

NUM_USERS = 100000

NUM_OBJECTS = 20000
MAX_WORKERS = 16

connection = psycopg2.connect("dbname='postgres' user='mslavoshevskiy' host='localhost' password='hui'")


def _populate_users():
    with connection.cursor() as cursor:
        for user in range(NUM_USERS):
            cursor.execute('INSERT INTO users(id) values (%s)', (user,))
    connection.commit()


def _populate_objects():
    with connection.cursor() as cursor:
        for object in range(NUM_OBJECTS):
            cursor.execute('INSERT INTO objects(id) values (%s) ', (object,))
    connection.commit()


def add(user_id: int, object_id: int) -> None:
    rep_code = requests.post(
        'http://localhost:8000/add/',
        json={
            'user_id': user_id,
            'object_id': object_id
        }
    ).status_code
    return rep_code


def main():
    users = range(NUM_USERS)
    objects = list(range(NUM_OBJECTS ))

    pairs = []
    for user in users:
        for _ in range(3):
            pairs += [(user, random.choice(objects))]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as tpe:
        result = tpe.map(lambda _: add(*_), pairs)
        print(list(result))


if __name__ == '__main__':
   # _populate_users()
   # _populate_objects()
   main()
