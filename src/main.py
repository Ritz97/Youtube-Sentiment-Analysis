import util

def main():

    videoID = input("Enter the YouTube video ID: ")
    youtube = util.getYoutube()
    youtubeCommentThreadResponse = util.getYoutubeCommentThread(
        youtubeInstance = youtube, 
        videoID = videoID
    )
    youtubeCommentThreadList = util.getYoutubeCommentThreadList(youtubeCommentThreadResponse)
    yamlData = util.getYamlData()
    outputText = util.callGenAI(
        modelInput = youtubeCommentThreadList, 
        systemInstruction = yamlData["youtube_main_instruction"]
    )
    util.saveMarkdownFile(outputText)
    print(outputText)

if __name__ == "__main__":
    main()