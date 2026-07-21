# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Python package implementing document-related tools (conversion/processing), exposed through an MCP server (`FastMCP`) for use by AI assistants. `app_starter` is a subdirectory of the larger `eulerapp` repo.

## Setup & running

```bash
uv venv
source .venv/bin/activate
uv pip install -e .

uv run main.py      # start the MCP server
uv run pytest       # run all tests
```

## Defining MCP tools

Tools are plain Python functions registered with the MCP server in `main.py` via `mcp.tool()(function_name)`.

Each parameter should use `pydantic.Field` for its description, and the docstring should:
- Begin with a one-line summary
- Provide a detailed explanation of functionality
- Explain when to use (and not use) the tool
- Include usage examples with expected input/output

`tools/math.py`'s `add` is the reference example for this convention:

```python
from pydantic import Field


def add(
    a: float = Field(description="First number to add"),
    b: float = Field(description="Second number to add"),
) -> float:
    """Add two numbers together.

    Takes two numerical inputs and returns their sum. This tool handles
    integers and floating point numbers.

    When to use:
    - When you need to perform simple addition
    - When you need precise numerical calculation

    Examples:
    >>> add(2, 3)
    5.0
    >>> add(2.5, 3.5)
    6.0
    """
    return a + b
```

New tools go in `tools/`, follow this pattern, and must be registered with `mcp.tool()(...)` in `main.py` to actually be exposed.

**Known gap:** `tools/document.py`'s `binary_document_to_markdown` is WIP — it isn't yet registered in `main.py`, and its docstring doesn't yet follow the Field/when-to-use/examples convention above. Bring it in line with the convention and register it when working on that tool.

## Tests

Tests live in `tests/`, one `Test<FunctionName>` class per tool function (see `tests/test_document.py`). Binary fixtures (real sample files, not mocks) live in `tests/fixtures/`.

## Code style

Always apply appropriate type annotations to function arguments (and return types).
