import os
import shutil

def create_project_template(project_name):
    # Define the directory structure
    template_structure = {
        'src': ['__init__.py'],
        'src/components':['__init__.py','text_extarct.py'],
        'uploads': [],
        'docs': [],
        'tests': [],
        'config': ['config.ini'],
        'README.md': '',
        'requirements.txt': ''
    }

    # Create the project directory
    project_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_path, exist_ok=True)

    # Create the directory structure and files
    for item, content in template_structure.items():
        item_path = os.path.join(project_path, item)

        if isinstance(content, list):
            os.makedirs(item_path, exist_ok=True)
            for file in content:
                with open(os.path.join(item_path, file), 'w') as f:
                    pass
        elif isinstance(content, str):
            with open(item_path, 'w') as f:
                f.write(content)
        else:
            os.makedirs(item_path, exist_ok=True)

    print(f"Project template '{project_name}' created successfully at '{project_path}'.")

if __name__ == "__main__":
    project_name = input("Enter the name of your project: ")
    create_project_template(project_name)
