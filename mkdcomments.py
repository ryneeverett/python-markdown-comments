"""
A Python-Markdown preprocessor extension to ignore html comments opened by
three dashes (<!---comment-->) and any whitespace prior to them. I believe
pandoc has similar functionality.

Note: This extension does not work with the markdownfromFile function or
the convertFile method. They raise a UnicodeDecodeError.

Note: If using multiple extensions, mkdcomments probably should be last in
the list. Markdown extensions are loaded into the OrderedDict from which they
are executed in the order of the extension list. If a different extension is
loaded after mkdcomments, it may insert itself before mkdcomments in the
OrderedDict. Undesirable results may ensue. If, for instance, the 'meta'
extension is executed before mkdcomments, any comments in the meta-data will be
included in meta's dictionary.
"""

import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class CommentsExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.preprocessors.add("comments", CommentsProcessor(md), "_begin")


class CommentsProcessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        is_multi = False
        for line in lines:
            if not is_multi:
                new_line, is_multi = self._uncommenter(line)
            else:
                new_line, is_multi = self._unmultiliner(line)
            new_lines.append(new_line)
        return new_lines

    def _uncommenter(self, line):
        # inline
        line = re.sub(r'\s*<!---.*?-->', '', line)

        # start multiline
        line, count = re.subn(r'\s*<!---.*', '', line)

        return line, bool(count)

    def _unmultiliner(self, line):
        new_line, count = re.subn(r'.*?-->', '', line, count=1)

        # end multiline
        if count > 0:
            return self._uncommenter(new_line)
        # continue multiline
        else:
            return ('', True)

def makeExtension(configs={}):
    return CommentsExtension(configs=configs)
