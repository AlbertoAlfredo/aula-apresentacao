import io

class HTTPMethodOverrideMiddleware(object):
    """
    Middleware que sobrescreve o método da requisição se _method for fornecido.
    Ajustado para lidar corretamente com o stream de input (wsgi.input).
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Apenas processa se o método for POST
        if environ['REQUEST_METHOD'] == 'POST':
            
            # 1. Lê todos os dados do stream de input
            # Garante que o stream é lido do início
            try:
                content_length = int(environ.get('CONTENT_LENGTH', 0))
                form_data = environ['wsgi.input'].read(content_length)
            except ValueError:
                form_data = b'' # Se não houver CONTENT_LENGTH ou for inválido
            
            form_str = form_data.decode('utf-8')

            # 2. Cria um novo stream de bytes em memória (BytesIO)
            # e repõe no environ para que o Flask possa ler
            environ['wsgi.input'] = io.BytesIO(form_data)
            
            # 3. Procura por "_method=PUT" ou "_method=DELETE" nos dados do formulário
            if "_method=PUT" in form_str:
                environ['REQUEST_METHOD'] = 'PUT'
            elif "_method=DELETE" in form_str:
                environ['REQUEST_METHOD'] = 'DELETE'
                
            # Adiciona o Content-Length para consistência
            environ['CONTENT_LENGTH'] = str(len(form_data))

        return self.app(environ, start_response)