from .models import Auditoria

class AuditoriaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and request.method in ['POST', 'PUT', 'DELETE']:
            Auditoria.objects.create(
                usuario=request.user,
                acao=f"Acessou {request.path}",
                caminho=request.path,
                metodo=request.method
            )

        return response
