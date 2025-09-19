import nest_asyncio
nest_asyncio.apply()

import streamlit as st
import os
import asyncio
from dotenv import load_dotenv
from crewai import Crew, Process, Task, Agent
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Get API keys
google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the search tool
tool = SerperDevTool()

# Initialize the LLM
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        verbose=True,
        temperature=0.3,
        google_api_key=google_api_key
    )
except Exception as e:
    st.error(f"Failed to initialize LLM: {str(e)}")
    st.stop()

# Define Agents
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# Async function to run CrewAI
async def run_crew(topic):
    try:
        research_task = Task(
            description=(
                f"Identify the next big trend in {topic}. "
                "Focus on identifying pros and cons and the overall narrative. "
                "Your final report should clearly articulate the key points, "
                "its market opportunities, and potential risks."
            ),
            expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
            tools=[tool],
            agent=news_researcher,
        )

        write_task = Task(
            description=(
                f"Compose an insightful article on {topic}. "
                "Focus on the latest trends and how it's impacting the industry. "
                "This article should be easy to understand, engaging, and positive."
            ),
            expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
            tools=[tool],
            agent=news_writer,
            async_execution=False,
        )

        crew = Crew(
            agents=[news_researcher, news_writer],
            tasks=[research_task, write_task],
            process=Process.sequential,
        )

        result = await asyncio.to_thread(crew.kickoff, inputs={'topic': topic})
        return result
    except Exception as e:
        return f"Error in crew execution: {str(e)}"

# -------- Streamlit UI / UX Enhancements --------

# Set page config for wide layout and theming support
st.set_page_config(
    page_title="AI News Article Generator",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Generates insightful AI news articles using multiphase agent collaboration."
    }
)

# --- CUSTOM CSS ---
st.markdown(
    """
    <style>
    /* Font and typography */
    .main {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #1a1a1a;
        line-height: 1.5;
    }
    h1, h2, h3 {
        font-weight: 700;
        color: #1e40af;
        margin-bottom: 0.5rem;
    }
    /* Title box */
    .title-box {
        background: linear-gradient(90deg, #f8fafc 0%, #e5e7eb 100%);
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    /* Button styling */
    .stButton>button {
        border-radius: 8px;
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #3b82f6 0%, #1e40af 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    /* Input styling */
    .stTextInput label {
        font-weight: 500;
        color: #1e40af;
    }
    .stTextInput>div>input {
        border-radius: 6px;
        border: 1px solid #d1d5db;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: #f9fafb;
    }
    .stTextInput>div>input:focus {
        border-color: #1e40af;
        box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.2);
        background: white;
    }
    /* Markdown output styling */
    .stMarkdown {
        font-size: 1rem;
        line-height: 1.7;
        color: #1a1a1a;
        background: #f8fafc;
        border-radius: 8px;
        padding: 1.5rem;
        border: 1px solid #e5e7eb;
        margin-top: 1rem;
        white-space: pre-wrap;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #1e40af;
    }
    /* Progress bar */
    .stProgress > div > div {
        background-color: #1e40af;
    }
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .title-box {
            padding: 1.5rem;
        }
        .stButton>button {
            padding: 0.5rem 1.5rem;
        }
        .stTextInput>div>input {
            padding: 0.5rem;
        }
        .stMarkdown {
            padding: 1rem;
        }
    }
    /* Dark mode support */
    [data-theme="dark"] {
        background-color: #111827;
        color: #e5e7eb;
    }
    [data-theme="dark"] .main {
        color: #e5e7eb;
    }
    [data-theme="dark"] .title-box {
        background: linear-gradient(90deg, #1f2a44 0%, #374151 100%);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }
    [data-theme="dark"] h1, [data-theme="dark"] h2, [data-theme="dark"] h3 {
        color: #60a5fa;
    }
    [data-theme="dark"] .stTextInput label {
        color: #60a5fa;
    }
    [data-theme="dark"] .stTextInput>div>input {
        background: #1f2a44;
        border-color: #4b5563;
        color: #e5e7eb;
    }
    [data-theme="dark"] .stTextInput>div>input:focus {
        border-color: #60a5fa;
        box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.3);
        background: #1f2a44;
    }
    [data-theme="dark"] .stButton>button {
        background: linear-gradient(90deg, #1e40af 0%, #60a5fa 100%);
    }
    [data-theme="dark"] .stButton>button:hover {
        background: linear-gradient(90deg, #60a5fa 0%, #1e40af 100%);
    }
    [data-theme="dark"] .stMarkdown {
        background: #1f2a44;
        color: #e5e7eb;
        border-color: #4b5563;
    }
    [data-theme="dark"] .stMarkdown h1, [data-theme="dark"] .stMarkdown h2, [data-theme="dark"] .stMarkdown h3 {
        color: #60a5fa;
    }
    [data-theme="dark"] .stProgress > div > div {
        background-color: #60a5fa;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title in a centered box
st.markdown(
    """
    <div class="title-box">
        <h1>AI News Article Generator</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Description
st.markdown(
    "Generate insightful research reports and engaging articles on your chosen AI or tech topic. "
    "Download the article as a Markdown file for easy sharing."
)

# Layout with two columns: input and button on the left, instructions on the right
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown("### Topic Input")
    topic = st.text_input(
        label="Enter a topic for your article",
        placeholder="e.g., Attention is all you need",
        help="Enter a specific AI or tech topic to generate a report and article."
    )
    generate_clicked = st.button("Generate Article", use_container_width=True)

with col2:
    with st.expander("How to Use", expanded=True):
        st.markdown(
            """
            - Enter a specific AI or tech topic in the input box.
            - Click **Generate Article** to create a research report and article.
            - Wait a few moments for the AI to process your request.
            - Download the generated article as a Markdown (.md) file.
            """
        )

# Placeholder for the results
result_placeholder = st.empty()

if generate_clicked:
    if topic:
        with st.spinner("Generating article..."):
            # Add a progress bar
            progress_bar = st.progress(0)
            for i in range(100):
                asyncio.run(asyncio.sleep(0.05))  # Simulate progress
                progress_bar.progress(i + 1)
            
            try:
                # Run the async function in a new thread with its own event loop
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(run_crew(topic))
                loop.close()

                # Clear progress bar
                progress_bar.empty()

                if "Error" in result:
                    result_placeholder.error(result)
                else:
                    # Display result with enhanced markdown formatting
                    formatted_result = f"# Generated Article on {topic}\n\n{result}\n\n---\n*Generated on September 15, 2025*"
                    result_placeholder.markdown(
                        f'<div class="stMarkdown">{formatted_result}</div>',
                        unsafe_allow_html=True,
                    )

                    # Download button
                    md_content = formatted_result.encode('utf-8')
                    filename = f"{topic.replace(' ', '_')}_article.md"
                    result_placeholder.download_button(
                        label="Download Article as Markdown",
                        data=md_content,
                        file_name=filename,
                        mime="text/markdown",
                        use_container_width=True
                    )
            except Exception as e:
                progress_bar.empty()
                result_placeholder.error(f"An error occurred: {str(e)}")
    else:
        result_placeholder.warning("Please enter a topic.")