#!/usr/bin/env python3
"""
Test script for Simple Agent
Run this to interact with your agent in the terminal.
"""

import requests
import sys
from datetime import datetime

# Configuration
AGENT_URL = "http://localhost:8080/invocations"

def check_agent_running():
    """Check if the agent is running by sending a test message."""
    try:
        # Try sending a simple test message
        test_payload = {"prompt": "ping", "session_id": "health-check"}
        response = requests.post(
            AGENT_URL,
            json=test_payload,
            headers={"Content-Type": "application/json"},
            timeout=2
        )
        if response.status_code == 200:
            print(f"✅ Agent is running and ready!")
            return True
        else:
            print(f"⚠️ Agent returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Agent is not running. Please start the agent first:")
        print("   python simple_agent.py")
        return False
    except Exception as e:
        print(f"❌ Error checking agent: {e}")
        return False

def send_message(message: str, session_id: str = "test-session"):
    """Send a message to the agent and return the response."""
    try:
        payload = {
            "prompt": message,
            "session_id": session_id
        }

        response = requests.post(
            AGENT_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("result", "No response")
        else:
            return f"Error: Agent returned status code {response.status_code}"

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to agent. Is it running?"
    except Exception as e:
        return f"Error: {e}"

def interactive_chat():
    """Run an interactive chat session with the agent."""
    print("\n" + "=" * 60)
    print("🤖 Simple Agent Test Client")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'help' to see what the agent can do")
    print("=" * 60 + "\n")

    # Check if agent is running first
    if not check_agent_running():
        print("\nPlease start the agent and try again.")
        sys.exit(1)

    print("\n" + "-" * 60)
    session_id = f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    print(f"Session ID: {session_id}")
    print("-" * 60 + "\n")

    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("\n👋 Goodbye! Thanks for chatting!")
                break

            # Send message to agent
            print("\n🤖 Agent: ", end="", flush=True)
            response = send_message(user_input, session_id)
            print(response)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

def run_tests():
    """Run a series of test messages."""
    print("\n" + "=" * 60)
    print("🧪 Running Agent Tests")
    print("=" * 60)

    # Check if agent is running
    if not check_agent_running():
        print("\nPlease start the agent and try again.")
        sys.exit(1)

    # Test messages
    test_messages = [
        "Hello!",
        "What's your name?",
        "What time is it?",
        "What's today's date?",
        "Can you help me?",
        "Calculate 5 plus 3",
        "What is 10 times 4?",
        "What is 100 divided by 25?",
        "Show me history",
        "Goodbye!"
    ]

    print("\n" + "-" * 60)
    session_id = "test-session"

    for message in test_messages:
        print(f"\n📤 Sending: {message}")
        response = send_message(message, session_id)
        print(f"📥 Response: {response}")
        print("-" * 40)

    print("\n✅ Tests completed!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test the Simple Agent")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run automated tests instead of interactive chat"
    )
    parser.add_argument(
        "--url",
        default="http://localhost:8080",
        help="Agent URL (default: http://localhost:8080)"
    )

    args = parser.parse_args()

    # Update URL if custom URL provided
    if args.url != "http://localhost:8080":
        AGENT_URL = f"{args.url}/invocations"

    # Run tests or interactive chat
    if args.test:
        run_tests()
    else:
        interactive_chat()