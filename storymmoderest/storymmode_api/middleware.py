class SimpleRequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Print the request path
        print(f"Request path: {request.path}")
        # Print the request headers
        print("Headers:")
        for header, value in request.headers.items():
            print(f"{header}: {value}")
        
        if request.method == 'POST':
            # Print the request body
            print("Body:")
            print(request.body)

            print("POST:")
            for key, value in request.POST.items():
                print(f"{key}: {value}")

        response = self.get_response(request)
        return response
