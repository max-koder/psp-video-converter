from pathlib import Path
from .presets import PRESETS
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import ffmpeg
import sys

console = Console()


def show_input_start_data():
    console.print('Enter [red][bold]FULL[/red][/bold] path to your input video'),
    console.print('[green]Example[/green]: /username/Videos/input_video_name.mp4')

def show_output_start_data():
    console.print('Enter [red][bold]FULL[/red][/bold] path where you want to get your output video'),
    console.print('[green]Example[/green]: /username/Videos/output_video_name.mp4')

def get_input_data():
    while True:
        console.print('[bold]YOUR INPUT PATH[/bold]: ', end=""),
        user_input = Path(input().strip())

        if str(user_input) == 'quit':
            console.print('[purple] Have a nice day! [/purple]')
            sys.exit(0)

        console.print("\n")

        if not user_input.is_file():
            console.print("[red][bold]ERROR: Incorrect input. Please try again.[/red][/bold]")
            console.print('\n')
            continue

        return str(user_input)

def get_output_data():
    while True:
        console.print('[bold]YOUR OUTPUT PATH[/bold]: ', end=""),
        user_input = Path(input().strip())

        if str(user_input) == 'quit':
            console.print('[purple] Have a nice day! [/purple]')
            sys.exit(0)

        try:
            user_input.parent.mkdir(parents = True, exist_ok = True),
            console.print("\n")
            return str(user_input)

        except PermissionError:
            console.print("[red]ERROR: Can't write file on this location. Please choose another one.[/red]")
            continue

        except Exception as e:
            console.print(f"[red]ERROR: {e}. Please try again")
            continue

def start_screen():
    console.print(Panel("[bold]Welcome to PSP Video Converter![/bold]\n\n"
                        "To start work with application, choose preset for video conversion.\n"
                        "To close app, write 'quit'\n"))

def preset_choice():
    table = Table(title = "Presets", min_width=60, box=box.SIMPLE_HEAVY)

    table.add_column("ID", justify="left", style="cyan", no_wrap=True)
    table.add_column("Preset", style="magenta")
    table.add_column("Description", justify="left", style="green")

    for presets in PRESETS:
        table.add_row(f"{presets.key}", f"{presets.name}", f"{presets.description}")

    console.print(table)

    while True:
        console.print("To choose preset write it [red][bold]ID[/red][/bold]: ", end="")
        chosen_by_user_preset = input()

        if chosen_by_user_preset not in ['1', '2', '3', 'quit']:
            console.print("[red][bold]ERROR: You wrote incorrect value. Please write another.[/red][/bold]\n")
            continue

        if chosen_by_user_preset == 'quit':
            console.print('[purple] Have a nice day! [/purple]')
            sys.exit(0)

        console.print('\n')

        return int(chosen_by_user_preset)


def make_conversion():

    chosen_by_user_preset = preset_choice()

    show_input_start_data()
    input_path = get_input_data()

    show_output_start_data()
    output_path = get_output_data()

    output_options = PRESETS[chosen_by_user_preset - 1].convert_to_ffmpeg_settings()

    ffmpeg.input(input_path).output(output_path, **output_options).run(quiet=True)

    console.print("[green]Conversion completed[/green]")
    console.print("Do you want convert more videos?\n"
                  "1. Yes\n"
                  "2. No\n")
    console.print("Please, use [red]numbers[/red] to give answer")
    console.print('[bold]ANSWER[/bold]: ', end='')
    if int(input()) == 1:
        make_conversion()
    else:
        sys.exit(0)

def main():
    start_screen()
    make_conversion()

if __name__ == "__main__":
    main()
