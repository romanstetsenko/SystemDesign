# PDF Conversion Guide

This guide explains how to convert the `Rate Limiter.md` file (with Mermaid diagrams) to PDF format.

## Quick Start

### Option 1: Using the Batch Script (Windows)
1. Double-click `convert_to_pdf.bat`
2. If HTML file doesn't exist, it will be created automatically
3. The HTML file will open in your default browser
4. Press `Ctrl+P` to print
5. Choose "Save as PDF" as the printer
6. Save the PDF

### Option 2: Manual Conversion
1. Run the Python script:
   ```bash
   E:/repos/SystemDesign/.venv/Scripts/python.exe convert_to_pdf.py
   ```
2. Open `rate-limiter.html` in a web browser
3. Print to PDF using `Ctrl+P`

## Files Generated

- `rate-limiter.html` - Printable HTML version with styling
- `convert_to_pdf.py` - Python conversion script
- `convert_to_pdf.bat` - Windows batch file for easy conversion

## Mermaid Diagrams

The HTML file includes Mermaid diagrams as code blocks. To visualize them:

1. Copy the Mermaid code block from the HTML file
2. Visit [Mermaid Live Editor](https://mermaid.live/)
3. Paste the code to see the rendered diagram
4. Take a screenshot or use Mermaid's export features

## Browser Print Settings

For best results when printing to PDF:

- **Margins**: Choose "Narrow" or "Minimum"
- **Layout**: Portrait or Landscape (depending on content width)
- **Scale**: 90-100% (adjust if content is cut off)
- **Headers/Footers**: Usually disabled for cleaner output

## Alternative Online Tools

If you prefer not to use Python:

- [Sejda HTML to PDF](https://www.sejda.com/html-to-pdf)
- [HTML2PDF](https://html2pdf.com/)
- [PDFShift](https://pdfshift.io/)

## Troubleshooting

### Python script fails
- Ensure Python 3.13+ is installed
- Install required packages: `pip install markdown`
- Check that `Rate Limiter.md` exists in the current directory

### HTML doesn't look right
- Open the HTML file in a modern browser (Chrome, Firefox, Edge)
- Check browser console for any errors
- Ensure CSS is loading properly

### Mermaid diagrams not rendered
- This is expected - the HTML contains the Mermaid code
- Use external Mermaid tools to visualize
- Consider taking screenshots of rendered diagrams

## Manual Markdown to PDF

If you have Pandoc installed:
```bash
pandoc Rate Limiter.md -o Rate Limiter.pdf --pdf-engine=wkhtmltopdf
```

Note: This may not render Mermaid diagrams properly without additional plugins.
