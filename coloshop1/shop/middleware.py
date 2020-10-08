class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('I am before view.')
        response = self.get_response(request)
        print('I am after view.')
        # Code to be executed for each request/response after
        # the view is called.

        return response
