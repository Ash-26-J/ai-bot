import discord
import openai
import os

# Set up OpenAI API key
openai.api_key = 'ai'  # Replace with your OpenAI API key

# Set up Discord bot token
DISCORD_TOKEN = 'DISCORD_TOKEN'  # Replace with your Discord bot token

# Create an instance of a client
client = discord.Client()

# Function to get a response from GPT-4
async def get_gpt4_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )

        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."

# Event when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event to listen to messages in Discord
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Respond only to messages that start with the bot's prefix (e.g., !ask)
    if message.content.startswith('!ask'):
        prompt = message.content[len('!ask '):]  # Get the question after the command

        # Call GPT-4 to get a response
        response = await get_gpt4_response(prompt)

        # Send the response back to the Discord channel
        await message.channel.send(response)

# Run the bot
client.run(DISCORD_TOKEN)
