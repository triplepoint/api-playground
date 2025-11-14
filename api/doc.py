import mistune


def html() -> str:
    """Generate an HTML string suitable for displaying as the general API docs."""
    with open("APIDOC.md", encoding="utf-8") as f:
        md = f.read()
    return """<!DOCTYPE html>
<style>
    html { font-family: sans; background: #222; color: white; }
    a:visited { color: red; }
    code.language-mermaid svg { background: #AAA; }
    code.language-python { width: 1000px;}
</style>
<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: false });
    await mermaid.run({ querySelector: '.language-mermaid' });
</script>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/styles/default.min.css">
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/highlight.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/languages/python.min.js"></script>
<script>hljs.highlightAll();</script>
""" + str(mistune.html(md))
