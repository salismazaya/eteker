from redis.asyncio import Redis
import os

redis_client = Redis.from_url(os.environ['REDIS_URL'])
