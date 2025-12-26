@echo off
REM Batch script to convert Markdown to PDF with rendered Mermaid diagrams
REM This will open the HTML file in your default browser for printing

echo Rate Limiter Documentation Converter
echo =====================================
echo.
echo This script will:
echo 1. Convert Rate Limiter.md to HTML
echo 2. Render Mermaid diagrams using Mermaid.js
echo 3. Open in your browser for PDF printing
echo.

REM Check if the HTML file exists
if exist "Rate Limiter.html" (
    echo ✅ HTML file found: Rate Limiter.html
    echo.
    echo Opening in default browser...
    start "" "Rate Limiter.html"
    echo.
    echo INSTRUCTIONS:
    echo 1. Wait for diagrams to render (1-2 seconds)
    echo 2. Press Ctrl+P to print
    echo 3. Select "Save as PDF" or "Print to PDF"
    echo 4. Use 'Narrow' margins for best results
    echo 5. Click "Save" or "Print"
    echo.
) else (
    echo ❌ HTML file not found. Running conversion script first...
    echo.
    E:/repos/SystemDesign/.venv/Scripts/python.exe convert_to_pdf.py
    if errorlevel 1 (
        echo.
        echo ❌ Conversion failed. Please check the errors above.
        exit /b 1
    )
    echo.
    echo Opening generated HTML file...
    start "" "Rate Limiter.html"
)

echo.
echo 💡 TIPS:
echo    • Mermaid diagrams render automatically using <pre class="mermaid"> tags
echo    • Uses Mermaid.js ESM module for modern browser support
echo    • Works offline after first CDN load
echo    • For editing: Modify Rate Limiter.md and re-run this script
echo    • Diagrams appear as visual flowcharts, not code blocks
echo.
echo Done!
pause
