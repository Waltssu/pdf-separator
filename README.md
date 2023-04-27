### PDF Separator

This script searches a directory and its subdirectories for PDF files containing specific keywords in their text. 

If a PDF file is found with the required text, the script moves it to a specified destination directory. The script also creates the necessary directory structure in the destination directory.

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

##### Download and install Poppler from [here](https://blog.alivate.com.au/poppler-windows/).

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
