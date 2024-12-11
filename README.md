# Argilla Dataset Manager

A Python package for managing and uploading datasets to Argilla, providing a streamlined interface for dataset creation, configuration, and management.

## Installation

```bash
pip install argilla-dataset-manager
```

## Features

- Easy dataset creation and configuration
- Predefined templates for common dataset types
- Flexible settings management
- Built-in support for various data formats
- Type-safe implementation with mypy support

## Quick Start

```python
from argilla_dataset_manager.datasets import SettingsManager
from argilla_dataset_manager.utils import DatasetManager, get_argilla_client

# Initialize Argilla client
client = get_argilla_client()

# Create dataset managers
dataset_manager = DatasetManager(client)
settings_manager = SettingsManager()

# Create dataset settings
settings = settings_manager.create_text_classification(
    labels=["positive", "negative", "neutral"],
    guidelines="Classify the sentiment of the text",
    include_metadata=True
)

# Create dataset
dataset = dataset_manager.create_dataset(
    workspace="my_workspace",
    dataset="sentiment_analysis",
    settings=settings
)
```

## Package Structure

```
argilla_dataset_manager/
├── datasets/
│   ├── __init__.py
│   └── settings_manager.py      # Dataset settings and templates
├── utils/
│   ├── __init__.py
│   ├── argilla_client.py       # Argilla client configuration
│   ├── dataset_manager.py      # Dataset operations
│   ├── data_loader.py         # Data loading utilities
│   ├── data_processor.py      # Data processing utilities
│   └── logger.py              # Logging configuration
└── __init__.py
```

## Dataset Settings

The package provides several predefined dataset templates:

### Text Classification
```python
settings = settings_manager.create_text_classification(
    labels=["label1", "label2"],
    guidelines="Classification guidelines",
    include_metadata=True
)
```

### Question-Answer
```python
settings = settings_manager.create_qa_dataset(
    include_context=True,
    include_keywords=True,
    guidelines="QA dataset guidelines"
)
```

### Text Generation
```python
settings = settings_manager.create_text_generation(
    include_prompt_template=True,
    include_context=True,
    guidelines="Text generation guidelines"
)
```

### Text Summarization
```python
settings = settings_manager.create_text_summarization(
    include_metadata=True,
    include_keywords=True,
    guidelines="Text summarization guidelines"
)
```

## Environment Variables

Required environment variables:
```
ARGILLA_API_URL=your_argilla_instance_url
ARGILLA_API_KEY=your_api_key
HF_TOKEN=your_huggingface_token  # Optional, for private spaces
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/jordanrburger/argilla_dataset_manager.git
cd argilla_dataset_manager
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

4. Run tests:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
