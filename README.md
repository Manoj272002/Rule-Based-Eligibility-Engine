
# Rule-Based Eligibility Engine

A simple, flexible rule engine implemented using Flask, designed to determine user eligibility based on a set of custom, configurable rules. This application parses rules expressed in natural language (like "age > 30 and department == 'Sales'") and evaluates them against user data provided in JSON format.

## Features

- **Dynamic Rule Creation:** Allows users to input eligibility rules through a web form, which are then parsed into an Abstract Syntax Tree (AST).
- **Rule Evaluation:** Evaluates data (in JSON format) against the defined rules and returns the eligibility result.
- **User-Friendly Interface:** Provides a clean, easy-to-use form interface for rule creation and evaluation.

## Technologies Used

- **Flask:** For creating the web interface and API endpoints.
- **Abstract Syntax Tree (AST):** For parsing and evaluating custom rules in a structured way.
- **Python Operators:** Used for implementing logical and comparison operators in eligibility rules.

## Installation
1. Install the required packages:
pip install Flask
2. **Run the Application:**
python app.py


The Flask server will start on `http://127.0.0.1:5000`. Open this URL in your browser to access the application.

## Usage

1. **Define a Rule:** Enter a rule in the form of a conditional statement (e.g., `(age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing')`).
2. **Evaluate Data:** Enter JSON data to test against the rule (e.g., `{"age": 35, "department": "Sales"}`) to see if the data meets the eligibility criteria.

### Example Rule and Data

**Rule:** `((age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing'))`

**JSON Data:** `{"age": 35, "department": "Sales", "salary": 60000, "experience": 6}`

## Project Structure

```plaintext
Rule-Based-Eligibility-Engine/
├── app.py                # Main Flask application with routes for rule creation and evaluation
├── rule_engine.py        # Contains ASTNode class and functions for rule creation and evaluation
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation
