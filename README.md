# ConvertAPI Python Client

[![PyPI version](https://badge.fury.io/py/convertapi.svg)](https://badge.fury.io/py/convertapi)
[![Build Status](https://github.com/Nietzsche-Ubermensch/convertapi-library-python/actions/workflows/main.yml/badge.svg)](https://github.com/Nietzsche-Ubermensch/convertapi-library-python/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Convert your files with our online file conversion API

ConvertAPI helps to convert various file formats. Creating PDF and Images from various sources like Word, Excel, Powerpoint, images, web pages or raw HTML codes. Merge, Encrypt, Split, Repair and Decrypt PDF files and many other manipulations. You can integrate it into your application in just a few minutes and use it easily.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Proxy Configuration](#proxy-configuration)
  - [File Conversion](#file-conversion)
  - [Convert File URL](#convert-file-url)
  - [Specifying From Format](#specifying-from-format)
  - [Additional Conversion Parameters](#additional-conversion-parameters)
  - [User Information](#user-information)
  - [Alternative Domain](#alternative-domain)
- [Error Handling](#error-handling)
- [More Examples](#more-examples)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Installation

Install with [pip](https://pypi.org/project/pip/):

    pip install --upgrade convertapi

Install from source with:

    python setup.py install

### Requirements

* Python 3.8+

## Usage

### Configuration

You can get your API credentials at https://www.convertapi.com/a

```python
import convertapi

convertapi.api_credentials = 'api-token'
```

#### Proxy configuration

If you need to use a proxy, you can specify it using `HTTPS_PROXY` environment variable when running your script.

Example:

```
API_TOKEN=api-token HTTPS_PROXY=https://user:pass@127.0.0.1:9000/ python convert_word_to_pdf_and_png.py
```

### File conversion

Convert a file to PDF example. All supported file formats and options can be found
[here](https://www.convertapi.com/conversions).

```python
result = convertapi.convert('pdf', { 'File': '/path/to/my_file.docx' })

# save to file
result.file.save('/path/to/save/file.pdf')
```

Other result operations:

```python
# save all result files to folder
result.save_files('/path/to/save/files')

# get conversion cost
conversion_cost = result.conversion_cost
```

#### Convert file url

```python
result = convertapi.convert('pdf', { 'File': 'https://website/my_file.docx' })
```

#### Specifying from format

```python
result = convertapi.convert(
    'pdf',
    { 'File': '/path/to/my_file' },
    from_format = 'docx'
)
```

#### Additional conversion parameters

ConvertAPI accepts additional conversion parameters depending on selected formats. All conversion
parameters and explanations can be found [here](https://www.convertapi.com/conversions).

```python
result = convertapi.convert(
    'pdf',
    {
        'File': '/path/to/my_file.docx',
        'PageRange': '1-10',
        'PdfResolution': '150',
    }
)
```

### User information

You can always check your usage by fetching [user information](https://www.convertapi.com/doc/user).

```python
user_info = convertapi.user()

print(user_info['ConversionsTotal'])
print(user_info['ConversionsConsumed'])
```

### Alternative domain

Set `base_uri` parameter to use other service domains. Dedicated to the region [domain list](https://www.convertapi.com/doc/servers-location).

```python
convertapi.base_uri = 'https://eu-v2.convertapi.com/'
```

## Error Handling

ConvertAPI uses exceptions to handle errors. All API errors raise an `ApiError` exception that contains detailed information about what went wrong.

```python
import convertapi
from convertapi import ApiError

convertapi.api_credentials = 'your-api-token'

try:
    result = convertapi.convert('pdf', {'File': '/path/to/file.docx'})
    result.file.save('/path/to/output.pdf')
except ApiError as e:
    print(f"API Error: {e}")
    print(f"Error Code: {e.code}")
    print(f"Error Message: {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### More examples

Find more advanced examples in the [/examples](https://github.com/Nietzsche-Ubermensch/convertapi-library-python/tree/master/examples) folder.

## Troubleshooting

### Common Issues

#### Authentication Errors
- Ensure your API token is valid and has not expired
- Check that you've set `convertapi.api_credentials` before making any conversion calls
- Verify your account has sufficient conversion credits at https://www.convertapi.com/a

#### Timeout Issues
- For large files, increase the timeout: `convertapi.conversion_timeout = 300`
- Check your internet connection stability
- Consider using a region-specific domain for better performance

#### File Upload Errors
- Verify the file path is correct and the file exists
- Ensure you have read permissions for the file
- For large files, consider using file URLs instead of direct uploads

#### SSL Certificate Errors
- If behind a corporate proxy, you may need to set `convertapi.verify_ssl = False` (not recommended for production)
- Ensure your system's SSL certificates are up to date

### FAQ

**Q: How do I check my remaining conversion credits?**
```python
user_info = convertapi.user()
remaining = user_info['ConversionsTotal'] - user_info['ConversionsConsumed']
print(f"Remaining conversions: {remaining}")
```

**Q: Can I convert multiple files at once?**
Yes, use the `Files` parameter for batch conversions:
```python
files = ['file1.docx', 'file2.docx', 'file3.docx']
result = convertapi.convert('zip', {'Files': files})
```

**Q: How do I convert a file from a URL?**
```python
result = convertapi.convert('pdf', {'File': 'https://example.com/document.docx'})
```

**Q: How do I chain conversions?**
```python
# First convert DOCX to PDF
pdf_result = convertapi.convert('pdf', {'File': 'document.docx'})
# Then convert PDF to JPG
jpg_result = convertapi.convert('jpg', {'File': pdf_result})
```

## Development

Execute `API_TOKEN=api-token pytest` to run the tests.

For development setup:
```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests with coverage
pytest --cov=convertapi

# Run type checking
mypy convertapi

# Run linting
ruff check convertapi
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Nietzsche-Ubermensch/convertapi-library-python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This library is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
