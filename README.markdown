markdowncomments
================

A Python-Markdown preprocessor extension to ignore html comments opened by three dashes (`<!---comment-->`) and any whitespace prior to them. I believe pandoc has similar functionality.

Usage Notes
-----------
+	This extension does not work with the `markdownfromFile` function or the `convertFile` method. They raise a UnicodeDecodeError.

+	If using multiple extensions, mkdcomments probably should be last in the list. Markdown extensions are loaded into the OrderedDict from which they are executed in the order of the extension list. If a different extension is loaded after mkdcomments, it may insert itself before mkdcomments in the OrderedDict. Undesirable results may ensue. If, for instance, the 'meta' extension is executed before mkdcomments, any comments in the meta-data will be included in meta's dictionary.


Example
-------
```python
import markdown
import mkdcomments


comments = mkdcomments.CommentsExtension()
markdowner = markdown.Markdown(extensions=[comments])
test = markdowner.convert("""\
markdowntext1     <!---inline comment-->
<!---this line is ommitted entirely-->
markdowntext2        <!---multiline comment
multiline comment
multiline comment-->markdowntext3

<!---inline comment-->markdowntext4<!---inline comment-->

<!---inline comment-->markdowntext5<!---multiline commment
multiline comment-->
<!---multiline comment
multiline comment-->markdowntext6<!---unsupported comment-->
<!---multiline comment
multiline comment-->markdowntext7<!---multiline comment
multiline comment-->
```

Results:
```Python Traceback
>>> import example
>>> print example.test
<p>markdowntext1</p>
<p>markdowntext2</p>
<p>markdowntext3</p>
<p>markdowntext4</p>
<p>markdowntext5</p>
<p>markdowntext6</p>
<p>markdowntext7</p>
```
