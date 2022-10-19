import os

cmds = [
    'pip install -r ./requirements.txt',
    'python ./tortoise-tts/setup.py install',
    'pip install imageio-ffmpeg'
    ]
for cmd in cmds:
    os.system(cmd)