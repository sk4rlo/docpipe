from pathlib import Path

from docling.document_converter import DocumentConverter

MARKDOWN_SUFFIXES = {".md", ".markdown"}


# Uses docling to convert a pdf into a markdown file and checks for errors.
# Returns an error if the output file already exists and --overwrite is not specified  
def convert_pdf_to_markdown(input_path: Path, output_path: Path, overwrite: bool = False) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != ".pdf":
        raise ValueError(f"Input file must be a PDF: {input_path}")

    if output_path.suffix.lower() not in MARKDOWN_SUFFIXES:
        raise ValueError(f"Output file must be Markdown: {output_path}")

    if output_path.exists() and not overwrite:
        raise FileExistsError(f"Output file already exists: {output_path}")

    converter = DocumentConverter()
    result = converter.convert(str(input_path))

    markdown = result.document.export_to_markdown()
    output_path.write_text(markdown, encoding="utf-8")

    print(f"Wrote Markdown to {output_path}")
