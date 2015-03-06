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
>>> markdowner.convert("""\
... blah blah blah  <!--- inline comment -->
...
... <!---multiline comment
... multiline comment
... multiline comment-->
...
... even more text.""")
u'<p>blah blah blah</p>\n<p>even more text.</p>'
```

Infrequently Asked Questions
----------------------------

### How can I write about markdown comments without them being removed?

In order to render markdown comments, you must *(a)*use them in an html block (which are not processed as markdown) and *(b)*escape the brackets so the browser won't think they're html comments. E.g.:

```html
<pre>
&lt;!--- meta markdown comment --&gt;
</pre>
```
