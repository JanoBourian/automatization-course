import logging 

class Post:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
    
    def json(self): 
        try: 
            return {
                "title": self.title,
                "content" : self.content,
            }
        except Exception as e: 
            logging.error(f"ERROR: {e}")
            