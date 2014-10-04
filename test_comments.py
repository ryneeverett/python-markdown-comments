import unittest
import textwrap
import markdown
import mkdcomments


class TestComments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        comments = mkdcomments.CommentsExtension()
        cls.markdowner = markdown.Markdown(extensions=[comments])

    def test_inline(self):
        result = self.markdowner.convert('text <!---inline comment-->')
        self.assertEqual(result, '<p>text</p>')

    def test_inline_beginning_and_end(self):
        result = self.markdowner.convert(
            '<!---inline comment-->text<!---inline comment-->')
        self.assertEqual(result, '<p>text</p>')

    def test_full_line(self):
        result = self.markdowner.convert(textwrap.dedent(
            """\
            text
            <!---this line is ommitted entirely-->
            more text"""))
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

    def test_multiline(self):
        result = self.markdowner.convert(textwrap.dedent(
            """\
            text  <!---multiline comment
            multiline comment
            multiline comment-->more text"""))
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

    def test_multiline_beginning_inline(self):
        result = self.markdowner.convert(textwrap.dedent(
            """\
            <!---inline comment-->text<!---multiline commment
            multiline comment-->
            more text"""))
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

    def test_multiline_ending_inline(self):
        result = self.markdowner.convert(textwrap.dedent(
            """\
            <!---multiline comment
            multiline comment-->text<!---inline comment-->"""))
        self.assertEqual(result, '<p>text</p>')

    def test_multiline_ending_and_beginning_on_same_line(self):
        result = self.markdowner.convert(textwrap.dedent(
            """\
            <!---multiline comment
            multiline comment-->text<!---multiline comment
            multiline comment-->
            more text
            """))
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
