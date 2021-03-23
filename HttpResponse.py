from Template import templater

class HttpResponse:

    def __init__(self, request):
        self.request = request

    def get_template(self, filepath):
        return templater(filepath)

    def create_response(self, filepath):
        return (self.request, self.get_template(filepath))