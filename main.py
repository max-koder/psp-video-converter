from pathlib import Path
import ffmpeg

def get_input_output_data():
    inp_out_list = []
    print("Welcome to PSP Converter\n Please, to start conversion, write path to file, which you want to convert")
    inp_out_list.append(str(Path(input().strip())))
    print("Thanks! Please, write path, where you want to find output file, with filename")
    inp_out_list.append(str(Path(input().strip())))
    return inp_out_list

def make_conversion(inp_out_list):
    input_path = inp_out_list[0]
    output_path = inp_out_list[1]
    output_options = {'vf': 'scale=480:272,format=yuv420p', 'profile:v': 'baseline', 'level': '3.0' }
    ffmpeg.input(input_path).output(output_path, **output_options).run()
    print("Conversation completed")
make_conversion(get_input_output_data())




