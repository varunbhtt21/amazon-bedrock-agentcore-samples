#!/usr/bin/env python3
"""
Simple Hello World Agent for Amazon Bedrock AgentCore
This is the simplest possible agent you can create and test locally.
"""

from bedrock_agentcore import BedrockAgentCoreApp
from datetime import datetime

# Create the AgentCore application
app = BedrockAgentCoreApp()

# Simple in-memory storage for conversation history
conversation_history = []

@app.entrypoint
def handle_request(payload):
    """
    Main handler function that processes incoming requests.
    This is where your agent logic goes.
    """

    # Extract the user's message from the payload
    user_message = payload.get("prompt", "Hello!")
    session_id = payload.get("session_id", "default")

    # Log the incoming request (useful for debugging)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Received: {user_message}")

    # Store in conversation history
    conversation_history.append({
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id,
        "user": user_message
    })

    # Simple agent logic - you can make this as complex as needed
    response = generate_response(user_message)

    # Store agent response
    conversation_history.append({
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id,
        "agent": response
    })

    # Return the response in the expected format
    return {
        "result": response,
        "session_id": session_id,
        "timestamp": datetime.now().isoformat()
    }

def generate_response(user_message: str) -> str:
    """
    Generate a response based on the user's message.
    This is where you'd add your agent's intelligence.
    """

    # Convert message to lowercase for easier matching
    message_lower = user_message.lower()

    # Simple response logic
    if "hello" in message_lower or "hi" in message_lower:
        return "Hello! I'm your simple agent. I can help you with basic questions. Try asking me about the time, date, or math!"

    elif "time" in message_lower:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    elif "date" in message_lower:
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date}"

    elif "name" in message_lower:
        return "I'm Simple Agent, your friendly AI assistant!"

    elif "help" in message_lower:
        return """I can help you with:
• Telling you the current time or date
• Basic math calculations
• Answering simple questions
• Having a friendly conversation

What would you like to know?"""

    elif "bye" in message_lower or "goodbye" in message_lower:
        return "Goodbye! It was nice talking to you. Have a great day!"

    elif "history" in message_lower:
        # Show recent conversation history
        recent = conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
        history_text = "Recent conversation:\n"
        for entry in recent:
            if "user" in entry:
                history_text += f"You: {entry['user']}\n"
            elif "agent" in entry:
                history_text += f"Me: {entry['agent']}\n"
        return history_text if len(recent) > 0 else "No conversation history yet."

    # Check for basic math
    elif any(op in message_lower for op in ['+', '-', '*', '/', 'plus', 'minus', 'times', 'divided']):
        return handle_math(message_lower)

    else:
        # Default response for unrecognized input
        return f"I heard you say: '{user_message}'. I'm a simple agent still learning. Try asking me about the time, date, or say 'help' to see what I can do!"

def handle_math(message: str) -> str:
    """
    Handle basic math operations.
    """
    try:
        # Replace word operators with symbols
        message = message.replace('plus', '+').replace('minus', '-')
        message = message.replace('times', '*').replace('multiplied by', '*')
        message = message.replace('divided by', '/').replace('divide', '/')

        # Try to evaluate simple math expressions
        # Extract numbers and operators
        import re
        pattern = r'(\d+)\s*([+\-*/])\s*(\d+)'
        match = re.search(pattern, message)

        if match:
            num1, operator, num2 = match.groups()
            num1, num2 = float(num1), float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "I can't divide by zero!"

            # Format result nicely
            if result.is_integer():
                result = int(result)

            return f"The answer is: {result}"
        else:
            return "I couldn't understand that math problem. Try something like '5 plus 3' or '10 divided by 2'"

    except Exception as e:
        return f"Sorry, I had trouble with that calculation. Try a simpler expression like '2 + 2'"

if __name__ == "__main__":
    # Run the agent locally for testing
    print("=" * 60)
    print("🤖 Simple Agent Starting...")
    print("=" * 60)
    print("Agent is ready at: http://localhost:8080/invocations")
    print("\nTest with: curl -X POST http://localhost:8080/invocations \\")
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"prompt": "Hello!"}\'')
    print("=" * 60)

    # Start the agent
    app.run(host="0.0.0.0", port=8080)