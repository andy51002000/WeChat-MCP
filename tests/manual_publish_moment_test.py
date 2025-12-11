from __future__ import annotations

from wechat_mcp.publish_moment_utils import publish_moment_without_media


def main() -> None:
    """
    Manual invocation helper for publish_moment_without_media.

    Run via:
        uv run python -m tests.manual_publish_moment_test
    """
    content = "Test moment from WeChat-MCP automation (no media)."
    result = publish_moment_without_media(content)
    print(result)


if __name__ == "__main__":
    main()

