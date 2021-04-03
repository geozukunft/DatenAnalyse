import asyncio
import asyncpg
import plotly.express as pe


async def run():
    credentials = {"user": "", "password": "", "database": "postgres", "host": "192.168.110.18", "port": "5432"}
    db = await asyncpg.create_pool(**credentials)

    data = await db.fetch(
        """
        SELECT duration FROM euw1.match WHERE details_pulled is True AND queue IN (420)
        """
    )

    longestGame = 4565 // 60
    endTime = [0] * longestGame
    for game in data:
        endTime[game['duration'] // 60] += 1

    figure = pe.line(x=range(longestGame),y=endTime)
    figure.show()





loop = asyncio.get_event_loop()
loop.run_until_complete(run())