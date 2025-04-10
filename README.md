
# Binary Basics: Learn, Convert, and Calculate in Binary

#### Video Demo: https://www.youtube.com/watch?v=BM0jY9t10Ls

## 📘 Project Description

This project is an educational and interactive tool to help users understand and perform calculations using binary numbers. It includes explanations and visual examples for addition, subtraction, multiplication, and division in binary form. Users can also convert between decimal and binary, and use a live calculator to try these operations themselves.

The web application is built using Python and Flask, with a lightweight responsive UI powered by PureCSS. Each topic includes educational content, and users can test the concepts interactively via a "Try It Yourself" panel.

#### Video Description:
In this CS50P Final Project video, I present 'Binary Basics: Learn, Convert, and Calculate in Binary' — a Flask-based web application that helps users understand and explore binary number operations.
The video starts with a personal introduction, followed by a walkthrough of the project’s file structure and a quick overview of the main logic in project.py.
I then run the app from the terminal and open it in the browser to showcase the homepage and individual tutorial pages, including one functioning embedded video.
Next, I demonstrate the interactive calculator, highlighting the division feature with floating-point results, and showing an error case for division by zero.

This project combines explanation, demonstration, and reflection to support learning binary concepts in a simple, hands-on way.


## 💻 How to Install and Run

1. Make sure Python is installed (version 3.7 or later recommended).
2. Open a terminal (Command Prompt or VS Code terminal).
3. Navigate to the folder containing this project.

4. (Optional) Create a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate      # Mac/Linux
    .venv\Scripts\activate       # Windows
    ```

5. Install required packages:
    ```
    pip install -r requirements.txt
    ```

6. Run the Flask server:
    ```
    python project.py
    ```

7. Open your browser and go to:
    ```
    http://127.0.0.1:5000
    ```

---

## 📂 Project File Structure Overview
```
CS50P_Final_Project/
├── project.py               # Main Flask app: routes + binary logic
├── test_project.py          # Unit tests for core functions (pytest)
├── requirements.txt         # Python dependencies (Flask, pytest)
├── README.md                # Project documentation
│
├── static/
│   ├── css/
│   │   └── styles.css       # Custom CSS for layout and visuals
│   └── js/
│       └── ui.js            # Sidebar behavior
│
├── templates/               # HTML templates rendered by Flask
│   ├── layout.html          # Base layout (PureCSS sidebar)
│   ├── index.html           # Homepage: binary history and introduction
│   ├── binary.html          # Intro to binary
│   ├── addition.html        # Binary addition tutorial and video
│   ├── subtraction.html     # Binary subtraction explanation and video
│   ├── multiplication.html  # Binary multiplication guide with video
│   ├── division.html        # Binary division with float support + videos
│   └── try_out.html         # Interactive converter & calculator
```


## 🧠 Design & Implementation Notes

I wanted to work on a topic that genuinely interests me and build a tool that I could actually use. While studying mathematics and number systems, I became fascinated by how they evolved alongside human civilization. The binary system, in particular, stood out to me. I thought it would be meaningful to create an educational, web-based program that not only performs calculations but also teaches the fundamental ideas behind them.

My goal was to create a simple yet informative web application that introduces users to the history of number systems, especially binary, and explains how basic binary calculations work — from a pen-and-paper perspective. I believe that understanding the core logic allows us to adapt in any condition, with calculators and tools serving as support rather than a crutch. This philosophy shaped the foundation of my project.

The website is built using Python with Flask, but my primary focus was not on mastering Flask. Instead, I used it as a lightweight way to structure and run the app. For the visual layout, I used PureCSS and adapted one of their templates. Most of the pages are informative, with embedded YouTube videos and step-by-step guides to explain binary operations, making the site feel more like an interactive tutorial.

My main focus was to deliver a working system that offers a good user experience, is simple and accessible, and serves an educational purpose. The "Try It Yourself" tool lets users convert between decimal and binary and perform binary addition, subtraction, multiplication, and division.

The most challenging part was implementing binary division with floating-point results. I had to learn how binary fractions work and translate that logic into Python code. It took time to understand and implement it correctly, but it was also the most rewarding part of the project.

In the end, I was surprised by how many components were involved, even in a relatively small project. I learned about Flask, HTML, CSS, and the importance of structuring and testing code. This project helped me see the bigger picture of how all parts of a web application come together.
