from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"{self.title} - {self.date_created}"