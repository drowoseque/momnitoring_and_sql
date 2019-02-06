from typing import Tuple, Any, List, Optional

import asyncpg
from asyncpg import Record

from asyncpg.connection import Connection

from mas.settings import POSTGRES_CONNECTION_CONF


async def connect() -> Connection:
    return await asyncpg.connect(**POSTGRES_CONNECTION_CONF)


_connection = None


async def execute(
        *,
        query: str,
        params: Optional[Tuple[Any, ...]] = None,
) -> List[Record]:
    global _connection
    if _connection is None:
        _connection = await connect()

    return await _connection.fetch(query, *params)
