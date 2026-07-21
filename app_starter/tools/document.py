from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    path: str = Field(description="Filesystem path to the PDF or DOCX file to convert"),
) -> str:
    """Converts a PDF or DOCX file at the given path to markdown-formatted text.

    Reads the document at the specified filesystem path and converts its
    contents to markdown. The file format (PDF vs DOCX) is inferred
    automatically from the path's extension — no separate file_type
    argument is needed.

    When to use:
    - When you have a path to a PDF or DOCX file on disk and need its
      contents as markdown text

    When not to use:
    - When you already have the raw file bytes in memory instead of a
      path — use `binary_document_to_markdown` instead

    Examples:
    >>> document_path_to_markdown("/path/to/report.pdf")
    '# Report\\n\\n...'
    """
    md = MarkItDown()
    result = md.convert(path)
    return result.text_content
