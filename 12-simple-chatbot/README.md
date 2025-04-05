---
title: Repeatie
emoji: 💜
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: false
license: mit
short_description: This project is basic implementation of chatbot using Python
---

# Simple Chatbot

This project is a basic implementation of a chatbot using Python. It demonstrates how to create a simple conversational bot that can respond to user inputs.

## Live
🔹 Live App: [huggingface.co/spaces/syedahoorainali/repeatie](https://huggingface.co/spaces/syedahoorainali/repeatie)

## Features

- Basic text-based interaction.
- Easy-to-understand code structure.
- Customizable responses.

## Prerequisites

- Python 3.x installed on your system.
- UV Package Manager

## Installation

1. Clone the space:
    ```bash
    git clone https://huggingface.co/spaces/syedahoorainali/repeatie
    ```
2. Navigate to the project directory:
    ```bash
    cd repeatie
    ```
3. Create and activate virtual environment:
    ```bash
    uv venv
    ./venv/Scripts/activate
    ```
4. Install the dependencies:
    ```bash
    uv pip install .
    ```

## Usage

1. Run the chatbot script:
    ```bash
    chainlit run src/main.py -w
    ```
2. Interact with the chatbot by typing your messages.

## Customization
You can modify the chatbot's responses by editing the `src/main.py` file. Add or update the response logic to suit your needs.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments
Inspired by the idea of creating simple and interactive Python projects.