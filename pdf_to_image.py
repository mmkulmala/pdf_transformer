from pdf2image import convert_from_path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="PDF file to transform")
parser.add_argument("to", help="Path for image")
parser.add_argument("type", help="Type of image")

args = parser.parse_args()

def convert_file(pdf_file_path: str, path_to: str, type: str):
    convert_from_path(pdf_file_path, fmt=type, output_folder=path_to)

def main():
    convert_file(args.file, args.to, args.type)

if __name__=="__main__":
    main()
