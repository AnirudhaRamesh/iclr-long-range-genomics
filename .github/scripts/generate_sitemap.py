import os
import glob
from datetime import datetime
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.dom import minidom

BASE_URL = "https://anirudharamesh.github.io/iclr-long-range-genomics"
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

def get_files():
    """Get all HTML, PDF, and other relevant files."""
    files = []
    for ext in ['*.html', '*.pdf']:
        files.extend(glob.glob(os.path.join(REPO_ROOT, "**", ext), recursive=True))
    return files

def get_priority(file_path):
    """Determine priority based on file path and type."""
    # Index page gets highest priority
    if file_path.endswith('index.html'):
        return '1.0'
    # PDFs get medium-high priority
    elif file_path.endswith('.pdf'):
        return '0.8'
    # Other HTML pages get medium priority
    elif file_path.endswith('.html'):
        return '0.8'
    # Default priority for other files
    return '0.5'

def generate_sitemap():
    # Create root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Add index page first
    index_url = ET.SubElement(urlset, 'url')
    ET.SubElement(index_url, 'loc').text = BASE_URL + '/'
    ET.SubElement(index_url, 'priority').text = '1.0'
    ET.SubElement(index_url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
    
    # Add all other files
    for file_path in get_files():
        # Skip the index page as it's already added
        if file_path.endswith('index.html'):
            continue
            
        rel_path = os.path.relpath(file_path, REPO_ROOT)
        # Skip files in .github directory
        if rel_path.startswith('.github'):
            continue
            
        url = ET.SubElement(urlset, 'url')
        file_url = f"{BASE_URL}/{rel_path}"
        ET.SubElement(url, 'loc').text = file_url
        ET.SubElement(url, 'priority').text = get_priority(file_path)
        ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
    
    # Create the XML string with proper formatting
    xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
    
    # Write to sitemap.xml
    with open(os.path.join(REPO_ROOT, 'sitemap.xml'), 'w') as f:
        f.write(xml_str)

if __name__ == '__main__':
    generate_sitemap() 