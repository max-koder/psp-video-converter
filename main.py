from pathlib import Path
from presets import PRESETS
from basics import VideoPreset
import ffmpeg

def get_input_output_data():
    inp_out_list = []
    print('To start conversion, write path to file, which you want to convert')
    inp_out_list.append(str(Path(input().strip())))
    print('Thanks! Please, write path, where you want to find output file, with filename')
    inp_out_list.append(str(Path(input().strip())))
    return inp_out_list

def preset_choice():

    print("Welcome to PSP Video Converter!"
          "To start work with application, choose presets for video conversion\n")

    for presets in PRESETS:
        print(f'{presets.key}. {presets.name}')
        print(f'{presets.description}\n')

    print('Please, choose preset from 1-3: ')
    preset_chosen = int(input())

    return preset_chosen


def make_conversion(preset_chosen ,inp_out_list):

    input_path = inp_out_list[0]
    output_path = inp_out_list[1]

    output_options = PRESETS[preset_chosen-1].convert_to_ffmpeg_settings()

    ffmpeg.input(input_path).output(output_path, **output_options).run()
    print("Conversion completed")

make_conversion(preset_choice(), get_input_output_data())




