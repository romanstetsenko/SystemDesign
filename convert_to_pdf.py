#!/usr/bin/env python3
"""
Convert Markdown file with Mermaid diagrams to HTML
Uses Mermaid.js to render diagrams directly in the browser
"""

import re
import sys
from pathlib import Path
from markdown import markdown

def extract_mermaid_blocks(content):
    """Extract Mermaid code blocks from Markdown content"""
    pattern = r'```mermaid\s*\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)
    return matches

def create_html_with_mermaid(md_content):
    """Create HTML with embedded Mermaid.js for diagram rendering"""
    # Extract mermaid blocks
    mermaid_blocks = extract_mermaid_blocks(md_content)
    
    # Split content by mermaid blocks and process each segment
    segments = []
    last_end = 0
    
    # Find all mermaid blocks and their positions
    pattern = r'```mermaid\s*\n(.*?)\n```'
    matches = list(re.finditer(pattern, md_content, re.DOTALL))
    
    for i, match in enumerate(matches):
        # Add the text before this mermaid block
        before_text = md_content[last_end:match.start()]
        if before_text.strip():
            segments.append(('markdown', before_text))
        
        # Add the mermaid block
        mermaid_code = match.group(1)
        segments.append(('mermaid', mermaid_code))
        
        last_end = match.end()
    
    # Add remaining text after last mermaid block
    remaining = md_content[last_end:]
    if remaining.strip():
        segments.append(('markdown', remaining))
    
    # Convert markdown segments to HTML
    html_parts = []
    for seg_type, content in segments:
        if seg_type == 'markdown':
            # Convert markdown to HTML
            converted = markdown(content, extensions=['extra', 'codehilite', 'tables'])
            html_parts.append(converted)
        else:  # mermaid
            # Add as pre class="mermaid"
            html_parts.append(f'<pre class="mermaid">\n{content}\n</pre>')
    
    html_content = ''.join(html_parts)
    
    # Build the complete HTML in parts to avoid f-string issues
    html_parts = []
    html_parts.append('<!DOCTYPE html>')
    html_parts.append('<html lang="en">')
    html_parts.append('<head>')
    html_parts.append('<meta charset="UTF-8">')
    html_parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html_parts.append('<title>Rate Limiter Documentation</title>')
    html_parts.append('<script type="module" src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs"></script>')
    html_parts.append('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">')
    html_parts.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>')
    html_parts.append('<style>')
    html_parts.append('body {font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; background: #ffffff;}')
    html_parts.append('h1 {font-size: 2.2em; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 20px; color: #2c3e50;}')
    html_parts.append('h2 {font-size: 1.6em; border-bottom: 1px solid #bdc3c7; padding-bottom: 5px; margin-top: 25px; color: #2c3e50;}')
    html_parts.append('h3 {font-size: 1.3em; color: #34495e; margin-top: 20px;}')
    html_parts.append('p {margin: 12px 0;}')
    html_parts.append('code {background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: "Courier New", monospace; font-size: 0.95em; color: #c7254e;}')
    html_parts.append('pre {background: #f8f9fa; padding: 15px; border-radius: 5px; border-left: 4px solid #3498db; overflow-x: auto; margin: 15px 0;}')
    html_parts.append('blockquote {border-left: 4px solid #3498db; padding-left: 15px; margin: 15px 0; color: #555; background: #f8f9fa; font-style: italic;}')
    html_parts.append('table {border-collapse: collapse; width: 100%; margin: 15px 0;}')
    html_parts.append('th, td {border: 1px solid #ddd; padding: 10px; text-align: left;}')
    html_parts.append('th {background-color: #3498db; color: white; font-weight: bold;}')
    html_parts.append('tr:nth-child(even) {background-color: #f9f9f9;}')
    html_parts.append('ul, ol {margin-left: 25px; margin-top: 10px; margin-bottom: 10px;}')
    html_parts.append('li {margin-bottom: 6px;}')
    html_parts.append('a {color: #3498db; text-decoration: none;}')
    html_parts.append('a:hover {text-decoration: underline;}')
    html_parts.append('.mermaid {margin: 25px 0; padding: 20px; background: #f8f9fa; border: 2px solid #3498db; border-radius: 8px; text-align: center;}')
    html_parts.append('.header {text-align: center; margin-bottom: 30px; padding-bottom: 20px; border-bottom: 3px solid #3498db;}')
    html_parts.append('.footer {text-align: center; font-size: 0.85em; color: #666; margin-top: 40px; padding-top: 20px; border-top: 1px solid #bdc3c7;}')
    html_parts.append('@media print {')
    html_parts.append('body {font-family: Arial, sans-serif; line-height: 1.5; color: #000; margin: 0.5in; font-size: 11pt; max-width: 100%;}')
    html_parts.append('h1 {font-size: 18pt; color: #0066cc; border-bottom: 2px solid #0066cc; padding-bottom: 5px; margin-bottom: 15px;}')
    html_parts.append('h2 {font-size: 14pt; color: #0066cc; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid #ccc; padding-bottom: 3px;}')
    html_parts.append('h3 {font-size: 12pt; color: #333; margin-top: 15px; margin-bottom: 8px;}')
    html_parts.append('code {background: #f5f5f5; padding: 1px 3px; border-radius: 2px; font-size: 10pt;}')
    html_parts.append('pre {background: #f5f5f5; padding: 8px; border-radius: 3px; border-left: 2px solid #0066cc; page-break-inside: avoid;}')
    html_parts.append('blockquote {border-left: 3px solid #0066cc; padding-left: 10px; margin: 10px 0; background: #f9f9f9;}')
    html_parts.append('table {border-collapse: collapse; width: 100%; margin: 10px 0; page-break-inside: avoid;}')
    html_parts.append('th, td {border: 1px solid #ddd; padding: 6px; font-size: 10pt;}')
    html_parts.append('th {background-color: #0066cc; color: white;}')
    html_parts.append('ul, ol {margin-left: 15px; margin-top: 8px; margin-bottom: 8px;}')
    html_parts.append('.mermaid {margin: 15px 0; padding: 10px; background: #f0f0f0; border: 1px solid #ccc; page-break-inside: avoid;}')
    html_parts.append('.header, .footer {display: none;}')
    html_parts.append('.mermaid svg {max-width: 100% !important; height: auto !important;}')
    html_parts.append('}')
    html_parts.append('</style>')
    html_parts.append('</head>')
    html_parts.append('<body>')
    html_parts.append('<div class="header">')
    html_parts.append('<h1>Rate Limiter Documentation</h1>')
    html_parts.append('<p>Generated from Rate Limiter.md</p>')
    html_parts.append('<p style="font-size: 0.85em; color: #888;">Mermaid diagrams are rendered below</p>')
    html_parts.append('</div>')
    html_parts.append('<div id="content">')
    html_parts.append(html_content)
    html_parts.append('</div>')
    html_parts.append('<div class="footer">')
    html_parts.append(f'<p>Generated: {Path("Rate Limiter.md").stat().st_mtime if Path("Rate Limiter.md").exists() else "N/A"}</p>')
    html_parts.append(f'<p>{len(mermaid_blocks)} Mermaid diagram(s) rendered with Mermaid.js</p>')
    html_parts.append('<p>For printing: Use Ctrl+P and select "Save as PDF"</p>')
    html_parts.append('</div>')
    html_parts.append('<script>')
    html_parts.append('// Initialize Mermaid with startOnLoad: true as per instructions')
    html_parts.append('mermaid.initialize({ startOnLoad: true, theme: "default", securityLevel: "loose" });')
    html_parts.append('</script>')
    html_parts.append('<script>')
    html_parts.append('// Highlight code blocks (non-mermaid)')
    html_parts.append('document.addEventListener("DOMContentLoaded", function() {')
    html_parts.append('var blocks = document.querySelectorAll("pre code");')
    html_parts.append('for (var i = 0; i < blocks.length; i++) {')
    html_parts.append('if (typeof hljs !== "undefined" && !blocks[i].classList.contains("mermaid")) {')
    html_parts.append('hljs.highlightElement(blocks[i]);')
    html_parts.append('}')
    html_parts.append('}')
    html_parts.append('});')
    html_parts.append('</script>')
    html_parts.append('</body>')
    html_parts.append('</html>')
    
    return '\n'.join(html_parts)

def main():
    """Main conversion function"""
    input_file = Path("Rate Limiter.md")
    html_output = Path("Rate Limiter.html")
    
    if not input_file.exists():
        print(f"❌ Error: Input file {input_file} not found")
        sys.exit(1)
    
    print(f"📖 Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print("🔄 Converting Markdown to HTML with Mermaid.js rendering...")
    html_content = create_html_with_mermaid(md_content)
    
    print("💾 Saving HTML file...")
    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("\n" + "="*60)
    print("✅ SUCCESS! HTML file generated successfully")
    print("="*60)
    print(f"📄 HTML file: {html_output.absolute()}")
    print(f"📊 File size: {html_output.stat().st_size / 1024:.1f} KB")
    print()
    print("📋 INSTRUCTIONS:")
    print("   1. Open the HTML file in your web browser")
    print("   2. Mermaid diagrams will render automatically")
    print("   3. To create PDF: Press Ctrl+P → Choose 'Save as PDF'")
    print("   4. For best results: Use 'Narrow' margins in print settings")
    print()
    print("💡 TIPS:")
    print("   • Works offline after first load (CDN cached)")
    print("   • Diagrams print perfectly to PDF")
    print("   • No need to copy/paste Mermaid code")
    print("="*60)

if __name__ == "__main__":
    main()
