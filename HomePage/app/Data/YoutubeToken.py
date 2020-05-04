class AccessToken():
    def __init__(self, access_token = "", expires_in ="", scope = "", token_type="", error = "", error_description=""):
        self.access_token = access_token;
        self.expires_in = expires_in;
        self.scope = scope; 
        self.token_type = token_type;

