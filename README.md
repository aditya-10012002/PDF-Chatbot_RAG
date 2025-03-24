# PDF Chatbot with RAG
## Overview
First, we run the ```create_database.py``` which makes the uploaded documents in the Data folder pass through the ```HuggingFaceEmbeddings``` and chunks of data are stored using the ```Chroma``` database in your local.<br>
<br>
- Put any number of documents you wanna use as context into the ```Data``` folder.
- Generate your Google Gemini API key and configure it.
- Then run the ```query_data.py``` file with your query as the arg parameter.

## Result
<br>

![pdf chatbot.jpg](<https://media-hosting.imagekit.io//bfd66dd0a22e4403/pdf%20chatbot.jpg?Expires=1837407401&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=QXxHhJA6XPJT1AXw2bCrorQbJXO3nsTuuMkaCX7OfNL6aM7AQYmymaIJSQOgD9VEV4~Ccl5GR7DczZanmumUDWrJo3AxpXRdtStsvpZxDmpVk7SHiYVVYRqF3zOlj1mP4qLLtD1-wKoT4MyFjVJ6wdCv5oHjnOdB8bgJ1Paz-ASgAOAt3AwvlEDID6AfjR8ug22l~aqYwIoGU1fw0T9FB3JMx5VUQcmVaKphx6bQlbRbOELz3Z0ZZZ7bLwctmw2WNPBtb3BkOiIFCW9ZGEY-XTDe3D46m7tbLmMe~s3h7U6H0zZl~jQjR9rM0x2k7dFf7fIPP8P-vBwbvlZmnhT9Bg__>)
