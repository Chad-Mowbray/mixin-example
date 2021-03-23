from AuthenticatorMixin import AuthenticatorMixin
from HttpResponse import HttpResponse

class ProtectedHttpResponse(HttpResponse, AuthenticatorMixin):
    def __init__(self, request):
        super().__init__(request)

    def create_response(self, filepath):
        if self.is_authenticated(self.request):
            return super().create_response(filepath)

protected = ProtectedHttpResponse({'loggedIn': "True"})
response = protected.create_response("index.html")
print(response)

protected2 = ProtectedHttpResponse({'loggedIn': "False"})
response2 = protected2.create_response("index.html")
print(response2)