<h1 align="center">PDF Separator</h1>

#### Background story
Assignment at work to go thru multiple directories filled with .pdf, .xlsx, .dwg etc. files and those needed to be sorted out. This script was created to automatically go thru the files and look for specific keywords and move the files into the correct destination depending on the keyword. _(e.g. property_1 and property_2)_

Script also creates a similar folder structure into the new destination, so the files will stay in the same directory but the root directory is in the correct destination.

### Prerequisites

The script requires the following packages to be installed:

- pdf2image
- pytesseract
- poppler

### Planned features

- Compability to search for multiple files, for example:
   - DWG files
   - Word documents
   - Excel spreadsheets
   - etc.

#### Installation

- Install the required packages using pip:
   ```
    pip install pdf2image pytesseract
   ```

##### Download and install Poppler from [here](https://poppler.freedesktop.org/).

#### Usage

- Set the following configurations in the script:

    ```
    poppler_path = r'PATH TO POPPLER'  # Path to the Poppler bin folder
    
    start_dir = 'START DIR PATH'  # Path to the directory to search
    
    file_types = ['.pdf']  # List of file types to search for
                                (WIP, .pdf only for now.)
    
    search_words = ['']  # List of keywords to search for
    
    destination_directory = 'PATH TO DESTINATION'  # Path to the destination directory
    ```

- Run the script:

    ```
    python pdf_separator.py
    ```
