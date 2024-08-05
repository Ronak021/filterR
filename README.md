
# FilterR - Data Table with Filters, Sorting, and Search

FilterR is a web application for displaying and manipulating data in a table format. It supports filtering, sorting, and searching functionality similar to Google Sheets, allowing users to interact with data effectively.

## Features

- **Filter Data**: Apply filters based on column types including integer, string, date, and boolean.
- **Sort Data**: Sort columns in ascending or descending order.
- **Search Data**: Search across multiple columns to find specific information.

## Technologies Used

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Flask (Python)
- **Libraries**:
  - Flask: Web framework
  - Jinja2: Templating engine


## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Ronak021/filterR.git
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd filterR
    ```

3. **Create a Virtual Enovironmennt**
    ```bash
    # install
    pip install virtualenv

    # create
    virtualenv env

    # activate
    .\env\Scripts\activate.ps1
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```


5. **Run the Application**:
    ```bash
    python .\app.py
    ```
