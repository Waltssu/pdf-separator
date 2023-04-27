import os
import shutil
import pytesseract
from pdf2image import convert_from_path
import logging

# Logging
logging.basicConfig(
    filename="separator.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# CONFIGURATION #
poppler_path = r'' # Path to Poppler
start_dir = '' # Path to searched root folder
file_types = ['.pdf'] # Filetypes to be searched
search_words = [''] # Words that script looks for
destination_directory = '' # Root folder where new folder structure will be created


# Create necessary directories
def create_directories(path, destination_path):
    dirs = path.split(os.path.sep)
    dirs = dirs[1:]
    current_dir = destination_path
    for directory in dirs:
        current_dir = os.path.join(current_dir, directory)
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)


# Check if file exists in the destination
def file_exists_in_destination(file_path, destination_path):
    dir_path, file_name = os.path.split(file_path)
    rel_path = os.path.relpath(dir_path, start_dir)
    sub_dir_path = os.path.join(destination_path, rel_path)
    dest_file_path = os.path.join(sub_dir_path, file_name)
    return os.path.exists(dest_file_path)


# Search and process files in the directory
def search_directory(directory):
    log_handler = logging.FileHandler('search_directory.log', mode='w')
    log_formatter = logging.Formatter('%(asctime)s - %(message)s')
    log_handler.setFormatter(log_formatter)
    log = logging.getLogger('search_directory')
    log.addHandler(log_handler)

    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                if os.path.splitext(filename)[1] in file_types:
                    if os.path.splitext(filename)[1] == '.pdf':
                        try:
                            pages = convert_from_path(
                                file_path, poppler_path=poppler_path)
                            for i, page in enumerate(pages):
                                found = False
                                for orientation in [0, 180]:
                                    if found:
                                        break
                                    # if .pdf file is upside down
                                    if orientation == 180:
                                        page = page.rotate(orientation)
                                    text = pytesseract.image_to_string(
                                        page, lang='eng+fin')
                                    # if words are found in the files
                                    if any(word in text for word in search_words):
                                        found = True
                                        # if file is not already in the destination, create necessary folders and move file
                                        if not file_exists_in_destination(file_path, destination_directory):
                                            dir_path, file_name = os.path.split(
                                                file_path)
                                            rel_path = os.path.relpath(
                                                dir_path, start_dir)
                                            sub_dir_path = os.path.join(
                                                destination_directory, rel_path)
                                            create_directories(
                                                sub_dir_path, destination_directory)
                                            dest_file_path = os.path.join(
                                                sub_dir_path, file_name)
                                            shutil.move(
                                                file_path, dest_file_path)
                                            print(
                                                f'Moved file: {filename} to {dest_file_path}')
                                            log.info(
                                                f'Moved file: {filename} to {dest_file_path}')
                                        else:
                                            # file already exists in destination, dont move
                                            print(
                                                f'File {filename} already exists in the destination')
                                            log.info(
                                                f'File {filename} already exists in the destination')
                        # error logging
                        except Exception as e:
                            log.error(
                                f'Error searching directory {directory}: {e}')
                            print(
                                f'Error searching directory {directory}: {e}')
            # directory logging
            elif os.path.isdir(file_path):
                print(f'Searching directory: {directory}, file: {filename}')
                log.info(f'Searching directory: {directory}, file: {filename}')
                try:
                    search_directory(file_path)
                except Exception as e:
                    log.error(f'Error searching subdirectory {file_path}: {e}')
                    print(f'Error searching subdirectory {file_path}: {e}')
    except Exception as e:
        log.error(f'Error searching directory {directory}: {e}')
        print(f'Error searching directory {directory}: {e}')

    log.removeHandler(log_handler)


# Start the search from the specified directory
try:
    search_directory(start_dir)
except Exception as e:
    logging.error(f'Error starting search from directory {start_dir}: {e}')
    print(f'Error starting search from directory {start_dir}: {e}')
