import asyncio
import aioredis
from uuid import uuid4
from example_pb2 import Feature, Point
from google.protobuf import json_format

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    reply_channel = str(uuid4())
    feature = Feature(point=Point(latitude=10, longitude=10))
    message = f'{reply_channel}{json_format.MessageToJson(feature)}'
    await redis.rpush('testing', message)
    [channel] = await redis.psubscribe(reply_channel)
    while True:
        message = await channel.get()
        print(message)
    # redis.close()
    # await redis.wait_closed()

asyncio.run(main())