import os
import pytest
from tools.document import binary_document_to_markdown, document_path_to_markdown


class TestBinaryDocumentToMarkdown:
    # Define fixture paths
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_fixture_files_exist(self):
        """Verify test fixtures exist."""
        assert os.path.exists(self.DOCX_FIXTURE), (
            f"DOCX fixture not found at {self.DOCX_FIXTURE}"
        )
        assert os.path.exists(self.PDF_FIXTURE), (
            f"PDF fixture not found at {self.PDF_FIXTURE}"
        )

    def test_binary_document_to_markdown_with_docx(self):
        """Test converting a DOCX document to markdown."""
        # Read binary content from the fixture
        with open(self.DOCX_FIXTURE, "rb") as f:
            docx_data = f.read()

        # Call function
        result = binary_document_to_markdown(docx_data, "docx")

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result

    def test_binary_document_to_markdown_with_pdf(self):
        """Test converting a PDF document to markdown."""
        # Read binary content from the fixture
        with open(self.PDF_FIXTURE, "rb") as f:
            pdf_data = f.read()

        # Call function
        result = binary_document_to_markdown(pdf_data, "pdf")

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result


class TestDocumentPathToMarkdown:
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    # Both fixtures share this text, so it's a reliable fidelity check.
    KNOWN_CONTENT = "Model Context Protocol"

    def test_document_path_to_markdown_with_docx(self):
        """Test converting a DOCX document to markdown from a path."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0
        assert "#" in result or "-" in result or "*" in result

    def test_document_path_to_markdown_with_pdf(self):
        """Test converting a PDF document to markdown from a path."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0
        assert "#" in result or "-" in result or "*" in result

    def test_docx_content_matches_known_text(self):
        """Converted DOCX output contains real document content, not just markdown syntax."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert self.KNOWN_CONTENT in result

    def test_pdf_content_matches_known_text(self):
        """Converted PDF output contains real document content, not just markdown syntax."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert self.KNOWN_CONTENT in result

    def test_consistent_with_binary_document_to_markdown(self):
        """Path-based and binary-based conversion produce the same result for the same file."""
        path_result = document_path_to_markdown(self.PDF_FIXTURE)
        with open(self.PDF_FIXTURE, "rb") as f:
            binary_result = binary_document_to_markdown(f.read(), "pdf")
        assert path_result == binary_result

    def test_is_deterministic(self):
        """Calling the tool twice on the same path returns identical output."""
        first = document_path_to_markdown(self.PDF_FIXTURE)
        second = document_path_to_markdown(self.PDF_FIXTURE)
        assert first == second

    def test_nonexistent_path_raises(self):
        """A path that doesn't exist should raise, not fail silently."""
        with pytest.raises(FileNotFoundError):
            document_path_to_markdown(os.path.join(self.FIXTURES_DIR, "does_not_exist.pdf"))

    def test_directory_path_raises(self):
        """A path that points at a directory should raise."""
        with pytest.raises((ValueError, IsADirectoryError)):
            document_path_to_markdown(self.FIXTURES_DIR)

    def test_empty_path_raises(self):
        """An empty path string should raise rather than being silently accepted."""
        with pytest.raises(ValueError):
            document_path_to_markdown("")

    def test_unsupported_extension_raises(self, tmp_path):
        """A file with an extension outside PDF/DOCX should raise."""
        txt_path = tmp_path / "notes.txt"
        txt_path.write_text("hello world")
        with pytest.raises(ValueError):
            document_path_to_markdown(str(txt_path))

    def test_missing_extension_raises(self, tmp_path):
        """A file with no extension at all should raise."""
        no_ext_path = tmp_path / "no_extension"
        no_ext_path.write_text("hello world")
        with pytest.raises(ValueError):
            document_path_to_markdown(str(no_ext_path))

    def test_corrupted_pdf_raises(self, tmp_path):
        """A truncated/corrupted PDF should raise a conversion error, not return garbage."""
        with open(self.PDF_FIXTURE, "rb") as f:
            truncated_bytes = f.read(50)
        bad_pdf_path = tmp_path / "truncated.pdf"
        bad_pdf_path.write_bytes(truncated_bytes)
        with pytest.raises(Exception):
            document_path_to_markdown(str(bad_pdf_path))

    def test_zero_byte_file_raises(self, tmp_path):
        """A zero-byte file with a valid extension should raise, not return an empty result."""
        empty_pdf_path = tmp_path / "empty.pdf"
        empty_pdf_path.write_bytes(b"")
        with pytest.raises(Exception):
            document_path_to_markdown(str(empty_pdf_path))

    def test_uppercase_extension(self, tmp_path):
        """Extension matching should be case-insensitive."""
        upper_path = tmp_path / "UPPER.PDF"
        upper_path.write_bytes(open(self.PDF_FIXTURE, "rb").read())
        result = document_path_to_markdown(str(upper_path))
        assert self.KNOWN_CONTENT in result

    def test_path_with_unicode_and_spaces(self, tmp_path):
        """Filenames with spaces and non-ASCII characters should work."""
        unicode_path = tmp_path / "héllo wörld 文档.pdf"
        unicode_path.write_bytes(open(self.PDF_FIXTURE, "rb").read())
        result = document_path_to_markdown(str(unicode_path))
        assert self.KNOWN_CONTENT in result

    def test_symlink_to_valid_file(self, tmp_path):
        """A symlink pointing at a valid document should resolve and convert correctly."""
        symlink_path = tmp_path / "linked.pdf"
        os.symlink(os.path.abspath(self.PDF_FIXTURE), symlink_path)
        result = document_path_to_markdown(str(symlink_path))
        assert self.KNOWN_CONTENT in result
