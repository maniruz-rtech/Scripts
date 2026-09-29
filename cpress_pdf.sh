#!/bin/bash

# Interactive PDF compression script using Ghostscript

echo "Select PDF compression type:"
echo "1) Screen (low quality, smallest size)"
echo "2) Ebook (medium quality, balanced)"
echo "3) Printer (high quality, larger size)"
echo "4) Prepress (very high quality, almost original size)"

read -p "Enter your choice (1/2/3/4): " choice

# Map user input to Ghostscript PDFSETTINGS
case $choice in
    1)
        setting="/screen"
        ;;
    2)
        setting="/ebook"
        ;;
    3)
        setting="/printer"
        ;;
    4)
        setting="/prepress"
        ;;
    *)
        echo "Invalid choice. Please run the script again and select 1, 2, 3, or 4."
        exit 1
        ;;
esac

# Create output folder
mkdir -p compressed_pdfs

# Compress all PDFs in current folder
for f in *.pdf; do
    if [ -f "$f" ]; then
        output="compressed_pdfs/$f"
        echo "Compressing $f → $output ..."
        gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=$setting -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$output" "$f"
    fi
done

echo "✅ All PDFs compressed! Check the 'compressed_pdfs' folder."
