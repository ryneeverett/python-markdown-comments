mkdcomments
===========

A [Python-Markdown](https://github.com/waylan/Python-Markdown) preprocessor extension to ignore html comments opened by three dashes (`<!---comment-->`) and any whitespace prior to them. I believe pandoc has similar functionality.

Usage Notes
-----------
+	This extension does not work with the `markdownfromFile` function or the `convertFile` method. They raise a UnicodeDecodeError.

+	If using multiple extensions, mkdcomments probably should be last in the list. Markdown extensions are loaded into the OrderedDict from which they are executed in the order of the extension list. If a different extension is loaded after mkdcomments, it may insert itself before mkdcomments in the OrderedDict. Undesirable results may ensue. If, for instance, the 'meta' extension is executed before mkdcomments, any comments in the meta-data will be included in meta's dictionary.


Example
-------
```python
>>> import markdown
>>> import mkdcomments
>>> comments = mkdcomments.CommentsExtension()
>>> markdowner = markdown.Markdown(extensions=[comments])
>>> print markdowner.convert("""\
... text  <!---inline comment-->
... <!---this line is ommitted entirely-->
... more text<!---multiline comment
... multiline comment
... multiline comment-->even more text
... """)
<p>text</p>
<p>more text></p>
<p>even more text</p>
```
