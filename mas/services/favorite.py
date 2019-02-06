from typing import List

from mas.repositories import favorite as favorite_repo


async def add(*, user_id: int, object_id: int):
    await favorite_repo.add(user_id=user_id, object_id=object_id)


async def get(*, user_id: int) -> List[int]:
    return await favorite_repo.get(user_id=user_id)
