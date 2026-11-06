from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

mcp = FastMCP(name="calculator")


@mcp.tool(name="multiply", description="Multiply two numbers.", tags=set(["math", "arithmetic"]))
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.

    """
    return a * b


@mcp.tool(name="add", description="Add two numbers.", tags=set(["math", "arithmetic"]))
def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    """
    return a + b


@mcp.tool(
    name="subtract",
    description="Subtract one number from another.",
    tags=set(["math", "arithmetic"]),
)
def subtract(a: float, b: float) -> float:
    """Subtract one number from another.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b.

    """
    return a - b


@mcp.tool(
    name="divide", description="Divide one number by another.", tags=set(["math", "arithmetic"])
)
def divide(a: float, b: float) -> float:
    """Divide one number by another.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a and b.

    """
    if b == 0:
        raise ToolError("Cannot divide by zero")
    return a / b


def main() -> None:
    """Run the calculator MCP server over stdio."""
    mcp.run()  # STDIO by default
