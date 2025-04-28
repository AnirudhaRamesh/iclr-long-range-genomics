import os
import glob
from datetime import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom
from urllib.parse import quote

def debug_print(message):
    print(f"DEBUG: {message}")

def prettify_xml(elem):
    """Return a pretty-formatted XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

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
        
        # Get current date in YYYY-MM-DD format
        today = datetime.now().strftime('%Y-%m-%d')
        debug_print(f"Using date: {today}")
        
        # Add index page first
        index_url = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(index_url, 'loc')
        loc.text = BASE_URL + '/'
        
        lastmod = ET.SubElement(index_url, 'lastmod')
        lastmod.text = today
        
        changefreq = ET.SubElement(index_url, 'changefreq')
        changefreq.text = 'monthly'
        
        priority = ET.SubElement(index_url, 'priority')
        priority.text = '1.0'
        
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
                    
                    # Add URL to sitemap with proper URL encoding
                    url = ET.SubElement(urlset, 'url')
                    
                    # Properly encode the URL, replacing spaces with %20
                    encoded_path = quote(rel_path)
                    file_url = f"{BASE_URL}/{encoded_path}"
                    
                    loc = ET.SubElement(url, 'loc')
                    loc.text = file_url
                    
                    lastmod = ET.SubElement(url, 'lastmod')
                    lastmod.text = today
                    
                    changefreq = ET.SubElement(url, 'changefreq')
                    changefreq.text = 'monthly'
                    
                    priority = ET.SubElement(url, 'priority')
                    priority.text = '0.8' if file_path.endswith('.pdf') else '0.6'
                    
                    debug_print(f"Added URL: {file_url}")
                    
                except Exception as e:
                    debug_print(f"Error processing file {file_path}: {str(e)}")
        
        # Create XML with proper format
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_body = prettify_xml(urlset)
        
        # Remove the XML declaration from prettify_xml as we're adding our own
        if xml_body.startswith('<?xml'):
            xml_body = xml_body[xml_body.find('?>')+2:]
        
        xml_str = xml_declaration + xml_body
        
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