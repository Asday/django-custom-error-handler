from django.views import View


class ErrorView(View):

    def dispatch(self, *args, **kwargs):
        1 / 0
