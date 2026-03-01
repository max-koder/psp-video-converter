from pathlib import Path
from presets import PRESETS
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import ffmpeg

console = Console()

def get_input_output_data():
    inp_out_list = []

    console.print('Enter [red][bold]FULL[/red][/bold] path to your input video'),
    console.print('[green]Example[/green]: /username/Videos/input_video_name.mp4'),
    console.print('[bold]YOUR INPUT PATH[/bold]: ', end=""),

    inp_out_list.append(str(Path(input().strip())))
    console.print('\n')

    console.print('Enter [red][bold]FULL[/red][/bold] path where you want to get your output video'),
    console.print('[green]Example[/green]: /username/Videos/output_video_name.mp4'),
    console.print('[bold]YOUR OUTPUT PATH[/bold]: ', end=""),

    inp_out_list.append(str(Path(input().strip())))
    console.print('\n')

    return inp_out_list

def preset_choice():

    console.print(Panel("[bold]Welcome to PSP Video Converter![/bold]\n\n"
          "To start work with application, choose preset for video conversion.\n"))

    table = Table(title = "Presets", padding = (1, 2), min_width=60)

    table.add_column("ID", justify="left", style="cyan", no_wrap=True)
    table.add_column("Preset", style="magenta")
    table.add_column("Description", justify="left", style="green")

    for presets in PRESETS:
        table.add_row(f"{presets.key}", f"{presets.name}", f"{presets.description}")

    console.print(table)
    console.print("To choose preset write it [red][bold]ID[/red][/bold]: ", end="")
    preset_chosen = int(input())
    console.print('\n')

    return preset_chosen


def make_conversion(preset_chosen ,inp_out_list):

    input_path = inp_out_list[0]
    output_path = inp_out_list[1]

    output_options = PRESETS[preset_chosen-1].convert_to_ffmpeg_settings()

    ffmpeg.input(input_path).output(output_path, **output_options).run(quiet=True)

    print("Conversion completed")

make_conversion(preset_choice(), get_input_output_data())




