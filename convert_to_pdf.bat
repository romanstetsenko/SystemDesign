@echo off
REM Batch script to convert Markdown to PDF
REM This will open the HTML file in your default browser for printing

echo Rate Limiter Documentation Converter
echo =====================================
echo.

REM Check if the HTML file exists
if exist "Rate Limiter.html" (
    echo ✅ HTML file found: Rate Limiter.html
    echo.
    echo Opening in default browser...
    start "" "Rate Limiter.html"
    echo.
    echo INSTRUCTIONS:
    echo 1. When the browser opens, press Ctrl+P (or Cmd+P on Mac)
    echo 2. Select "Save as PDF" or "Print to PDF" as the printer
    echo 3. Choose your preferred settings (margins, layout, etc.)
    echo 4. Click "Save" or "Print"
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

echo Done!
pause
