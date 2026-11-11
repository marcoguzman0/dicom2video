from pathlib import Path
import subprocess
import re

PROJECT_PATH = Path(__file__).resolve().parent
images_path = PROJECT_PATH / 'input'
output_path = PROJECT_PATH / 'output'
_IMAGE_SUFFIX_PATTERN = re.compile(r'-[a-zA-Z0-9]+$')


def ensure_directories() -> None:
  images_path.mkdir(parents=True, exist_ok=True)
  output_path.mkdir(parents=True, exist_ok=True)


def main_menu() -> None:
  while True:
    print("\033c", end="")
    print("========== Weasis2Video ==========")
    print("Main menu:")
    print("1. Rename images and generate video")
    print("2. Exit program")
    picked_option = input("Input here your option (number only): ")

    match picked_option:
      case "1":
        rename_images()
        generate_video()
      case "2":
        return
      case _:
        print("Invalid option. Please enter 1 or 2.")


def rename_images() -> None:
  for file in images_path.iterdir():
    if file.is_file() and file.suffix.lower() == '.png':
      new_stem = _IMAGE_SUFFIX_PATTERN.sub('', file.stem)
      new_path = file.with_name(f'{new_stem}{file.suffix}')

      if new_path == file:
        continue
      if not new_path.exists():
        file.rename(new_path)
        print(f'Renaming: {file.name} -> {new_path.name}')
      else:
        print(f'Omitted (file already exists): {file.name} -> {new_path.name}')


def generate_video(
  output: Path = output_path / 'output.mp4',
  framerate: int = 3,
) -> None:
  ffmpeg_cmd = [
    "ffmpeg",
    "-framerate",
    str(framerate),
    "-i",
    str(images_path / '%05d.png'),
    "-c:v",
    "libx264",
    "-crf",
    "15",
    "-preset",
    "slow",
    "-pix_fmt",
    "yuv420p",
    str(output),
  ]

  try:
    subprocess.run(ffmpeg_cmd, check=True, text=True, capture_output=True)
    print(f"Video successfully generated: {output}")
  except FileNotFoundError as error:
    print(f"Failed trying to execute ffmpeg: {error}")
  except subprocess.CalledProcessError as e:
    print("Failed trying to execute ffmpeg:")
    print(e.stderr)