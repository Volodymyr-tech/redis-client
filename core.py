import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

def init_redis(
    host: str = REDIS_HOST,
    port: int = REDIS_PORT,
    # password: str = REDIS_PASSWORD
) -> redis.Redis:
    return redis.Redis(
        host=host,
        port=port,
        # password=password,
        decode_responses=True
    )

def test_redis_connection(client: redis.Redis) -> str:
    try:
        if client.ping():
            client.set("test_key", "hello_world")
            value = client.get("test_key")
            return f"Connected! Value: {value}"
        return "Can't connect to Redis!"
    except Exception as e:
        return f"An error occurs: {e}"

if __name__ == "__main__":
    redis_client = init_redis()
    print(test_redis_connection(redis_client))