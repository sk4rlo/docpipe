import argparse
from pathlib import Path

from convert import convert_pdf_to_markdown
from summarize import summarize_markdown

# 1 ----------- function handlers --------------

def handle_convert(args):
    try:
        convert_pdf_to_markdown(
            input_path=Path(args.input),
            output_path=Path(args.output),
            overwrite=args.overwrite,
        )
    except FileNotFoundError as error:
        raise SystemExit(f"Error: {error}")
    except FileExistsError as error:
        raise SystemExit(f"Error: {error}")
    except ValueError as error:
        raise SystemExit(f"Error: {error}")

def handle_summarize(args):
    try:
        summarize_markdown(
            input_path=Path(args.input),
            output_path=Path(args.output),
            chunks=args.chunks,
            max_chunk_words=args.max_chunk_words,
            overwrite=args.overwrite,
        )
    except FileNotFoundError as error:
        raise SystemExit(f"Error: {error}")
    except FileExistsError as error:
        raise SystemExit(f"Error: {error}")
    except ValueError as error:
        raise SystemExit(f"Error: {error}")
    except RuntimeError as error:
        raise SystemExit(f"Error: {error}")

# 2 ----------- main --------------

def main():
    parser = argparse.ArgumentParser(prog="docpipe")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # calls the handler for convert command (pdf to markdown conversion)
    convert_parser = subparsers.add_parser("convert")
    convert_parser.add_argument("input")
    convert_parser.add_argument("-o", "--output", required=True)
    convert_parser.add_argument("--overwrite", action="store_true")
    convert_parser.set_defaults(func=handle_convert)

    # calls the handler for summarize command (chunking and then summary)
    summarize_parser = subparsers.add_parser("summarize")
    summarize_parser.add_argument("input")
    summarize_parser.add_argument("-o", "--output", required=True)
    summarize_parser.add_argument("--chunks", type=int, default=10)
    summarize_parser.add_argument("--max-chunk-words", type=int, default=300)
    summarize_parser.add_argument("--overwrite", action="store_true")
    summarize_parser.set_defaults(func=handle_summarize)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
