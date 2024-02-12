# Gem-Chat 💬💬

PDFChat is a project that leverages Google's Gemini Pro model. It comprises of two parts: 

1. A simple Q&A module for users to ask their questions
2. An image vision module for users to query on their images

## Q&A module: Features 🚀

- **Web UI**: 🌐 Streamlit UI for users to query.
- **Answer Generation**: 📚 Leverages Gemini to produce high-quality responses.
- **Cache/Data Persistence/Optimization**: 💾 Streamlit's session state used to store recent queries.

***Cache optimization***

Gemini Pro is free to use for 60 requests/min. However, if we store the recently asked queries in the session state as cache, those can be fetched with thunder speed reducing request traffic to the model. The result was over 5000 times faster response and reduced model calls(as per usage). This can even help in saving credits or money when using proprietary models.

## Performance Comparison

Response Time in seconds is used as metric.

First time request  | Second time request served by cash
------------- | -------------
5-12   | 0.001

---
## Screenshots 📸

![Home Screen](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(103).png)

---

![q1](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(105).png)

---

![q13](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(106).png)

---

![q12](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(107).png)

--- 

***Cached response***
Time proof

![cached](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(108).png)


---


## Image Vision module: Features 🚀

- **Web UI**: 🌐 Streamlit UI for users to either upload a photo from their device or load an image from a URL and instruct the model to perform a task.
- **Answer Generation**: 🤖 Leverages Gemini to produce high-quality responses.
- **Cache/Data Persistence/Optimization**: 📦 Streamlit's session state used to store recent queries.

***Cache optimization***

Just like Q&A module, same idea has been used for cache implementation. But here, I have used combination of question and image in bytes format to generate cache key using hashing. This cache key is used to store responses. This was important as query or image or both may change, so I had to handle all the cases. Cached response were only needed if none of the two changed. The result was over 250 times faster response and reduced model calls(as per usage). This can even help in saving credits or money when using proprietary models.

## Performance Comparison

Response Time in seconds is used as metric.

First time request  | Second time request served by cash
------------- | -------------
5-35   | 0.005-0.020

---

## Screenshots 📸
![Home Screen](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(110).png)

---

![Home Page 2](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(111).png)

---

The Model smartly handles the case when you don't provide some prompt.


![Q1](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(113).png)

---

***Example queries***

---

![Q](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Tanishka%20SOB%20Thumbnail.png)

The prompt was to generate a Linkedin post. Here's the result:

![Q](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(114).png)

---

![Q3](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(115).png)

The prompt was to generate image description.

![Q3](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(116).png)


---

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(118).png)

Image Link: https://www.pexels.com/photo/brown-hummingbird-selective-focus-photography-1133957/

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(119).png)

Cached response:

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(122).png)

---

![Uploaded image](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/palak%20photo.jpg)

Prompt: Write a Twitter post.

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(123).png)

Cached response:

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(124).png)

---

![Q5](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/palak_photo-removebg-preview.png)

Prompt: Write a Twitter post.

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(125).png)

---

***Ok, Now Food Time!!😋🤤***

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(126).png)

![Q4](https://github.com/SrijanShovit/Gem-Chat/blob/main/images/Screenshot%20(127).png)

---

## Technologies Used 🛠️

- **Streamlit**: 🚀 A Python library that allows you to create interactive web apps for machine learning and data science projects.
- **Google Generative AI Package**: 🎨 The Google AI Python SDK enables developers to use Google's state-of-the-art generative AI models (like Gemini and PaLM) to build AI-powered features and applications.
- **Google Gemini**: 🔮 Gemini is a family of multimodal large language models developed by Google DeepMind, serving as the successor to LaMDA and PaLM 2.
- **libhash**: 🔐 A library used for generating and managing cryptographic hashes, ensuring data integrity and security.


## Usage 🖥️

It's nothing less than ChatGPT!!😉🙃

## Getting Started 🚀

To run Gem-Chat locally, you'll need to have Python installed. Then, follow these steps:

1. **Clone the repository**: 📁 Clone this repository to your local machine.
2. **Install dependencies**: 💻 Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

3. **Run the app**: ▶️ Run the Streamlit app:

   ```
   streamlit run app.py

   or

   streamlit run vision.py
   ```

4. **Access the app**: 🌐 Access the Streamlit app in your web browser.

## Contributing 🤝

Contributions to Gem-Chat are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

---

Feel free to customize the README as needed and add any additional information or sections based on the specific requirements of your project.
