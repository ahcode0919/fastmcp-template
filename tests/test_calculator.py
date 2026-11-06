import pytest
from fastmcp.exceptions import ToolError


@pytest.mark.asyncio
async def test_add(client):
    result = await client.call_tool("add", {"a": 3, "b": 4})
    assert result.data == 7


@pytest.mark.asyncio
async def test_subtract(client):
    result = await client.call_tool("subtract", {"a": 3, "b": 4})
    assert result.data == -1


@pytest.mark.asyncio
async def test_multiply(client):
    result = await client.call_tool("multiply", {"a": 3, "b": 4})
    assert result.data == 12


@pytest.mark.asyncio
async def test_divide(client):
    result = await client.call_tool("divide", {"a": 4, "b": 4})
    assert result.data == 1


@pytest.mark.asyncio
async def test_divide_by_zero(client):
    with pytest.raises(ToolError, match="Cannot divide by zero"):
        await client.call_tool("divide", {"a": 1, "b": 0})
