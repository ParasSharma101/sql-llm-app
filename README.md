# sql-llm-app

## Overview
`sql-llm-app` is a Streamlit application that uses Google Generative AI to convert natural language questions into SQL queries and retrieve data from a SQLite database.

## Features
- Converts English questions to SQL queries using Google Generative AI.
- Retrieves data from a SQLite database based on the generated SQL queries.
- Displays the retrieved data in a user-friendly format using Streamlit.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/sql-llm-app.git
    cd sql-llm-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your Google API key in the `.env` file:
    ```env
    GOOGLE_API_KEY = "your-google-api-key"
    ```

## Usage
1. Run the SQLite setup script to create the database and insert sample records:
    ```sh
    python sqlite.py
    ```

2. Start the Streamlit application:
    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the application.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)