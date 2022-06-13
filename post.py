class Post:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content
        
    def json(self):
        return{
            'title': self.title,
            'content': self.content,
        }