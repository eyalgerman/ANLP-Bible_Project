
# README for main_langchain_RAG.ipynb

## Overview

This Jupyter Notebook is designed to preprocess text data, create embeddings, and implement retriever models for Hebrew and English texts. It includes experiments to evaluate model performance on various datasets, primarily focused on text retrieval and question answering tasks.

## Table of Contents

1. [Installation](#installation)
2. [Data Preprocessing](#data-preprocessing)
3. [Creating Embeddings](#creating-embeddings)
4. [Retriever Models](#retriever-models)
5. [Chain of Thought (CoT) Templates](#chain-of-thought-cot-templates)
6. [Experiments](#experiments)
7. [Results](#results)
8. [Usage](#usage)

## Installation

To run the notebook, you need to install the following dependencies:

```bash
!pip install -qU langchain-ai21
!pip install langchain langchain-ai21 requests
!pip install transformers
!pip install huggingface_hub
!pip install pandas
```

## Data Preprocessing

The notebook includes functions to preprocess text data, specifically focusing on Hebrew text.

### Remove Cantillation Marks

The function `remove_cantillation` removes cantillation marks and nikkud (vowel points) from Hebrew text.

### Fetch Torah Text

The function `fetch_torah_text` retrieves text from the Torah using the Sefaria API and stores it in a numpy array.

## Creating Embeddings

Embeddings are created using pre-trained models:

- Hebrew Tokenizer and Model: `alephBERT`
- English Tokenizer and Model

## Retriever Models

### Embedding-based Retriever

Uses embeddings generated by the `alephBERT` model for Hebrew and a pre-trained model for English.

### BM25 Retriever

Uses the BM25 algorithm for text retrieval, which is particularly effective for sparse datasets.

## Chain of Thought (CoT) Templates

Custom templates for structuring the context and questions in Hebrew are defined.

## Experiments

The notebook includes various experiments to evaluate the performance of different models on question-answering tasks:

### English Dataset

Uses datasets from Huggingface to evaluate model performance.

### Hebrew Dataset

Evaluates model performance on Hebrew texts with both open-ended and multiple-choice questions.

## Results

The results of the experiments are evaluated and compared using custom functions:

- `evaluate_model`
- `evaluate_model_multi`
- `evaluate_model_hugginface`

## Usage

To use the notebook, follow these steps:

1. Install the required dependencies.
2. Preprocess the data using the provided functions.
3. Generate embeddings for the text data.
4. Choose and configure a retriever model.
5. Run the experiments to evaluate model performance.
6. Analyze the results to draw conclusions.
