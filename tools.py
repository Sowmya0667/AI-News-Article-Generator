from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()