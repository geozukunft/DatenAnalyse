import asyncio
import asyncpg


async def run():
    credentials = {"user": "", "password": "", "database": "postgres", "host": "192.168.110.18", "port": "5432"}
    db = await asyncpg.create_pool(**credentials)

    data = await db.fetch(
        """
        SELECT duration FROM euw1.match WHERE details_pulled is True AND queue IN (420)
        """
    )

    for game in data:



loop = asyncio.get_event_loop()
loop.run_until_complete(run())