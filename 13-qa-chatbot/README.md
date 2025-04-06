---
title: VioBot
emoji: 💜
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: false
license: mit
short_description: A Python-based chatbot designed for interactive and meaningful conversations.
---

## Overview
VioBot is a basic implementation of a chatbot built using Python. It leverages natural language processing techniques to provide interactive and meaningful conversations.

## Live
🔹 Live App: [huggingface.co/spaces/syedahoorainali/viobot](https://huggingface.co/spaces/syedahoorainali/viobot)

## Features

- Simple and intuitive chatbot interface.
- Built using Python for easy customization and scalability.
- Lightweight and efficient implementation.

## Prerequisites

- Python 3.8 or higher
- UV Package Manager
- Docker (if using the provided Docker setup)


## Installation

1. Clone the space:
    ```bash
    git clone https://huggingface.co/spaces/syedahoorainali/viobot
    ```
2. Navigate to the project directory:
    ```bash
    cd viobot
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
5. (Optional) Run using Docker:
    ```bash
    docker build -t viobot .
    docker run -p 5000:5000 viobot
    ```

## Usage

1. Run the chatbot script:
    ```bash
    chainlit run src/main.py -w
    ```
2. Interact with the chatbot through the web interface.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the open-source community for providing tools and libraries that made this project possible.