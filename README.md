# Note Taker Agent

This Python program takes in streaming audio from a user via LiveKit client SDK, sends it to Cartesia's Ink STT model to transcribe into text, and then transmits a live transcription of what the user said back to their device.

This repo does not (at least not yet) provide a client implementation, only the agent implementation.

## Create a LiveKit Cloud project
1. Navigate to: [https://cloud.livekit.io](https://cloud.livekit.io)
2. Sign up and create a project

## Run the agent:
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cp .env.example .env`
5. add values for keys in `.env` (obtain values for LiveKit keys here: [https://cloud.livekit.io/projects/p_/settings/keys](https://cloud.livekit.io/projects/p_/settings/keys))
6. `python main.py dev`

## Run a test client:
1. Navigate to [https://agents-playground.livekit.io](https://agents-playground.livekit.io)
2. Select the project you just created (and set up keys for with the agent above) and click `Connect to <project name>`
3. Once you're connected, you should be able to speak and see transcriptions show up!
