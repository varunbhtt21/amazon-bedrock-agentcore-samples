# 🤖 Simple Agent - Your First AgentCore Agent

This is the simplest possible agent you can create and test with Amazon Bedrock AgentCore. It's perfect for learning and testing!

## 🎯 What This Agent Does

This simple agent can:
- ✅ Respond to greetings
- ⏰ Tell you the current time
- 📅 Show today's date
- 🧮 Perform basic math calculations
- 💬 Remember conversation history
- 🎯 Provide help and guidance

## 🚀 Quick Start (3 Minutes!)

### Step 1: Set Up Environment

```bash
# Navigate to the simple-agent directory
cd simple-agent

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Mac/Linux
# OR
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Start the Agent

In Terminal 1:
```bash
# Start the agent
python simple_agent.py
```

You should see:
```
============================================================
🤖 Simple Agent Starting...
============================================================
Agent is ready at: http://localhost:8080/invocations
Health check at: http://localhost:8080/health
```

### Step 3: Test the Agent

In Terminal 2:

**Option A: Interactive Chat**
```bash
# Run the interactive test client
python test_agent.py
```

**Option B: Quick Test**
```bash
# Send a single test message
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello! What can you do?"}'
```

**Option C: Run Automated Tests**
```bash
# Run all test cases
python test_agent.py --test
```

## 🎮 Interactive Chat Examples

Once you run `python test_agent.py`, try these:

```
You: Hello!
Agent: Hello! I'm your simple agent. I can help you with basic questions...

You: What time is it?
Agent: The current time is 2:45 PM

You: What's 15 plus 27?
Agent: The answer is: 42

You: Show me history
Agent: Recent conversation:
You: Hello!
Me: Hello! I'm your simple agent...
You: What time is it?
Me: The current time is 2:45 PM
```

## 📁 Project Structure

```
simple-agent/
├── simple_agent.py     # Main agent code
├── test_agent.py       # Interactive test client
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 How It Works

1. **Agent Core**: The `BedrockAgentCoreApp` handles HTTP requests and responses
2. **Entry Point**: The `@app.entrypoint` decorator marks the main handler function
3. **Request Processing**: Each request contains a "prompt" from the user
4. **Response Generation**: Simple if-else logic generates appropriate responses
5. **Memory**: Basic conversation history stored in-memory

## 🚀 Deploy to AWS (Optional)

Once you're happy with local testing, deploy to AWS:

### Prerequisites
- AWS account with Bedrock access
- AWS CLI configured (`aws configure`)
- AgentCore CLI installed (`pip install bedrock-agentcore-starter-toolkit`)

### Deploy
```bash
# Configure for deployment
agentcore configure -e simple_agent.py

# Deploy to AWS
agentcore launch

# Test deployed agent
agentcore invoke '{"prompt": "Hello from AWS!"}'
```

## 🎨 Customize Your Agent

Want to make it smarter? Edit `simple_agent.py`:

### Add New Responses
```python
elif "weather" in message_lower:
    return "I can't check real weather yet, but it's always sunny in the cloud! ☁️"
```

### Add a Joke Feature
```python
elif "joke" in message_lower:
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the agent go to therapy? It had too many issues to handle!",
    ]
    import random
    return random.choice(jokes)
```

### Connect to Real APIs
```python
elif "weather" in message_lower:
    # Add real weather API call here
    weather_data = get_weather_from_api()
    return f"Current weather: {weather_data}"
```

## 🐛 Troubleshooting

### Agent won't start?
```bash
# Check if port 8080 is already in use
lsof -i :8080  # Mac/Linux
netstat -ano | findstr :8080  # Windows

# Kill the process or use a different port
python simple_agent.py --port 8081
```

### Module not found?
```bash
# Make sure virtual environment is activated
which python  # Should show venv path

# Reinstall requirements
pip install -r requirements.txt
```

### Connection refused?
- Make sure the agent is running in Terminal 1
- Check firewall settings
- Try `http://127.0.0.1:8080` instead of `localhost`

## 📚 Next Steps

1. **Add AI**: Integrate with Claude or other LLMs
2. **Add Tools**: Connect to databases, APIs, or files
3. **Add Memory**: Use AgentCore Memory for persistent storage
4. **Add Auth**: Implement authentication with AgentCore Identity
5. **Production**: Deploy with proper monitoring and scaling

## 🎓 Learning Resources

- [AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/)
- [Strands Agents](https://strandsagents.com/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)

## 🤝 Help & Support

Having issues? Try:
1. Check the troubleshooting section above
2. Run `python test_agent.py --test` to verify setup
3. Check agent logs in Terminal 1
4. Restart both the agent and test client

---

**Happy Testing! 🚀** Your simple agent is ready to chat!