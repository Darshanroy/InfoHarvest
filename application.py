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

        selected_category = request.form.get('category')  # Get the selected category from the form

        # Create an instance of ResumeTextExtractor
        resume_text_extractor = ResumeTextExtractor()

        # Extract text from resumes
        preprocessed_text = resume_text_extractor.extract_text_from_resumes(folder_path=file_path)

        # Get the corresponding set of questions based on the selected category
        prompt_dict = {
            "Content Understanding": [
                "Summarize the key findings of the research paper.",
                "What is the main objective of the study described in the research paper?",
                "Provide an overview of the methodology used in the research."
            ],
            "Methodology and Experimentation": [
                "Describe the experimental design and methodology employed in the research.",
                "What data sources were used in the study?",
                "Explain the statistical methods or analysis techniques applied in the research."
            ],
            "Results and Analysis": [
                "Highlight the main results and outcomes presented in the paper.",
                "What trends or patterns were observed in the data analysis?",
                "Discuss the significance of the results in the context of the research objectives."
            ],
            "Limitations and Challenges": [
                "Identify and discuss any limitations mentioned in the research paper.",
                "What challenges or constraints were faced during the study?",
                "How might the limitations impact the generalizability of the findings?"
            ],
            "Comparisons and Contrasts": [
                "Compare the approach used in this research paper with other studies in the same field.",
                "Contrast the findings of this paper with those of a related work."
            ],
            "Future Work and Implications": [
                "Examine the recommendations or suggestions for future research provided in the paper.",
                "Discuss the potential real-world applications or implications of the research."
            ],
            "Technical Details": [
                "Explain any complex technical terms or concepts mentioned in the paper.",
                "Clarify the significance of specific algorithms or models used in the research."
            ],
            "Citations and References": [
                "Provide a list of key references cited in the research paper.",
                "Summarize the contributions of the most cited works in the bibliography."
            ],
            "Interdisciplinary Aspects": [
                "Explore any interdisciplinary connections or collaborations mentioned in the paper.",
                "How does the research contribute to multiple fields or disciplines?"
            ],
            "Ethical Considerations": [
                "Discuss any ethical considerations or implications mentioned in the paper.",
                "How does the research address potential ethical challenges in its approach?"
            ],
            "Review of Related Literature": [
                "Summarize the literature review section of the research paper.",
                "What gaps in existing research does this paper aim to fill?"
            ],
            "Critical Analysis": [
                "Provide a critical analysis of the methodology employed in the research.",
                "Discuss potential biases or limitations in the study design."
            ]
        }

        questions = prompt_dict.get(selected_category, [])  # Get the questions for the selected category

        # Check if "Own Prompt" is selected
        if selected_category == "Own Prompt":
            custom_prompt = request.form.get('customPrompt')
            questions = [custom_prompt] if custom_prompt else []

        # Example usage:
        default_prompt = f"""
        Extract key elements from the provided research paper text. The paper falls under the [{selected_category}] category, and I need information on the following sections:
        - {'        - '.join(questions)}

        The paper text is as follows:
        "{preprocessed_text}"

        Provide detailed information for each section, summarizing the content and key findings. If a section is not present in the paper, indicate that it is not applicable.
        just give sample text without any symobles like "*" ,"#"
        """

        result = generate_content(default_prompt)

        return render_template('upload_success.html', file_path=file_path, text=result)

    return redirect(request.url)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
