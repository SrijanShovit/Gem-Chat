https://www.pexels.com/photo/brown-hummingbird-selective-focus-photography-1133957/


# Gem-Chat 💬💬

PDFChat is a project that leverages Google's Gemini Pro model. It comprises of two parts: 

1. A simple Q&A module for users to ask their questions
2. An image vision module for users to query on their images

## Q&A module: Features 🚀

- **Web UI**: 🌐 Streamlit UI for users to query.
- **Answer Generation**: 📚 Leverages Gemini to produce high-quality responses.
- **Cache/Data Persistence/Optimization**: 💾 Streamlit's session state used to store recent queries.

***Cache optimization***

Gemini Pro is free to use for 60 requests/min. However, if we store the recently asked queries in the session state as cache, those can be fetched with thunder speed reducing request traffic to the model.

## Performance Comparison

Response Time in seconds is used as metric.

First time request  | Second time request served by cash
------------- | -------------
5-12   | 0.001

---

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





## Screenshots 📸
![Home Screen](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(52).png)

---

![PDF Uploaded](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(44).png)

---

![Q1](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(45).png)

---

![Q2](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(46).png)

---

![Q3](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(49).png)

---

![Q4](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(50).png)

---

![Q5](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(47).png)

---

![Q5](https://github.com/SrijanShovit/PDFChat/blob/main/Screenshots/Screenshot%20(51).png)

---

## Technologies Used 🛠️

- **Streamlit**: 
- **Google Generative AI Package**: 
- **Google Gemini**: 

## Usage 🖥️

To use PDFChat, follow these steps:

1. **Upload a PDF file**: 📂 Upload a PDF file containing textual content.
2. **Ask questions**: ❓ Ask questions related to the content of the uploaded PDF file.
3. **View answers**: 👀 Wait for the answers to be generated (approximately 2 minutes) and view them on the interface.

## Getting Started 🚀

To run PDFChat locally, you'll need to have Python installed. Then, follow these steps:

1. **Clone the repository**: 📁 Clone this repository to your local machine.
2. **Install dependencies**: 💻 Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

3. **Run the app**: ▶️ Run the Streamlit app:

   ```
   streamlit run pdf_chat.py
   ```

4. **Access the app**: 🌐 Access the Streamlit app in your web browser.

## Contributing 🤝

Contributions to PDFChat are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

---

Feel free to customize the README as needed and add any additional information or sections based on the specific requirements of your project.
