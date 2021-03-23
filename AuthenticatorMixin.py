class AuthenticatorMixin:

    def is_authenticated(self, request):
        if request["loggedIn"] == "True":
            return True
        else:
            raise Exception()