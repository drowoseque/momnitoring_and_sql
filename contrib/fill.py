import random
from concurrent.futures import ThreadPoolExecutor

import requests

NUM_USERS = 100000
NUM_OBJECTS = 20
MAX_OBJECT_ID = 1000000
MAX_WORKERS = 16


def add(user_id: int, object_id: int) -> None:
    requests.post(
        'http://localhost:8000/add/',
        json={
            'user_id': user_id,
            'object_id': object_id
        }
    )


def main():
    users = range(NUM_USERS)
    objects = list(range(MAX_OBJECT_ID))

    pairs = []
    for user in users:
        for _ in range(NUM_OBJECTS):
            pairs += [(user, random.choice(objects))]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as tpe:
        tpe.map(add, pairs)


if __name__ == '__main__':
    main()
