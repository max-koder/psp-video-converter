from basics import VideoPreset
from typing import List

PRESETS: List[VideoPreset] = [
    VideoPreset(
        key = '1',
        name = 'Low Quality',
        description = '480x272, 128kbps',
        width = 480,
        height = 272,
        profile = 'baseline',
        level = '3.0',
        audio_bitrate = '128k'
    ),
    VideoPreset(
        key = '2',
        name = 'Medium Quality',
        description = '480x272, 160kbps',
        width = 480,
        height = 272,
        profile = 'baseline',
        level = '3.0',
        audio_bitrate = '160k'
    ),
    VideoPreset(
        key = '3',
        name = 'Highest Quality',
        description = '480x272, 192kbps',
        width = 480,
        height = 272,
        profile = 'baseline',
        level = '3.0',
        audio_bitrate = '192k'
    )
]