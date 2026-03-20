import os
import sys
import argparse
from pdf2image import convert_from_path
from PIL import Image

def extract_images_from_pdf(pdf_path, output_folder, poppler_path=None):
    """
    Extracts each page of a PDF file as an image.

    Args:
        pdf_path (str): The path to the PDF file.
        output_folder (str): The folder where images will be saved.
        poppler_path (str, optional): The path to the Poppler 'bin' directory.
    """
    try:
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Created output folder: {output_folder}")

        # Convert PDF to list of PIL images
        print(f"Converting {pdf_path}...")
        images = convert_from_path(pdf_path, poppler_path=poppler_path)

        # Save each page as an image
        for i, image in enumerate(images):
            card_num = (i // 2) + 1
            side = "recto" if i % 2 == 0 else "verso"
            image_name = f"card_{card_num}_{side}.png"
            image_path = os.path.join(output_folder, image_name)
            image.save(image_path, "PNG")
            print(f"Saved: {image_path}")

        print(f"Extraction complete. {len(images)} images saved to {output_folder}.")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        if "poppler" in str(e).lower():
            print("\nTip: Make sure Poppler is installed and added to your system PATH, or provide the poppler_path argument.", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Extract images (pages) from a PDF file.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("-o", "--output", help="Output folder (default: 'output')", default="output")
    parser.add_argument("-p", "--poppler", help="Path to Poppler 'bin' folder (optional)", 
                        default=r"C:\Program Files (x86)\poppler\poppler-25.12.0\Library\bin")

    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        print(f"Error: File '{args.pdf_path}' not found.")
        sys.exit(1)

    extract_images_from_pdf(args.pdf_path, args.output, args.poppler)

if __name__ == "__main__":
    main()
