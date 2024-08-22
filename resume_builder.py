from fpdf import FPDF
from fpdf.enums import XPos, YPos
import json

class PDFResume(FPDF):
    def __init__(self, data_file):
        super().__init__()
        self.load_data(data_file)
        self.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf')
        self.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf')
        self.set_font('DejaVu', '', 12)
        self.set_left_margin(15)  
        self.set_right_margin(15)  

    def header(self):
        self.set_font('DejaVu', 'B', 14)
        self.cell(0, 10, self.name, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.set_font('DejaVu', '', 12)
        self.cell(0, 10, f"Email: {self.email} | Phone: {self.phone} | LinkedIn: {self.linkedin} | GitHub: {self.github}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('DejaVu', '', 12)
        self.multi_cell(0, 10, text=body)
        self.ln(10)  

    def add_experience(self, experience):
        self.chapter_title('Experience')
        for exp in experience:
            self.set_font('DejaVu', 'B', 12)
            self.cell(0, 10, f"{exp['title']} - {exp['company']} ({exp['dates']})", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.set_font('DejaVu', '', 11)
            self.cell(0, 10, exp['location'], new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.ln(5)
            description = "\n".join(exp['description']) if isinstance(exp['description'], list) else exp['description']
            page_width = self.w - 2 * self.l_margin
            self.multi_cell(w=page_width, h=10, text=description)
            self.ln(10)  

    def add_projects(self, projects):
        self.chapter_title('Projects')
        for project in projects:
            self.set_font('DejaVu', 'B', 12)
            self.cell(0, 10, project['name'], new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.set_font('DejaVu', '', 12)
            description = "\n".join(project['description']) if isinstance(project['description'], list) else project['description']
            page_width = self.w - 2 * self.l_margin
            self.multi_cell(w=page_width, h=10, text=description)
            
            self.set_font('DejaVu', 'B', 12)
            technologies = ', '.join(project['technologies'])
            self.multi_cell(w=page_width, h=10, text=f"Technologies: {technologies}")
            self.ln(10)  

    def add_education(self, education):
        self.chapter_title('Education')
        for edu in education:
            self.set_font('DejaVu', 'B', 12)
            self.cell(0, 10, f"{edu['degree']} - {edu['institution']} ({edu['dates']})", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.set_font('DejaVu', '', 12)
            self.cell(0, 10, edu['location'], new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.ln(10)  

    def add_skills(self, skills):
        self.chapter_title('Skills')
        self.set_font('DejaVu', '', 12)
        self.multi_cell(0, 10, text=', '.join(skills))
        self.ln(10)  

    def load_data(self, data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
        self.name = data['name']
        self.email = data['contact']['email']
        self.phone = data['contact']['phone']
        self.linkedin = data['contact']['linkedin']
        self.github = data['contact']['github']
        self.summary = data['summary']
        self.experience = data['experience']
        self.education = data['education']
        self.skills = data['skills']
        self.projects = data.get('projects', [])

def create_resume(data_file):
    pdf = PDFResume(data_file)
    pdf.add_page()


    pdf.chapter_title('Summary')
    pdf.chapter_body(pdf.summary)

    pdf.add_projects(pdf.projects)

    pdf.add_education(pdf.education)

    pdf.add_skills(pdf.skills)

    pdf.add_experience(pdf.experience)

    # OUTPUT PDF
    pdf.output('resume.pdf')

if __name__ == "__main__":
    create_resume('data/resume_data.json')