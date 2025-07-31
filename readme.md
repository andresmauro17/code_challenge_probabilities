# CSV Data Processing and Database Storage

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library for python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/andresmauro17/code_challenge_probabilities
cd code_challenge_probabilities
```

2. Ensure you have the CSV file (`import_test.csv`) in the project directory

### Usage

Run the main script:
```bash
python main.py
```

The application will:
1. Create/recreate the SQLite database (`database.db`)
2. Process the CSV file (`import_test.csv`)
3. Insert all processed records into the database

Note: you can see logs in each step

### How to see the results

To see the results, just open the database.db  database with a sqlite client
    You can use this extension in vscode https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer



