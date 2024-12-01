# Argilla Dataset Manager

A Python-based tool for managing and uploading datasets to Argilla, specifically designed for handling Q&A data from various sources like Confluence and Slack.

## Features

- Load and process CSV files containing Q&A data
- Configurable data processing and transformation
- Automated dataset creation and management in Argilla
- Robust logging system
- Support for custom metadata and field mapping

## Prerequisites

- Python 3.x
- Argilla server access
- Required CSV data files

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd argilla-dataset-manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Argilla credentials:
```env
ARGILLA_API_URL=your_argilla_api_url
ARGILLA_API_KEY=your_api_key
```

## Project Structure

```
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── utils/
│   ├── argilla_client.py  # Argilla API interaction functions
│   ├── data_loader.py     # Data loading utilities
│   ├── data_processor.py  # Data processing functions
│   └── logger.py          # Logging configuration
├── datasets/
│   └── dataset_settings.py # Dataset field configurations
└── requirements.txt       # Project dependencies
```

## Usage

1. Update the file paths in `main.py` to point to your CSV files:
```python
file_paths = {
    'confluence_qa_v2_df': 'path/to/your/csv/file.csv',
}
```

2. Configure dataset settings in `datasets/dataset_settings.py` if needed.

3. Run the application:
```bash
python main.py
```

## Data Format

The tool expects CSV files with the following columns:
- prompt
- response
- context
- keywords
- category
- references
- conversation_date
- source_platform

## Configuration

You can modify the following settings:
- Workspace name and dataset name in `main.py`
- Dataset field configurations in `datasets/dataset_settings.py`
- Logging settings in `utils/logger.py`

## Error Handling

The application includes comprehensive error handling and logging. Check the logs for any issues during execution.

## Contributing

Feel free to submit issues and enhancement requests.

## License

[Your chosen license]
