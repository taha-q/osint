#!/usr/bin/env python3
"""
OSINT CLI tool with interactive and argument modes.
"""

import argparse
import asyncio
import sys
from typing import Optional

from modules.email_check import EmailChecker
from modules.username_searcher import UsernameSearcher


async def check_email(email: str) -> None:
    """Check if an email is valid."""
    async with EmailChecker() as checker:
        is_valid = await checker.is_valid_email(email)
        status = "Valid" if is_valid else "Invalid"
        print(f"+ {email}: {status}")


async def search_username(username: str, timeout: float = 5.0) -> None:
    """Search for a username across platforms."""
    async with UsernameSearcher() as searcher:
        matches = await searcher.search(username, timeout=timeout)
        if matches:
            print(f"\nFound {username} on:")
            for url in matches:
                print(f"+ {url}")
        else:
            print(f"No matches found for {username}")


async def interactive_mode() -> None:
    """Run in interactive mode."""
    print("\n=== OSINT CLI (Interactive Mode) ===")
    print("Commands: email, username, quit\n")

    while True:
        try:
            cmd = input("Enter command: ").strip().lower()

            if cmd == "quit" or cmd == "exit":
                print("Goodbye!")
                break

            elif cmd == "email":
                email = input("Enter email: ").strip()
                if email:
                    await check_email(email)

            elif cmd == "username":
                username = input("Enter username: ").strip()
                if username:
                    timeout_input = input("Timeout in seconds (default 5.0): ").strip()
                    timeout = float(timeout_input) if timeout_input else 5.0
                    await search_username(username, timeout=timeout)

            else:
                print("Unknown command. Try: email, username, quit")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


async def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="OSINT utilities for email validation and username search.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py email user@example.com
  python main.py username john_doe --timeout 10
  python main.py interactive
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Email subcommand
    email_parser = subparsers.add_parser("email", help="Check if an email is valid")
    email_parser.add_argument("email", help="Email address to check")

    # Username subcommand
    username_parser = subparsers.add_parser(
        "username", help="Search for a username across platforms"
    )
    username_parser.add_argument("username", help="Username to search for")
    username_parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Request timeout in seconds (default: 5.0)",
    )

    # Interactive subcommand
    subparsers.add_parser("interactive", help="Run in interactive mode")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    try:
        if args.command == "email":
            await check_email(args.email)

        elif args.command == "username":
            await search_username(args.username, timeout=args.timeout)

        elif args.command == "interactive":
            await interactive_mode()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
