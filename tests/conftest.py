import pytest_asyncio
from fastmcp import Client

from example.calculator import mcp


@pytest_asyncio.fixture
async def client():
    async with Client(mcp) as client:
        yield client
