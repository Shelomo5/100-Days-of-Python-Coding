# Used to created objects which contain information from blog JSON data (post_num, title, subtitle, and body)
class Post:
    def __init__(self,post_num,title,subtitle,body):
        self.id = post_num
        self.title = title
        self.subtitle = subtitle
        self.body = body