import json
import os
import asyncio

import redis
from redis.asyncio import Redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

data_json = {
    "method": "publish",
    "params": {
        "channel": "chat:user_1",
        "data": {
            "chat": {"owner_id": 1, "client_id": 22, "platform": "instagram", "last_message": "sharyaaap"},
            "message": {"owner_id": 1, "chat_id": 1, "sender_type": "ai"}
        }
    }
}


class CustomRedis(Redis):
    """Basic redis methods"""

    def __init__(self, host: str = REDIS_HOST, port: int = REDIS_PORT, **kwargs):

        super().__init__(
            host=host,
            port=port,
            decode_responses=True,
            **kwargs
        )

    async def __call__(self):
        """Ping check: await redis_client()"""
        try:
            if await self.ping():
                await self.set("test_key", json.dumps(data_json))
                value = await self.get("test_key")
                obj = json.loads(value)
                return f"Connected! Value type: {type(obj)}. Data: {obj}"
            return "Can't connect to Redis!"
        except Exception as e:
            return f"An error occurs: {e}"


    async def set_cache_json(self, key:str, data: json):
        try:
            await self.set(key, json.dumps(data))
        except Exception as e:
            return f"An error occurs: {e}"


    async def get_cache_json(self, key:str):
        try:
            value = await self.get(key)
            return json.loads(value)
        except redis.exceptions.ConnectionError as e:
            print(e)
            return None


    async def delete_key(self, key: str):
        await self.delete(key)
        print(f"Key {key} deleted")

    async def delete_keys_by_prefix(self, prefix: str):
        keys = await self.keys(f"{prefix}*")
        if keys:
            await self.delete(*keys)
            print(f"Deleted keys starting with: {prefix}")

    async def delete_all_keys(self):
        await self.flushdb()
        print("All keys cleared")


async def main():
    redis_client = CustomRedis()

    await redis_client.set_cache_json("chacne:1", data_json)

    res = await redis_client.get_cache_json("chacne:1")
    print(res)
    for r in res:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())