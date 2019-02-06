import random
from concurrent.futures import ThreadPoolExecutor

import requests

NUM_USERS = 1000000
NUM_OBJECTS = 2000
MAX_OBJECT_ID = 100000
MAX_WORKERS = 16


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
    objects = list(range(MAX_OBJECT_ID))

    pairs = []
    for user in users:
        for _ in range(NUM_OBJECTS):
            pairs += [(user, random.choice(objects))]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as tpe:
        result = tpe.map(lambda _: add(*_), pairs)
        print(list(result))


if __name__ == '__main__':
    main()
