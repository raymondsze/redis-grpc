import asyncio
import aioredis
from example_pb2 import Feature, Point
from google.protobuf import json_format

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    channel, = await redis.subscribe('testing')
    assert isinstance(channel, aioredis.Channel)
    
    async def reader(channel):
        async for message in channel.iter():
            feature = json_format.Parse(message, Feature())
            print("Got message:", feature.point.latitude)
    task = asyncio.get_running_loop().create_task(reader(channel))
    await task
    # redis.close()
    # await redis.wait_closed()

asyncio.run(main())