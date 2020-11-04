import asyncio
import aioredis
from example_pb2 import Feature, Point
from google.protobuf import json_format

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    while True:
        channel, text_message = await redis.blpop('testing')
        reply_channel = text_message[0:36].decode('utf-8')
        feature = json_format.Parse(text_message[36:], Feature())
        print(reply_channel)
        await redis.publish(reply_channel, 'Hello World')

asyncio.run(main())