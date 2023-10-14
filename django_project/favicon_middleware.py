from django.utils.deprecation import MiddlewareMixin

class FaviconMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Add the HTML line to the response content
        line_to_add = "<link rel='icon' type='image/png' href='{% static 'images/SGS_logo_clean.png' %}'>"
        response.content = response.content.replace(b'</head>', f'{line_to_add}</head>'.encode())
        return response