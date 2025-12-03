class HTTPMethodOverrideMiddleware(object):
    """
    Middleware que sobrescreve o método da requisição se _method for fornecido.
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Apenas processa se o método for POST
        if environ['REQUEST_METHOD'] == 'POST':
            # Lê os dados do formulário sem consumir completamente o stream de input
            # Isso é necessário para que o Flask possa ler os dados novamente depois
            form = environ['wsgi.input'].read().decode('utf-8')
            environ['wsgi.input'] = form.encode('utf-8') # Repõe o stream de input
            
            # Procura por "_method=PUT" ou "_method=DELETE" nos dados do formulário
            if "_method=PUT" in form:
                environ['REQUEST_METHOD'] = 'PUT'
            elif "_method=DELETE" in form:
                environ['REQUEST_METHOD'] = 'DELETE'

        return self.app(environ, start_response)

