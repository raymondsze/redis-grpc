import asyncio
import aioredis
from example_pb2 import Feature, Point
from google.protobuf import json_format

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    feature = Feature(point=Point(latitude=10, longitude=10))
    message = json_format.MessageToJson(feature)
    await redis.publish('testing', message)
    redis.close()
    await redis.wait_closed()

asyncio.run(main())