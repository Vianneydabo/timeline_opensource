# PDF Image Extractor

A simple and robust Python utility to extract each page of a PDF file as a PNG image, named according to a card recto/verso scheme.

## Features
- Convert each page of a PDF to a high-quality JPEG image.
- Command-line interface for easy usage.
- Error handling for missing files or Poppler configuration issues.

## Prerequisites

### 1. Python Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
*Alternatively, you can install them individually:*
```bash
pip install pdf2image pillow
```

### 2. Poppler (Required)
`pdf2image` is a wrapper around the Poppler utility. You must have Poppler installed on your system.

#### Windows installation:
1. Download the latest Poppler for Windows (e.g., from [Oshani's Poppler Windows builds](https://github.com/oschwartz10612/poppler-windows/releases/)).
2. Extract the ZIP file to a location (e.g., `C:\Program Files\poppler`).
3. Add the `bin` directory of the extracted folder to your system **PATH** environment variable.
4. *Alternatively*, you can specify the path to the `bin` folder directly in the script using the `--poppler` argument.

#### Linux installation (Ubuntu/Debian):
```bash
sudo apt-get install poppler-utils
```

#### macOS installation:
```bash
brew install poppler
```

## Usage

You can run the script from the command line:

```bash
python extract_images_from_pdf.py <path_to_pdf> -o <output_folder>
```

### Arguments:
- `pdf_path`: (Required) The path to the PDF file you want to process.
- `-o`, `--output`: (Optional) The directory where images will be saved. Default is `output`.
- `-p`, `--poppler`: (Optional) The path to the Poppler `bin` directory. Default is your current installation path.

### Example:
```bash
python extract_images_from_pdf.py document.pdf -o my_images
```

## How it works
The script uses `pdf2image.convert_from_path` to read the PDF file and convert each page into a PNG image. The naming convention is:
- **Even-numbered pages** (1, 3, 5...): `card_{N}_recto.png`
- **Odd-numbered pages** (2, 4, 6...): `card_{N}_verso.png`

## Troubleshooting
If you receive an error stating `poppler is not installed or in PATH`, ensure that the `pdftoppm` executable is accessible. On Windows, this is usually located in the `bin` folder of your Poppler installation.
