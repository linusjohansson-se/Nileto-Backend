from allauth.account.adapter import DefaultAccountAdapter, HttpRequest

class AllAuthAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest) -> bool:
        return False

    


