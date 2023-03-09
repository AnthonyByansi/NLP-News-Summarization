# NLP News Summarization

## Overview

News articles provide valuable information, but reading through multiple articles can be time-consuming. Text summarization is a text analysis technique that can automatically summarize long articles into shorter, more manageable summaries. By applying text summarization to news articles, users can quickly get an overview of the news and stay up-to-date with current events. This project aims to develop a text summarization tool for news articles using natural language processing (NLP) techniques.


## Features

The NLP News Summarization tool provides the following features:

- **Extractive summarization** : The tool uses extractive summarization techniques to identify the most important sentences in a news article and generate a summary based on those sentences.
- **Abstractive summarization** : The tool uses abstractive summarization techniques to generate a summary that is not a direct extract from the article but instead is paraphrased or rephrased to create a more concise summary.
- **Customizable summarization** : The tool allows users to customize the length of the summary they wish to generate, making it easy to get a summary of any length that meets their needs.
- **Multilingual summarization** : The tool supports summarization of news articles in multiple languages, including English, Spanish, French, German, and Chinese.
- **API access** : The tool provides a simple RESTful API for accessing its summarization functionality programmatically.

## Installation

To install the NLP News Summarization tool, follow these steps:

1. Clone the repository to your local machine: `https://github.com/AnthonyByansi/NLP-News-Summarization.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## Usage
To use the NLP News Summarization tool, follow these steps:

* Open the web application in your browser at http://localhost:5000/.
* Enter the URL or text of the news article you want to summarize.
* Select the summarization technique you want to use (extractive or abstractive).
* Choose the length of the summary you want to generate.
* Click the "Summarize" button to generate the summary.
* The summary will be displayed on the screen.

Alternatively, you can use the RESTful API to access the summarization functionality programmatically. Simply send a POST request to the API endpoint with the following parameters:

`text`: The text of the news article you want to summarize.
`technique`: The summarization technique you want to use (extractive or abstractive).
`length`: The length of the summary you want to generate.

## Conclusion

The NLP News Summarization tool is a powerful and easy-to-use tool for summarizing news articles. Its customizable and multilingual summarization capabilities make it suitable for a wide range of users. The tool is also available as a RESTful API for programmatic access, making it easy to integrate into other applications. We hope that this tool will help users stay up-to-date with current events and make it easier to access important information quickly and efficiently.
