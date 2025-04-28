import os
import glob
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
from urllib.parse import quote

def debug_print(message):
    print(f"DEBUG: {message}")

def generate_sitemap():
    try:
        # Get the current directory (where the script is run from)
        current_dir = os.getcwd()
        debug_print(f"Current directory: {current_dir}")

        # Base URL for the website
        BASE_URL = "https://anirudharamesh.github.io/iclr-long-range-genomics"
        
        # Create root element
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        
        # Add index page first
        index_url = ET.SubElement(urlset, 'url')
        ET.SubElement(index_url, 'loc').text = BASE_URL + '/'
        ET.SubElement(index_url, 'priority').text = '1.0'
        ET.SubElement(index_url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
        
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
                    ET.SubElement(url, 'loc').text = file_url
                    ET.SubElement(url, 'priority').text = priority
                    ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
                    
                    debug_print(f"Added URL: {file_url}")
                    
                except Exception as e:
                    debug_print(f"Error processing file {file_path}: {str(e)}")
        
        # Create the XML string with proper formatting
        xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
        
        # Write to sitemap.xml
        sitemap_path = os.path.join(current_dir, 'sitemap.xml')
        with open(sitemap_path, 'w') as f:
            f.write(xml_str)
        
        debug_print(f"Sitemap written to: {sitemap_path}")
        
    except Exception as e:
        debug_print(f"Error generating sitemap: {str(e)}")
        raise

if __name__ == '__main__':
    generate_sitemap() 