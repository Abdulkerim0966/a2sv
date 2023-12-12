class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.session={}
        self.time=timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.session[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.session:
            if self.session[tokenId]+self.time>currentTime:
                self.session[tokenId]=currentTime
                # print(self.session[tokenId]) 
        
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans=0
        
        for i in self.session:
            if self.session[i]+self.time>currentTime:
                ans+=1
        return ans


        


