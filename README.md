mkdcomments
===========

A [Python-Markdown](https://github.com/waylan/Python-Markdown) preprocessor extension to ignore html comments opened by three dashes and any whitespace prior to them. I believe pandoc has similar functionality.

```html
<!-- This is a standard html comment which will remain in the output. -->
<!--- This is a markdown comment which this extension removes. -->
```

Installation
------------

```sh
pip install git+https://github.com/ryneeverett/python-markdown-comments.git
```

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
