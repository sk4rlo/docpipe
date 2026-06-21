# docpipe

`docpipe` is a small local CLI for two file-based workflows:

1. Convert a PDF file to Markdown.
2. Summarize a Markdown file into another Markdown file.

The workflows are intentionally separate:

```text
PDF -> Markdown
Markdown -> Summary Markdown
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

Check the CLI:

```bash
docpipe --help
```

## Convert

Convert a PDF to Markdown:

```bash
docpipe convert input.pdf -o output.md
```

By default, existing output files are not overwritten. To overwrite:

```bash
docpipe convert input.pdf -o output.md --overwrite
```

## Summarize

Summarize a Markdown file:

```bash
export DOCPIPE_API_KEY="your_api_key_here"
docpipe summarize input.md -o summary.md
```

Options:

```bash
docpipe summarize input.md -o summary.md --chunks 10 --max-chunk-words 300
```

- `--chunks` sets the target number of Markdown chunks.
- `--max-chunk-words` asks the model to keep each chunk summary under that word count.
- `--overwrite` allows replacing an existing output file.

The summarization backend uses the OpenAI Python SDK. By default, it uses the standard OpenAI API unless `DOCPIPE_BASE_URL` is set.

Use OpenAI:

```bash
export DOCPIPE_API_KEY="your_openai_key"
export DOCPIPE_MODEL="gpt-5.4-mini"
unset DOCPIPE_BASE_URL
```

Use Groq's OpenAI-compatible API for a free alternative:

```bash
export DOCPIPE_API_KEY="your_groq_key"
export DOCPIPE_BASE_URL="https://api.groq.com/openai/v1"
export DOCPIPE_MODEL="openai/gpt-oss-20b"
```

The default model is:

```text
openai/gpt-oss-20b
```

You can override it with:

```bash
export DOCPIPE_MODEL="another-model-id"
```

## Current Behavior

- PDF conversion uses Docling.
- Markdown chunking is simple paragraph grouping based on the requested chunk count.
- Each chunk is summarized with AI.
- Final output is built by deterministically merging chunk summaries.
- The final merge does not call AI.

## Supported Formats

`convert`:

- input: `.pdf`
- output: `.md` or `.markdown`

`summarize`:

- input: `.md` or `.markdown`
- output: `.md` or `.markdown`

## Credits

PDF conversion is powered by [Docling](https://github.com/docling-project/docling).

## Notes

Do not commit API keys, `.env` files, virtual environments, generated outputs, or local test documents.

## Next Steps

Improve chunking modes (use the number of paragraph in the .md file as chunks when they do not exceed max chunck size as default)
