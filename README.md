## Overview

Part of my Bachelor's Degree Project, this Python application is focused on **Artificial Intelligence (AI)**, with a strong emphasis on **Machine Learning (ML)**, **Semantic Search**, and related technologies. The project leverages advanced concepts such as **LangChain**, **VectorStore**, and **Embeddings** to build a robust, AI-driven solution.
The user is able to upload his PDFs and ask questions based on them using the **Conversational Chain** implementation. Also, there is a **Flashcard Generation** feature configured where flashcards can be obtained based on the text content that has been received by the PDF documents. A friendly flipping animation is used in order to showcase the other part of the flashcard with the answer of the question. The frontend text is in Romanian but can easily be translated.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Key Concepts](#key-concepts)
   - [Artificial Intelligence](#artificial-intelligence)
   - [Machine Learning](#machine-learning)
   - [Semantic Search](#semantic-search)
   - [LangChain](#langchain)
   - [VectorStore](#vectorstore)
   - [Embeddings](#embeddings)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

This project is designed to be a comprehensive exploration of modern AI technologies. It provides an in-depth look at how various components, such as machine learning models and semantic search algorithms, can be integrated to create intelligent systems.

The application is built using Python and includes a number of innovative features that demonstrate the power of AI. This README provides the necessary steps to install, use, and contribute to the project, along with detailed explanations of the key concepts involved.

## Project Structure

The project is organized into several key directories:

- **`authentication/`**: Contains the authentication logic, including the `auth.py` file.
- **`flashcards/`**: Manages the flashcards component, including the `cards.py` file.
- **`handlers/`**: Contains handlers such as `userinput.py` which manage user inputs.
- **`templates/`**: Holds the templates and components like `streamlit_components.py` and `template.html`.
- **`utils/`**: Utility functions and helpers, including the `inputs.py` file.
- **`main.py`**: The main entry point for the application.
- **`requirements.txt`**: Lists the Python dependencies for the project.

## Installation

To install and set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/razvanalexuc/The_Interactive_Learning_Platform_with_AI.git
2. **Create a virtual environment**:
  python3 -m venv env
  source env/bin/activate
3. **Install dependencies**
  pip install -r requirements.txt
4. **Run the app**
  In terminal, do the following: streamlit run main.py


## Key Concepts

### Artificial Intelligence
**Artificial Intelligence (AI)** refers to the simulation of human intelligence in machines that are designed to think and act like humans. This project incorporates AI to develop intelligent systems capable of performing complex tasks.

### Machine Learning
**Machine Learning (ML)** is a subset of AI that involves the use of algorithms and statistical models to enable machines to improve their performance on tasks through experience. This project includes various ML models that are trained to process data and make predictions.

### Semantic Search
**Semantic Search** is a search method that understands the contextual meaning of a query rather than relying solely on keyword matching. This application implements semantic search to provide more relevant and accurate search results.

### LangChain
**LangChain** is a framework that allows developers to build applications using language models in a modular way. It facilitates the integration of various language processing components to create cohesive AI-driven applications.

### VectorStore
**VectorStore** is a system for storing and retrieving vector embeddings, which are numerical representations of data that capture their semantic meaning. This application uses VectorStore to efficiently manage and query large volumes of vectorized data.

### Embeddings
**Embeddings** are dense vector representations of words or data points that capture their meanings or features in a high-dimensional space. This project utilizes embeddings for tasks like semantic search, classification, and clustering.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch**:
   ```bash
   git checkout -b feature/YourFeature
3. **Commit your changes**:
   git commit -m 'Add your feature'
4. **Push to the branch**:
   git push origin feature/YourFeature
5. **Create new Pull Request.**

## LICENSE
MIT License

Copyright (c) [2024] [Răzvan Alexuc]

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

