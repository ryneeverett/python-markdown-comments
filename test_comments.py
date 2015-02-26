import unittest
import textwrap
import markdown
import mkdcomments


class TestComments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        comments = mkdcomments.CommentsExtension()
        cls.markdowner = markdown.Markdown(extensions=[comments])

    @classmethod
    def markdown(cls, multiline_string):
        return cls.markdowner.convert(textwrap.dedent(multiline_string))

    def test_inline(self):
        result = self.markdown('text <!---inline comment-->')
        self.assertEqual(result, '<p>text</p>')

    def test_inline_beginning_and_end(self):
        result = self.markdown(
            '<!---inline comment-->text<!---inline comment-->')
        self.assertEqual(result, '<p>text</p>')

    def test_full_line(self):
        result = self.markdown(
            """\
            text
            <!---this line is ommitted entirely-->
            more text""")
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

    def test_multiline(self):
        result = self.markdown(
            """\
            text  <!---multiline comment
            multiline comment
            multiline comment-->more text""")
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

    def test_multiline_beginning_inline(self):
        result = self.markdown(
            """\
            <!---inline comment-->text<!---multiline commment
            multiline comment-->
            more text""")
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

    def test_multiline_ending_inline(self):
        result = self.markdown(
            """\
            <!---multiline comment
            multiline comment-->text<!---inline comment-->""")
        self.assertEqual(result, '<p>text</p>')

    def test_multiline_ending_and_beginning_on_same_line(self):
        result = self.markdown(
            """\
            <!---multiline comment
            multiline comment-->text<!---multiline comment
            multiline comment-->
            more text
            """)
        expected_result = textwrap.dedent(
            """\
            <p>text</p>
            <p>more text</p>""")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
