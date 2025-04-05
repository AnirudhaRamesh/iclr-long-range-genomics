# State Space Models in Long Range Genomics - Project Website

This repository contains the website for our ICLR 2025 Workshop paper "Leveraging State Space Models in Long Range Genomics".

## Website Overview

The website showcases our research on using State-Space Models (SSMs) for genomic sequence modeling, highlighting:

- Performance comparison between SSMs (Caduceus, Hawk) and transformer-based models (NTv2)
- Zero-shot extrapolation capabilities to longer sequences
- Processing of ultralong sequences (1Mbp+) on a single GPU

## Design & Structure

The website follows a clean, academic design inspired by modern research project websites. It features:

- Responsive single-page layout with clear sections
- Interactive figures from the paper
- Mobile-friendly design
- BibTeX citation for easy referencing
- Author information with affiliations

## Local Development

To run this website locally:

1. Clone this repository
2. Navigate to the project folder
3. Run a local server:
   ```
   python -m http.server 8000
   ```
4. Open your browser to `http://localhost:8000`

No build process is required as this is a static website.

## Deploying to GitHub Pages

To deploy this website to GitHub Pages:

1. Run the included setup script:
   ```
   ./setup-github.sh
   ```
   
2. Follow the instructions provided by the script to:
   - Create a GitHub repository
   - Connect your local repository
   - Enable GitHub Pages in the repository settings

Your website will be available at `https://yourusername.github.io/your-repo-name/`

## Customization

- `index.html`: Main structure and content
- `style.css`: Styling and visual design
- `script.js`: JavaScript for smooth scrolling
- `images/`: Contains all figures from the paper
- `assets/`: Contains the favicon and other assets

## Contact

For questions about this website or the research, please contact:
- Anirudha Ramesh (a.ramesh@instadeep.com) 