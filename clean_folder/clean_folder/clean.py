from pathlib import Path
import shutil
import sys
from clean_folder import file_parser as parser
from clean_folder.normalize import normalize


def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)  # робимо папку для архіва
    folder_for_file = target_folder / normalize(
        filename.name.replace(filename.suffix, "")
    )
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file)
    except shutil.ReadError:
        print("It is not archive")
        folder_for_file.rmdir()
    filename.unlink()


def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / "Images" / "JPEG")
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / "Images" / "JPG")
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / "Images" / "PNG")
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / "Images" / "SVG")

    for file in parser.AVI_VIDEO:
        handle_media(file, folder / "Video" / "AVI")
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / "Video" / "MP4")
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / "Video" / "MOV")
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / "Video" / "MKV")

    for file in parser.DOC_DOCS:
        handle_media(file, folder / "Docs" / "Doc")
    for file in parser.DOCX_DOCS:
        handle_media(file, folder / "Docs" / "Docx")
    for file in parser.TXT_DOCS:
        handle_media(file, folder / "Docs" / "TXT")
    for file in parser.PDF_DOCS:
        handle_media(file, folder / "Docs" / "PDF")
    for file in parser.XLSX_DOCS:
        handle_media(file, folder / "Docs" / "XLSX")
    for file in parser.PPTX_DOCS:
        handle_media(file, folder / "Docs" / "PPTX")

    for file in parser.MP3_AUDIO:
        handle_media(file, folder / "Audio" / "MP3")
    for file in parser.OGG_AUDIO:
        handle_media(file, folder / "Audio" / "OGG")
    for file in parser.WAV_AUDIO:
        handle_media(file, folder / "Audio" / "WAV")
    for file in parser.AMR_AUDIO:
        handle_media(file, folder / "Audio" / "AMR")

    for file in parser.MY_OTHER:
        handle_media(file, folder / "MY_OTHER")
    for file in parser.ZIP_ARCHIVE:
        handle_media(file, folder / "ZIP_ARCHIVE")
    for file in parser.GZ_ARCHIVE:
        handle_media(file, folder / "GZ_ARCHIVE")
    for file in parser.TAR_ARCHIVE:
        handle_media(file, folder / "TAR_ARCHIVE")

    for folder in parser.FOLDERS[::-1]:
        try:
            folder.rmdir()
        except OSError:
            print(f"Can't delete folder: {folder}")


def start():
    if len(sys.argv) == 2:
        folder_for_scan = Path(sys.argv[1])
        print(f"Start in folder: {folder_for_scan.resolve()}")
        main(folder_for_scan.resolve())
        print("Finally we did it")
    else:
        print("Not enought or too many arguments. Try again!")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        folder_for_scan = Path(sys.argv[1])
        print(f"Start in folder: {folder_for_scan.resolve()}")
        main(folder_for_scan.resolve())
    else:
        print("Not enought or too many arguments. Try again!")
