import os

from pathlib import Path
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

from templates import career_gpt

# Initializes app with bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Langchain
template = career_gpt.template

prompt = PromptTemplate(
    input_variables=["history", "input"], 
    template=template
)


chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=4),
)

# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    # For debugging purposes
    # print(message)
    # logger.info(message)

    say(llm_predict(message["text"]))

# Mention handler for slack
# Call sherpa bot by using @CareerSherpa
@app.event("app_mention")
def handle_app_mention_events(ack, body, say, logger):
    ack()
    say(llm_predict(body["event"]["text"]))

# Command handler for Slack
# Call sherpa bot by using /sherpa command
@app.command("/sherpa")
def command_handler(ack, client, command):
    ack()

    # For debugging purposes
    # print(command)

    # Post the user's message to the channel
    channel_id = command["channel_id"]
    user_message = command["text"]
    
    # Retrieve the user's information
    user_info = client.users_info(user=command["user_id"])
    user_name = user_info["user"]["profile"]["real_name"]
    user_icon = user_info["user"]["profile"]["image_48"]

    # Post the user's message
    client.chat_postMessage(channel=channel_id, text=user_message, username=user_name, icon_url=user_icon)

    # Generate a response using ChatGPT
    output = llm_predict(user_message)

    # Post the response to the channel
    client.chat_postMessage(channel=channel_id, text=output)
    # ack()
    # print(command)

    # output = chatgpt_chain.predict(input=command["text"]) 
    # respond(output)

# The open_modal shortcut listens to a shortcut with the callback_id "open_modal"
@app.shortcut("open_modal")
def open_modal(ack, shortcut, client):
    ack()

def llm_predict(message):
    return chatgpt_chain.predict(input=message)


# TO make use of flask and ngrok, refer below:
# Source: https://www.makeuseof.com/slack-custom-slash-command-create-your-own/

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()