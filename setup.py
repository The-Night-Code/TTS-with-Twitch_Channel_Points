from cx_Freeze import setup, Executable

setup(name="TTS redeem twitch message",
      version="0.1",
      description="",
      executables=[Executable("tts_twitch_chat.py")])