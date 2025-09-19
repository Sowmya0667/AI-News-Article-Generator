# 🚀 AI News Article Generator using CrewAI & Gemini

An intelligent application that leverages a multi-agent system built with **CrewAI** to autonomously research and write insightful news articles on any given technology topic. The application is powered by Google's **Gemini 2.5 Pro** and features a sleek, modern user interface built with **Streamlit**.

-----

### 

## ✨ Features

  * **🤖 Multi-Agent System:** Utilizes two specialized AI agents:
      * **Senior Researcher:** Scans the web to find the latest trends, pros, cons, and market opportunities for a given topic.
      * **Expert Writer:** Crafts a compelling, easy-to-understand, and engaging news article based on the researcher's findings.
  * **🌐 Dynamic Content Generation:** Simply enter a topic (e.g., "Quantum Computing," "Generative Adversarial Networks"), and the agents will handle the rest.
  * **🎨 Modern UI/UX: Clean, responsive, and user-friendly interface built with Streamlit. mode support.
  * **⚡ Powered by Gemini Pro:** Leverages the advanced capabilities of Google's `gemini-2.5-pro` model for high-quality research and content creation.
  * **📥 Markdown Export:** Download the final generated article as a `.md` file, ready for easy sharing or publishing.

-----

## 🛠️ Tech Stack

  * **AI Framework:** [CrewAI](https://github.com/joaomdmoura/crewai)
  * **LLM:** Google Gemini 2.5 Pro via `langchain_google_genai`
  * **Web Framework:** [Streamlit](https://streamlit.io/)
  * **Web Search:** `SerperDevTool` from CrewAI Tools
  * **Language:** Python

-----

## ⚙️ Setup and Installation

Follow these steps to get the application running on your local machine.

### 1\. Prerequisites

Make sure you have **Python 3.9 or higher** installed on your system.

### 2\. Clone the Repository

```bash
git clone https://github.com/Sowmya0667/AI-News-Article-Generator.git
cd AI-News-Article-Generator
```

### 3\. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 4\. Install Dependencies

Install all the required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5\. Set Up Environment Variables

You'll need API keys for Google Gemini and Serper (for the search tool).

1.  Create a file named `.env` in the root directory of the project.

2.  Add your API keys to this file:

    ```env
    GOOGLE_API_KEY="your_google_api_key_here"
    SERPER_API_KEY="your_serper_api_key_here"
    ```

      * Get your **Google API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey).
      * Get your **Serper API Key** from [Serper.dev](https://serper.dev/).

### 6\. Run the Streamlit App

You're all set\! Launch the application with the following command:

```bash
streamlit run app.py
```

Open your web browser and navigate to `http://localhost:8501` to start using the app.

![AI News Article Generator UI](https://github.com/Sowmya0667/AI-News-Article-Generator/blob/main/assests/Screenshot.png)


-----

## 📖 How to Use

1.  **Enter a Topic:** Type any AI or technology-related topic into the input box. For example: "Attention is all you need" or "The future of AI in healthcare."
2.  **Generate:** Click the **"Generate Article"** button.
3.  **Wait:** The AI agents will start their work. You'll see a progress bar indicating that the research and writing process is underway.
4.  **View & Download:** Once complete, the generated article will appear on the screen. You can read it directly or use the **"Download Article as Markdown"** button to save it locally.

----

## 💡 Acknowledgements

* Built with [Streamlit](https://streamlit.io/)
* Powered by [Google Gemini](https://deepmind.google/technologies/gemini/) and [Serper.dev](https://serper.dev/)
