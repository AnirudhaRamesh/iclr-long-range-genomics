import os
import glob
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
from urllib.parse import quote

def debug_print(message):
    print(f"DEBUG: {message}")

def clean_xml_output(xml_str):
    # Remove extra newlines and spaces
    import re
    # Replace multiple newlines with single newline
    xml_str = re.sub(r'\n\s*\n', '\n', xml_str)
    # Remove newlines and extra spaces between tags
    xml_str = re.sub(r'>\s*<', '><', xml_str)
    # Add newlines after closing tags for readability
    xml_str = re.sub(r'(<\/[^>]+>)([^<])', r'\1\n\2', xml_str)
    # Ensure proper XML declaration
    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str[xml_str.find('<urlset'):]
    return xml_str.strip()

def generate_sitemap():
    try:
        # Get the current directory (where the script is run from)
        current_dir = os.getcwd()
        debug_print(f"Current directory: {current_dir}")

        # Base URL for the website
        BASE_URL = "https://anirudharamesh.github.io/iclr-long-range-genomics"
        
        # Create root element with proper namespace
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        urlset.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        urlset.set('xsi:schemaLocation', 'http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd')
        
        # Get current date in YYYY-MM-DD format
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Add index page first
        index_url = ET.SubElement(urlset, 'url')
        ET.SubElement(index_url, 'loc').text = BASE_URL + '/'
        ET.SubElement(index_url, 'priority').text = '1.0'
        ET.SubElement(index_url, 'lastmod').text = today
        
        # Find all HTML and PDF files
        file_patterns = ['*.html', '*.pdf']
        for pattern in file_patterns:
            files = glob.glob(os.path.join(current_dir, "**", pattern), recursive=True)
            debug_print(f"Found {len(files)} files matching pattern {pattern}")
            for file_path in files:
                try:
                    # Skip index.html as it's already added
                    if os.path.basename(file_path) == 'index.html':
                        continue
                    
                    # Get relative path
                    rel_path = os.path.relpath(file_path, current_dir)
                    debug_print(f"Processing file: {rel_path}")
                    
                    # Skip hidden files and directories
                    if any(part.startswith('.') for part in rel_path.split(os.sep)):
                        continue
                    
                    # Determine priority
                    priority = '0.8' if file_path.endswith('.pdf') else '0.6'
                    
                    # Add URL to sitemap with proper URL encoding
                    url = ET.SubElement(urlset, 'url')
                    # Properly encode the URL, replacing spaces with %20
                    encoded_path = quote(rel_path)
                    file_url = f"{BASE_URL}/{encoded_path}"
                    loc = ET.SubElement(url, 'loc')
                    loc.text = file_url
                    pri = ET.SubElement(url, 'priority')
                    pri.text = priority
                    mod = ET.SubElement(url, 'lastmod')
                    mod.text = today
                    
                    debug_print(f"Added URL: {file_url}")
                    
                except Exception as e:
                    debug_print(f"Error processing file {file_path}: {str(e)}")
        
        # Create the XML string with proper formatting
        xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
        # Clean up the formatting
        xml_str = clean_xml_output(xml_str)
        
        # Write to sitemap.xml
        sitemap_path = os.path.join(current_dir, 'sitemap.xml')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        debug_print(f"Sitemap written to: {sitemap_path}")
        
    except Exception as e:
        debug_print(f"Error generating sitemap: {str(e)}")
        raise

if __name__ == '__main__':
    generate_sitemap() 