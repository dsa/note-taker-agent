from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    cartesia,
    noise_cancellation,
    silero,
)

load_dotenv()


class NoteTaker(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a note taker.")


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=cartesia.STT(),
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=NoteTaker(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
