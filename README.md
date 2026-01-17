# Async Redis Client
#### A lightweight, high-performance asynchronous Redis client wrapper built on top of redis-py. Designed for seamless integration with FastAPI, Aiogram, and other async Python frameworks.

## 🚀 Key Features
Fully Asynchronous: Built with redis.asyncio for non-blocking I/O.

Connection Pooling: Efficiently manages multiple connections out of the box.

Singleton Friendly: Designed to be initialized once and reused across your entire application.

Clean API: Simplified methods for common operations (GET, SET, DELETE, EXISTS).


## ⚙️ Configuration
The client can be easily configured using environment variables for Dockerized environments:

````commandline
REDIS_HOST=localhost(Redis server hostname)
REDIS_PORT=6379(Redis server port)
REDIS_DB=1(Database index)
REDIS_PASSWORD=None(Authentication password)
````

