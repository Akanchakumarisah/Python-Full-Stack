from abc import ABC, abstractmethod
class SocialMedia:
    @abstractmethod
    def post_content(self):
        pass
class Instagram(SocialMedia):
    def post_content(self):
        print("Posting photo with filter on Instagram")
class Twitter(SocialMedia):
    def post_content(self):
        print("Tweeting with hashtag on Twitter")
class LinkedIn(SocialMedia):
    def post_content(self):
        print("Sharing a professional update on LinkedIn")
insta = Instagram()
insta.post_content()
twit = Twitter()
twit.post_content()
link = LinkedIn()
link.post_content()
