# from asyncio.windows_events import NULL
import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from allrunning import grab_all_running
from isrunning import isrunning

def index_in_list(a_list, index):
  return index < len(a_list)

app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/cycle")
def cycle(ack, body, respond):
  if body["channel_name"] != "test":
    ack(f"[ERROR] You are not in the right channel. Ask me again from test channel")
  else:
    iBody = body["text"]
    iBody_split = iBody.split()

    if index_in_list(iBody_split, 0):
      match iBody_split[0]:
        case 'list':
          ack('Getting you all your pods:')
          respond(grab_all_running())
        case 'pod':
          if not index_in_list(iBody_split, 1):
            ack('[ERROR] - Missing pod name!')
          else:
            if isrunning(iBody_split[1]):
              ack('Found pod')
            else:
              ack('[ERROR] - Pod not running!')
        case _:
          ack('Unknow command!')
    else:
      ack(f'Bruh! why you playing with me. You need pass something in.')

@app.event("app_mention")
def event_test(say):
  say("Hi there!")

if __name__ == "__main__":
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
