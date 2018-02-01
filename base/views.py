from django.views.generic import TemplateView


class ErrorHandler(TemplateView):
    template_name = '500.html'

    def get_app_name(self):
        module = self.request.resolver_match.func.__module__
        app, *path = module.split('.')

        return app

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['app_name'] = self.get_app_name()

        return context
