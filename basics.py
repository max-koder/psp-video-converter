from dataclasses import dataclass
from typing import Dict

@dataclass
class VideoPreset:
    key: str
    name: str
    description: str
    width: int
    height: int
    profile: str
    level: str
    audio_bitrate: str

    def convert_to_ffmpeg_settings(self) -> Dict[str, any]:
        return {
            'vf': f'scale={self.width}:{self.height},format=yuv420p',
            'profile': f'{self.profile}',
            'level': f'{self.profile}',
            'audio_bitrate': f'{self.audio_bitrate}'
        }

