import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCS = []
DOCX_DOCS = []
TXT_DOCS = []
PDF_DOCS = []
XLSX_DOCS = []
PPTX_DOCS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVE = []
GZ_ARCHIVE = []
TAR_ARCHIVE = []
MY_OTHER = []
ARCHIVES = []
REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "AVI": AVI_VIDEO,
    "MP4": MP4_VIDEO,
    "MOV": MOV_VIDEO,
    "MKV": MKV_VIDEO,
    "DOC": DOC_DOCS,
    "DOCX": DOCX_DOCS,
    "TXT": TXT_DOCS,
    "PDF": PDF_DOCS,
    "XLSX": XLSX_DOCS,
    "PPTX": PPTX_DOCS,
    "MP3": MP3_AUDIO,
    "OGG": OGG_AUDIO,
    "WAV": WAV_AUDIO,
    "AMR": AMR_AUDIO,
    "ZIP": ZIP_ARCHIVE,
    "GZ": GZ_ARCHIVE,
    "TAR": TAR_ARCHIVE,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def scan(folder: Path):
    # JPEG_IMAGES = []
    # JPG_IMAGES = []
    # PNG_IMAGES = []
    # SVG_IMAGES = []
    # AVI_VIDEO = []
    # MP4_VIDEO = []
    # MOV_VIDEO = []
    # MKV_VIDEO = []
    # DOC_DOCS = []
    # DOCX_DOCS = []
    # TXT_DOCS = []
    # PDF_DOCS = []
    # XLSX_DOCS = []
    # PPTX_DOCS = []
    # MP3_AUDIO = []
    # OGG_AUDIO = []
    # WAV_AUDIO = []
    # AMR_AUDIO = []
    # ZIP_ARCHIVE = []
    # GZ_ARCHIVE = []
    # TAR_ARCHIVE = []
    # MY_OTHER = []
    # ARCHIVES = []

    # REGISTER_EXTENSION = {
    #     "JPEG": JPEG_IMAGES,
    #     "JPG": JPG_IMAGES,
    #     "PNG": PNG_IMAGES,
    #     "SVG": SVG_IMAGES,
    #     "AVI": AVI_VIDEO,
    #     "MP4": MP4_VIDEO,
    #     "MOV": MOV_VIDEO,
    #     "MKV": MKV_VIDEO,
    #     "DOC": DOC_DOCS,
    #     "DOCX": DOCX_DOCS,
    #     "TXT": TXT_DOCS,
    #     "PDF": PDF_DOCS,
    #     "XLSX": XLSX_DOCS,
    #     "PPTX": PPTX_DOCS,
    #     "MP3": MP3_AUDIO,
    #     "OGG": OGG_AUDIO,
    #     "WAV": WAV_AUDIO,
    #     "AMR": AMR_AUDIO,
    #     "ZIP": ZIP_ARCHIVE,
    #     "GZ": GZ_ARCHIVE,
    #     "TAR": TAR_ARCHIVE,
    # }
    # FOLDERS = []
    # EXTENSION = set()
    # UNKNOWN = set()

    for item in folder.iterdir():
        # Якщо це папка то додаємо її до списку FOLDERS і переходимо до наступного елемента папки
        if item.is_dir():
            # перевіряємо, щоб папка не була тією в яку ми складаємо вже файли
            if item.name not in (
                "Archives",
                "Video",
                "Audio",
                "Documents",
                "Images",
                "MY_OTHER",
            ):
                FOLDERS.append(item)
                # скануємо вкладену папку
                scan(item)  # рекурсія
            continue  # переходимо до наступного елементу в сканованій папці

        #  Робота з файлом
        ext = Path(item.name).suffix[1:].upper()  # беремо розширення файлу
        fullname = folder / item.name  # беремо шлях до файлу
        if not ext:  # якщо файл немає розширення то додаєм до невідомих
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                # Якщо ми не зареєстрували розширення у REGISTER_EXTENSION, то додаємо до невідомих
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)
    return MOV_VIDEO, XLSX_DOCS


if __name__ == "__main__":
    if len(sys.argv) == 2:
        folder_to_scan = sys.argv[1]
        print(sys.argv)
        print(f"Start in folder {folder_to_scan}")
        scan(Path(folder_to_scan))
        print(f"Images JPEG: {scan(Path(folder_to_scan))}")
        print(f"Images JPG: {JPG_IMAGES}")
        print(f"Images SVG: {SVG_IMAGES}")
        print(f"Images PNG: {PNG_IMAGES}")
        print(f"Video MP4: {MP4_VIDEO}")
        print(f"Video AVI: {AVI_VIDEO}")
        print(f"Video MOV: {MOV_VIDEO}")
        print(f"Video MKV: {MKV_VIDEO}")
        print(f"Docs Doc: {DOC_DOCS}")
        print(f"Docs Docx: {DOCX_DOCS}")
        print(f"Docs PDF: {PDF_DOCS}")
        print(f"Docs TXT: {TXT_DOCS}")
        print(f"Docs XLSX: {XLSX_DOCS}")
        print(f"Docs PPTX: {PPTX_DOCS}")
        print(f"Audio mp3: {MP3_AUDIO}")
        print(f"Audio OGG: {OGG_AUDIO}")
        print(f"Audio VAW: {WAV_AUDIO}")
        print(f"Audio AMR: {AMR_AUDIO}")
        print(f"Archives ZIP: {ZIP_ARCHIVE}")
        print(f"Archives GZ: {GZ_ARCHIVE}")
        print(f"Archives TAR: {TAR_ARCHIVE}")
        print(f"Types of files in folder: {EXTENSION}")
        print(f"Unknown files of types: {UNKNOWN}")
        print(f"MY_OTHER: {MY_OTHER}")
        print(f"Folders: {FOLDERS}")
    else:
        print("Not enought or too many arguments. Try again!")
