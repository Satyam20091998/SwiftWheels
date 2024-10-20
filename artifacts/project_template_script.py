import os

# Define the project structure with empty files and folders
project_structure = {
    "uber-clone-web-app": {
        "README.md": "",
        ".gitignore": "",
        "LICENSE": "",
        "frontend": {
            "package.json": "",
            "package-lock.json": "",
            "public": {
                "favicon.ico": "",
                "index.html": ""
            },
            "src": {
                "index.js": "",
                "App.js": "",
                "components": {},
                "pages": {},
                "services": {},
                "styles": {}
            }
        },
        "user-service": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app": {
                "__init__.py": "",
                "models.py": "",
                "routes.py": "",
                "controllers.py": "",
                "utils.py": "",
                "config.py": ""
            },
            "tests": {
                "test_models.py": "",
                "test_routes.py": ""
            }
        },
        "ride-service": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app": {
                "__init__.py": "",
                "models.py": "",
                "routes.py": "",
                "controllers.py": "",
                "utils.py": "",
                "config.py": ""
            },
            "tests": {
                "test_models.py": "",
                "test_routes.py": ""
            }
        },
        "driver-service": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app": {
                "__init__.py": "",
                "models.py": "",
                "routes.py": "",
                "controllers.py": "",
                "utils.py": "",
                "config.py": ""
            },
            "tests": {
                "test_models.py": "",
                "test_routes.py": ""
            }
        },
        "payment-service": {
            "Dockerfile": "",
            "requirements.txt": "",
            "app": {
                "__init__.py": "",
                "models.py": "",
                "routes.py": "",
                "controllers.py": "",
                "utils.py": "",
                "config.py": ""
            },
            "tests": {
                "test_models.py": "",
                "test_routes.py": ""
            }
        },
        "docker-compose.yml": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # If content is a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursive call for subdirectories
        else:  # If content is a file
            with open(path, 'w') as f:
                f.write(content)  # Create an empty file

# Create the project structure in the current directory
create_structure(os.getcwd(), project_structure)
print("Project structure created successfully.")
