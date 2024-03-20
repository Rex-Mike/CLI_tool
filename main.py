
import typer
from pathlib import Path
import shutil


def main(source_file: Path, destination_dir: Path):
    if not source_file.exists():
        print(f"The file {source_file} does not exist")
        raise typer.Exit()
        
    shutil.move(source_file, destination_dir)
    print("File moved")
if __name__ == "__main__":
    typer.run(main)

