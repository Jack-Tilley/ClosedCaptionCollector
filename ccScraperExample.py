from ccScraper import ClosedCaptionCollector
url = "https://www.youtube.com/watch?v=k6U-i4gXkLM"
path = "/Users/Tilley/Downloads/chromedriver"
cc = ClosedCaptionCollector(url, path)
cc.create_transcript()
cc.print_transcript()