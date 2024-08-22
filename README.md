# Resume

**Built with Python**

This Python project generates a PDF of a resume using the fpdf library. The resume is formatted with sections such as Summary, Projects, Education, Skills, and Experience. This version (v.1) features a _basic_ layout with minimal styling, using an imported font for text formatting.

### Project Overview

- The script `resume_builder.py` reads data from a JSON file (`resume_data.json`) and uses the fpdf library to create a formatted PDF resume.

### The resulting PDF includes:

- **Header**: Displays the name and contact information (email, phone, LinkedIn, GitHub).
- **Summary**: A brief overview of the individual's professional background and skills.
- **Projects**: Details of relevant projects, including descriptions and technologies used.
- **Education**: Educational background and qualifications.
- **Skills**: A list of skills and technologies.
- **Experience**: Professional work experience, including job titles, companies, dates, and descriptions.

## Files and Structure

- **resume_builder.py**: Main script to generate the resume.
- **data/resume_data.json**: JSON file containing sample resume data.
- **data/data_template.json**: A blank template for creating new resume data.

## How to Use

1. **Prepare Data**: Ensure either `resume_data.json` or `data_template.json` contains the correct information for the resume.
2. **Run Script**: Execute `resume_builder.py` to generate the resume PDF.
3. **View PDF**: Check the generated `resume.pdf` file in the same directory.

## Future Improvements

- Enhance the styling.
- Add support for multiple font styles and sizes.
- Include additional features such as sections for awards or certifications.
