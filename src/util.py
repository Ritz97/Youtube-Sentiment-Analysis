import googleapiclient.discovery
from google import genai
from dotenv import load_dotenv 
import os
import yaml

load_dotenv()

def getYoutube():

    youtube = googleapiclient.discovery.build(
        serviceName = "youtube",
        version = "v3",
        developerKey = os.getenv("YOUTUBE_API_KEY")
    )

    return youtube

def getYoutubeCommentThread(youtubeInstance, videoID):

    youtubeCommentThreadRequest = youtubeInstance.commentThreads().list(
        part = "snippet",
        videoId = videoID,
        maxResults = 100,
        order = "time"
    )

    youtubeCommentThreadResponse = youtubeCommentThreadRequest.execute()

    return youtubeCommentThreadResponse

def getYoutubeCommentThreadList(youtubeCommentThreadResponse):

    youtubeCommentThreadList = []

    for item in youtubeCommentThreadResponse["items"]:
        youtubeCommentThreadList.append(
            dict(
                type = "text", 
                text = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            )
        )

    return youtubeCommentThreadList

def getYamlData():

    rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    yamlFile = os.path.join(rootDir, "config", "genai_system_instruction.yaml")
    yamlData = yaml.safe_load(open(yamlFile, "r", encoding="utf-8"))

    return yamlData

def callGenAI(modelInput, systemInstruction):

    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

    interaction = client.interactions.create(
        model = "gemini-3.1-flash-lite",
        input = modelInput,
        system_instruction = systemInstruction
    )

    return interaction.output_text

def saveMarkdownFile(content):

    rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    newDir = os.path.join(rootDir, "output")
    os.makedirs(newDir, exist_ok = True)
    outputFile = os.path.join(newDir, "Output.md")

    with open(outputFile, "w", encoding = "utf-8") as f:
        f.write(content)