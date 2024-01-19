from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from src.components.text_extarct import ResumeTextExtractor
from src.components.API_extractor import generate_content
import os
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyApKK5BXpv6x41yTXubZnkkKBnQq4NLEbM")

user_name = "Darshan"
UPLOAD_FOLDER = f'uploads/{user_name}'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Create an instance of ResumeTextExtractor
        resume_text_extractor = ResumeTextExtractor()

        # Extract text from resumes
        preprocessed_text = resume_text_extractor.extract_text_from_resumes(folder_path=file_path)

        # Example usage:
        default_prompt = f"""
        Extract key elements from the provided research paper text. The paper falls under the [Science technology] category, and I need information on the following sections:
        - Title
        - Abstract
        - Introduction
        - Literature Review
        - Research Question/Hypothesis (if applicable)
        - Methodology
        - Results
        - Discussion
        - Conclusion
        - References
        - Ethical Considerations (if applicable)
        - Figures/Tables

        The paper text is as follows:
        "{preprocessed_text}"

        Provide detailed information for each section, summarizing the content and key findings. If a section is not present in the paper, indicate that it is not applicable.
        """

        result = generate_content(default_prompt)

        return render_template('upload_success.html', file_path=file_path, text=result)
    
    return redirect(request.url)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
