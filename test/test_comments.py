import re
import pathlib
import unittest
import textwrap
import subprocess

import markdown
import mkdcomments


class TestComments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        comments = mkdcomments.CommentsExtension()
        cls.markdowner = markdown.Markdown(extensions=[comments])

    def assertExpectedMarkdown(self, md_input, expected_output):
        output = self.markdowner.convert(textwrap.dedent(md_input))
        expected = textwrap.dedent(expected_output)
        self.assertEqual(output, expected)

    def test_inline(self):
        md_input = 'text <!---inline comment-->'
        self.assertExpectedMarkdown(md_input, '<p>text</p>')

    def test_inline_beginning_and_end(self):
        md_input = '<!---inline comment-->text<!---inline comment-->'
        self.assertExpectedMarkdown(md_input, '<p>text</p>')

    def test_full_line(self):
        md_input = """\
            text
            <!---this line is ommitted entirely-->
            more text"""
        expected_result = """\
            <p>text</p>
            <p>more text</p>"""
        self.assertExpectedMarkdown(md_input, expected_result)

    def test_multiline(self):
        md_input = """\
            text  <!---multiline comment
            multiline comment
            multiline comment-->more text"""
        expected_result = """\
            <p>text</p>
            <p>more text</p>"""
        self.assertExpectedMarkdown(md_input, expected_result)

    def test_multiline_beginning_inline(self):
        md_input = """\
            <!---inline comment-->text<!---multiline commment
            multiline comment-->
            more text"""
        expected_result = """\
            <p>text</p>
            <p>more text</p>"""
        self.assertExpectedMarkdown(md_input, expected_result)

    def test_multiline_ending_inline(self):
        md_input = """\
            <!---multiline comment
            multiline comment-->text<!---inline comment-->"""
        self.assertExpectedMarkdown(md_input, '<p>text</p>')

    def test_multiline_ending_and_beginning_on_same_line(self):
        md_input = """\
            <!---multiline comment
            multiline comment-->text<!---multiline comment
            multiline comment-->
            more text
            """
        expected_result = """\
            <p>text</p>
            <p>more text</p>"""
        self.assertExpectedMarkdown(md_input, expected_result)

    def test_comments_in_html(self):
        """ See issue #2. """
        md_input = """\
            <pre>
                <!--- test --> testing code blocks
                    <!--- test --> testing 8 spaces
                 <!--- test --> testing 5 spaces
            </pre>"""
        self.assertExpectedMarkdown(md_input, md_input)

    def test_mkdocs(self):
        p = subprocess.run(
            ['mkdocs', 'build'], cwd=pathlib.Path('./test/mkdocsproject'))
        self.assertEqual(p.returncode, 0)


if __name__ == '__main__':
    unittest.main()
