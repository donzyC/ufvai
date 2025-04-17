# UFV AI Programming Department Proposal Website

A professional website proposing the establishment of a new AI Programming Department at the University of the Fraser Valley (UFV). This website serves as a feasibility study and marketing pitch to UFV stakeholders, faculty, students, and potential investors.

## Features

- Modern, responsive design
- Interactive UI elements
- Contact form functionality
- Smooth scrolling and animations
- Professional content structure
- Mobile-friendly layout

## Technology Stack

- Python 3.8+
- Flask (Web Framework)
- SQLite (Database)
- HTML5/CSS3
- JavaScript (ES6+)
- Tailwind CSS
- Font Awesome Icons

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd ufv-ai-proposal
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Deployment to GitHub Pages

This project is configured for deployment to GitHub Pages:

1. Push your code to a GitHub repository
2. Go to the repository settings
3. Navigate to "Pages" in the sidebar
4. Under "Source", select "GitHub Actions"
5. The site will be automatically deployed when you push to the main branch

The deployed site will be available at:
```
https://<your-github-username>.github.io/<repository-name>/
```

## Project Structure

```
ufv-ai-proposal/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/               # Static files
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── images/          # Image assets
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   └── ...             # Other pages
├── .github/              # GitHub configuration
│   └── workflows/        # GitHub Actions workflows
└── README.md            # Project documentation
```

## Content Sections

1. Home Page
2. Why This Department?
3. Problem & Opportunity
4. The Plan
5. AI, Ethics, and Society
6. Can AI Teach AI?
7. Interface, Access, and Security
8. Programming Section
9. Contact Form

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries, please contact:
- Email: ai.department@ufv.ca
- Website: https://www.ufv.ca 