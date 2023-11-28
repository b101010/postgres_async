import asyncio
import asyncpg
import fake_data
import time

async def insert_record(pool, record):
    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(
                "INSERT INTO users (name) VALUES ($1)",
                record["name"]
            )

async def main():
    async with asyncpg.create_pool(dsn="postgresql://postgres:valami@localhost/async") as pool:

        # records = [
        #     {"name": "Tom Bombadil"},
        #     {"name": "Frodo Baggins"}
        # ]

        fake = fake_data.fakeDicts(1000,100,'name')
        records = fake.genDicts()

        tasks = []
        for record in records:
            tasks.append(insert_record(pool, record))

        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)
