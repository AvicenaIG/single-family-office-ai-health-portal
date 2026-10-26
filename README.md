# single-family-office-ai-health-portal
## AI-Powered Health Portal for Single Family Offices

**A one-stop-shop for health-related inquiries, leveraging AI to provide accurate and reliable information.**

### Badges

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-0.1.0-blue.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)

### Features

1. **Multimodal Search**: Search across various sources, including internet, images, and videos, to provide comprehensive answers.
2. **Knowledge Graph Integration**: Utilize a knowledge graph to enhance search results and provide relevant information.
3. **Natural Language Processing**: Leverage NLP capabilities to understand and process user queries.
4. **Text-to-Speech**: Convert text into speech to provide a more engaging user experience.
5. **Speech Recognition**: Recognize and process spoken language to enable voice-activated interactions.
6. **Document Generation**: Automatically generate documents, such as PPT and Word files, based on user requests.

### Installation

```bash
git clone https://github.com/AvicenaIG/cyber-doctor.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Quick Start

```python
import os
from Internet.Internet_prompt import extract_question
from Internet.retrieve_Internet import retrieve_html
from Internet.youcom_search import search_news as youcom_search
from client.clientfactory import Clientfactory
from env import get_app_root

# Example usage:
question = "What are the symptoms of COVID-19?"
history = ["I have a fever.", "I have a cough."]
response, links, has_files = InternetSearchChain(question, history)
print(response)
```

### Usage

**Example 1:** Search for information on COVID-19 symptoms.

```python
question = "What are the symptoms of COVID-19?"
history = ["I have a fever.", "I have a cough."]
response, links, has_files = InternetSearchChain(question, history)
print(response)
```

**Example 2:** Generate a PPT file on the benefits of regular exercise.

```python
question = "What are the benefits of regular exercise?"
response = Clientfactory().get_client().chat_with_ai_stream(question)
print(response)
```

### Configuration

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `APP_ROOT` | `str` | `./data/cache/internet` | Path to cache directory |
| `CLIENT_FACTORY` | `str` | `clientfactory.Clientfactory` | Client factory class |

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

MIT License

Copyright (c) 2026 single-family-office-ai-health-portal contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM
THIS SOFTWARE OR FROM ANY CONTRIBUTION OR MODIFYING IT.