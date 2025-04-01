# Random Joke Generator

<video controls>
    <source src="./demo.mp4" />
</video>

## Overview
This project is a simple Python application that generates random jokes using an external API. It is a fun way to explore working with APIs and handling JSON data in Python.

## Features

- Fetches random jokes from an online API.
- Displays jokes in a user-friendly format.
- Easy to set up and run.

## Live Demo
Check out the live version of this Random Joke Generator [here](https://random-jokes-generator.streamlit.app/).

## Requirements

- Python 3.x
- UV Package Manager

## Installation

To install Mode Tracker, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/syeda-hoorain-ali/ramzan-coding-nights.git
    ```
2. Navigate to the project directory:
    ```bash
    cd 11-random-jokes-generator
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

To start using the app, run the following command:
```bash
streamlit run src/app.py
```

## Joke API

This project uses the [Official Joke API](https://official-joke-api.appspot.com/random_joke) to fetch random jokes. You can explore the API documentation for more details.

## Example

Here’s an example of a random joke fetched by the application:

```
Q: Why don't skeletons fight each other?
A: They don't have the guts.
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Contact
For any questions or feedback, please contact us at [jagjets133@gmail.com](mailto:jagjets133@gmail.com).
