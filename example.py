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
""")

"""
Results:
>>> import example
>>> print example.test
<p>markdowntext1</p>
<p>markdowntext2</p>
<p>markdowntext3</p>
<p>markdowntext4</p>
<p>markdowntext5</p>
<p>markdowntext6</p>
<p>markdowntext7</p>
"""
