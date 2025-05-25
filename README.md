# PDF Chatbot with RAG
## Overview
First, we run the ```create_database.py``` which makes the uploaded documents in the Data folder pass through the ```HuggingFaceEmbeddings``` and chunks of data are stored using the ```Chroma``` database in your local.<br>
<br>
- Put any number of documents you wanna use as context into the ```Data``` folder.
- Generate your Google Gemini API key and configure it.
- Then run the ```query_data.py``` file with your query as the arg parameter.

## Result
<br>

![pdf chatbot.jpg](<https://ik.imagekit.io/py7zov877/Screenshot%202025-03-24%20122157.png?updatedAt=1748198068638__>)
