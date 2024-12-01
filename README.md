# Argilla Dataset Manager

A Python-based tool for managing and uploading datasets to Argilla, specifically designed for handling various types of text datasets with advanced configuration options.

## Features

- Easy dataset creation with predefined templates
- Flexible dataset configuration for different use cases
- Dataset migration and versioning
- Workspace management
- Robust error handling and logging

## Prerequisites

- Python 3.x
- Argilla server access
- Required CSV data files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jordanrburger/argilla_dataset_manager.git
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

## Quick Start

### 1. Create a Text Classification Dataset

```python
from utils import DatasetManager, get_argilla_client
from datasets import SettingsManager

# Initialize
client = get_argilla_client()
dataset_manager = DatasetManager(client)
settings_manager = SettingsManager()

# Create settings for text classification
settings = settings_manager.create_text_classification(
    labels=['positive', 'negative', 'neutral'],
    guidelines="Sentiment analysis dataset",
    include_metadata=True,
    metadata_fields=['source', 'confidence']
)

# Create dataset
dataset = dataset_manager.create_dataset(
    workspace="my_workspace",
    dataset="sentiment_analysis",
    settings=settings
)

# Add records
record = rg.Record(
    fields={
        "text": "This product is amazing!"
    },
    metadata={
        "source": "reviews",
        "confidence": 0.95
    }
)
dataset.records.log([record])
```

### 2. Create a Q&A Dataset

```python
# Create settings for Q&A dataset
settings = settings_manager.create_qa_dataset(
    include_context=True,
    include_keywords=True,
    include_references=True,
    guidelines="Customer support Q&A dataset"
)

# Create dataset
dataset = dataset_manager.create_dataset(
    workspace="support_workspace",
    dataset="customer_qa",
    settings=settings
)

# Add a Q&A record
record = rg.Record(
    fields={
        "question": "How do I reset my password?",
        "answer": "Click on 'Forgot Password' and follow the instructions.",
        "context": "User authentication flow",
        "keywords": "password,reset,auth",
        "references": "docs/auth.md"
    },
    metadata={
        "source": "support_tickets",
        "date": "2023-12-01"
    }
)
dataset.records.log([record])
```

### 3. Dataset Migration and Versioning

```python
# Create new version of existing dataset with updated settings
new_version = dataset_manager.update_dataset_settings(
    workspace="my_workspace",
    dataset="customer_qa",
    new_settings=updated_settings,
    create_new_version=True
)

# Clone dataset to different workspace
cloned_dataset = dataset_manager.clone_dataset(
    workspace="development",
    dataset="customer_qa",
    new_name="customer_qa_prod",
    new_workspace="production"
)
```

## Available Dataset Templates

The `SettingsManager` provides several predefined templates:

1. **Text Classification**
   - Basic text classification with customizable labels
   - Optional metadata fields

2. **Q&A Datasets**
   - Question and answer fields
   - Optional context, keywords, and references
   - Configurable metadata

3. **Text Generation**
   - Prompt and response fields
   - Optional prompt templates
   - Model-specific metadata

4. **Text Summarization**
   - Text and summary fields
   - Length and compression ratio tracking
   - Source tracking

5. **Custom Datasets**
   - Create datasets with custom fields
   - Flexible metadata configuration

## Project Structure

```
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── utils/
│   ├── argilla_client.py  # Argilla API interaction
│   ├── dataset_manager.py # Dataset management
│   ├── data_loader.py     # Data loading utilities
│   └── logger.py          # Logging configuration
├── datasets/
│   └── settings_manager.py # Dataset settings and templates
└── examples/              # Usage examples and tutorials
```

## Error Handling

The library includes comprehensive error handling:
- Connection validation
- Workspace existence checks
- Dataset creation validation
- Record format validation

## Contributing

Feel free to submit issues and enhancement requests.

## License

MIT License

Copyright (c) 2023 Jordan Burger

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
