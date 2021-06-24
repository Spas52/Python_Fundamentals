class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("Spas", "Aaaaaide", 69)
print(f"User: {comment.username}")
print(f"Says: {comment.content}")
print(f"Likes: {comment.likes}")