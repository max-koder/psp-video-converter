from basics import VideoPreset
from typing import List

PRESETS: List[VideoPreset] = [
    VideoPreset(
        key = '1',
        name = 'Low Quality Audio Bitrate',
        description = 'Have the lowest audio bitrate, but file will take less space',
        width = 480,
        height = 272,
        profile = 'baseline',
        level = '3.0',
        audio_bitrate = '128k'
    ),
    VideoPreset(
        key = '2',
        name = 'Medium Quality Audio Bitrate',
        description = 'Have medium audio bitrate',
        width = 480,
        height = 272,
        profile = 'baseline',
        level = '3.0',
        audio_bitrate = '160k'
    ),
    VideoPreset(
        key = '3',
        name = 'Highest Quality Audio Bitrate',
        description = 'Gives the best audio Bitrate on which PSP can work, but takes more space',
        width = 480,
        height = 272,
        profile = 'baseline',
        level = '3.0',
        audio_bitrate = '192k'
    )
]