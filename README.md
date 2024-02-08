# Regex Generator

A Python tool for dynamically generating regex patterns from strings and bytes.

# RegexGen

`RegexGen` is a versatile Python tool designed to automatically generate regular expression (regex) patterns from given input data, which works with strings and bytes. This tool simplifies the process of creating regex patterns for various applications, including data validation, parsing, and extraction tasks.

## Features

- **Dynamic Regex Generation**: Automatically generates regex patterns for strings and byte sequences.
- **Custom Character Support**: Allows customization of regex patterns for specific characters.
- **Testing Utility**: Includes a method for testing generated regex patterns against provided or auto-generated data.

## Installation

To use `RegexGen`, clone this repository or download the source code. No external dependencies are required beyond the Python standard library.
```bash
git clone https://github.com/memoryapi/RegexGen/tree/main
```

## Usage

### Basic Usage

### Text Data
  ```python
  from RegexGenerator import RegexGenerator
  
  dataText = "Hello123 World!"
  rgText = RegexGenerator(dataText)
  regexText = rgText.generate()
  print(f"Generated Regex Pattern: {regexText}")
  ```
### Byte Data
  ```python
  from RegexGenerator import RegexGenerator
  
  dataBytes = b'\x00\x00\x00N\x00\t$\x93\x8d\x86S-|\xd94\xa2\x99@\x00\x00\x00'
  rgBytes = RegexGenerator(dataBytes)
  regexBytes = rgBytes.generate()
  print(f"Generated Regex Pattern: {regexBytes}")
  ```
### Custom Character Mapping
```python
customChars = {'H': '[Hh]', 'e': '[eE]', '!': '[!1]'}
rgCustom = RegexGenerator("Hello World!", customChars)
regexCustom = rgCustom.generate()
print(f"Generated Regex Pattern with Custom Characters: {regexCustom}")
```

### Testing Regex Patterns
```python
extractedText = rgText.test(regexText)
print(f"Extracted Text: {extractedText}")
```
##### [!} see main.py for test cases.

## Contributing

Contributions to `RegexGen` are welcome. Please feel free to submit pull requests or open issues to improve the tool or suggest new features.

## License

`RegexGen` is released under the MIT License. See the LICENSE file for more details.
