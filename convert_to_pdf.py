#!/usr/bin/env python3
"""
Convert Markdown file with Mermaid diagrams to PDF
Uses alternative methods since WeasyPrint has dependencies issues on Windows
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

def create_printable_html(md_content):
    """Create a printable HTML version of the Markdown content"""
    # Extract mermaid blocks for reference
    mermaid_blocks = extract_mermaid_blocks(md_content)
    
    # Replace mermaid blocks with formatted text representations
    clean_md = md_content
    for i, block in enumerate(mermaid_blocks):
        # Create a readable representation of the mermaid diagram
        diagram_info = f"\n\n**Mermaid Diagram {i+1}:**\n\n```\n{block}\n```\n\n*Note: This is the Mermaid code. Copy it to a Mermaid renderer to visualize.*\n\n"
        # Replace the mermaid block
        pattern = r'```mermaid\s*\n.*?\n```'
        clean_md = re.sub(pattern, diagram_info, clean_md, 1)
    
    # Convert to HTML
    html_content = markdown(clean_md, extensions=['extra', 'codehilite', 'tables'])
    
    # Create styled HTML
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Rate Limiter Documentation</title>
        <style>
            @media print {{
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.5;
                    color: #000;
                    margin: 0.5in;
                    font-size: 11pt;
                }}
                h1 {{
                    font-size: 20pt;
                    color: #0066cc;
                    border-bottom: 2px solid #0066cc;
                    padding-bottom: 5px;
                    margin-bottom: 15px;
                }}
                h2 {{
                    font-size: 16pt;
                    color: #0066cc;
                    margin-top: 20px;
                    margin-bottom: 10px;
                    border-bottom: 1px solid #ccc;
                    padding-bottom: 3px;
                }}
                h3 {{
                    font-size: 14pt;
                    color: #333;
                    margin-top: 15px;
                    margin-bottom: 8px;
                }}
                code {{
                    background: #f5f5f5;
                    padding: 2px 4px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                    font-size: 10pt;
                }}
                pre {{
                    background: #f5f5f5;
                    padding: 10px;
                    border-radius: 4px;
                    border-left: 3px solid #0066cc;
                    overflow-x: auto;
                    page-break-inside: avoid;
                }}
                blockquote {{
                    border-left: 4px solid #0066cc;
                    padding-left: 15px;
                    margin: 12px 0;
                    color: #555;
                    background: #f9f9f9;
                    font-style: italic;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 12px 0;
                    page-break-inside: avoid;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 6px;
                    text-align: left;
                    font-size: 10pt;
                }}
                th {{
                    background-color: #0066cc;
                    color: white;
                    font-weight: bold;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
                ul, ol {{
                    margin-left: 20px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                }}
                li {{
                    margin-bottom: 4px;
                }}
                a {{
                    color: #0066cc;
                    text-decoration: none;
                }}
                .mermaid-code {{
                    background: #f0f8ff;
                    border: 1px dashed #0066cc;
                    padding: 12px;
                    margin: 12px 0;
                    border-radius: 4px;
                    page-break-inside: avoid;
                }}
                .mermaid-code strong {{
                    color: #0066cc;
                    display: block;
                    margin-bottom: 8px;
                }}
                .mermaid-code pre {{
                    background: white;
                    border: none;
                    margin: 0;
                    padding: 0;
                    font-size: 9pt;
                }}
                .mermaid-code em {{
                    color: #666;
                    font-size: 9pt;
                    display: block;
                    margin-top: 8px;
                }}
                hr {{
                    border: none;
                    border-top: 1px solid #ccc;
                    margin: 20px 0;
                }}
                .header {{
                    text-align: center;
                    margin-bottom: 30px;
                    padding-bottom: 15px;
                    border-bottom: 2px solid #0066cc;
                }}
                .footer {{
                    text-align: center;
                    font-size: 9pt;
                    color: #666;
                    margin-top: 30px;
                    padding-top: 10px;
                    border-top: 1px solid #ccc;
                }}
            }}
            
            /* Screen display styles */
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #2c3e50;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
            }}
            h1 {{ border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            h2 {{ border-bottom: 1px solid #bdc3c7; padding-bottom: 5px; }}
            code {{
                background: #f8f9fa;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            pre {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #3498db;
                overflow-x: auto;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 15px;
                margin: 15px 0;
                color: #555;
                background: #f8f9fa;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 15px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            .mermaid-code {{
                background: #e8f4f8;
                border: 2px dashed #3498db;
                padding: 15px;
                margin: 15px 0;
                border-radius: 5px;
            }}
            .mermaid-code strong {{
                color: #3498db;
                display: block;
                margin-bottom: 8px;
            }}
            .mermaid-code em {{
                color: #666;
                font-size: 0.9em;
                display: block;
                margin-top: 8px;
            }}
            hr {{
                border: none;
                border-top: 1px solid #bdc3c7;
                margin: 20px 0;
            }}
            ul, ol {{
                margin-left: 20px;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 15px;
                border-bottom: 2px solid #3498db;
            }}
            .footer {{
                text-align: center;
                font-size: 0.9em;
                color: #666;
                margin-top: 30px;
                padding-top: 10px;
                border-top: 1px solid #bdc3c7;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Rate Limiter Documentation</h1>
            <p style="color: #666; margin: 0;">Generated from Rate Limiter.md</p>
        </div>
        
        {html_content}
        
        <div class="footer">
            <p>Generated on: {Path('Rate Limiter.md').stat().st_mtime if Path('Rate Limiter.md').exists() else 'N/A'}</p>
            <p>{len(mermaid_blocks)} Mermaid diagram(s) included as code blocks</p>
            <p>For visualization, copy Mermaid code to: https://mermaid.live/</p>
        </div>
    </body>
    </html>
    """
    
    # Replace mermaid blocks in HTML with styled divs
    for i, block in enumerate(mermaid_blocks):
        # Find and replace the mermaid code blocks in the HTML
        mermaid_div = f'''
        <div class="mermaid-code">
            <strong>Mermaid Diagram {i+1}</strong>
            <pre>{block}</pre>
            <em>Copy this code to mermaid.live to visualize</em>
        </div>'''
        
        # Replace the markdown code block representation in HTML
        # The markdown conversion creates <pre><code> blocks for the code
        old_pattern = f'<pre><code>{re.escape(block)}</code></pre>'
        # But we need to handle the fact that markdown might have escaped some characters
        # Let's use a more flexible approach
        styled_html = styled_html.replace(
            f'<pre><code>{block}</code></pre>',
            mermaid_div
        )
    
    return styled_html

def create_html_file(html_content, output_path):
    """Save HTML content to file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ HTML file created: {output_path}")

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
    
    print("🔄 Converting Markdown to printable HTML...")
    html_content = create_printable_html(md_content)
    
    print("💾 Saving HTML file...")
    create_html_file(html_content, html_output)
    
    print("\n" + "="*60)
    print("✅ SUCCESS! HTML file generated successfully")
    print("="*60)
    print(f"📄 HTML file: {html_output.absolute()}")
    print(f"📊 File size: {html_output.stat().st_size / 1024:.1f} KB")
    print()
    print("📋 NEXT STEPS TO CREATE PDF:")
    print("   1. Open the HTML file in your web browser")
    print("   2. Use browser's Print function (Ctrl+P or Cmd+P)")
    print("   3. Choose 'Save as PDF' or 'Print to PDF' in the printer dropdown")
    print("   4. Adjust margins if needed (I recommend 'Narrow' or 'Minimum')")
    print("   5. Save the PDF")
    print()
    print("💡 ALTERNATIVE: You can also use online tools like:")
    print("   - https://www.sejda.com/html-to-pdf")
    print("   - https://html2pdf.com/")
    print()
    print("🔧 For Mermaid diagrams, visit: https://mermaid.live/")
    print("   Paste the Mermaid code blocks to visualize them")
    print("="*60)

if __name__ == "__main__":
    main()
