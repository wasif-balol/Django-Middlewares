from django.db.models import F
from .models import NewStats


class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_exceptions = 0
        self.request_handled = 0
        self.context_response = {
            "msg": {"warning": "There is no more ink in the printer"}
        }

    def stats(self, os_info):
        if 'Windows' in os_info:
            NewStats.objects.all().update(win=F('win') + 1)
        elif 'Mac' in os_info:
            NewStats.objects.all().update(mac=F('mac') + 1)
        elif 'iPhone' in os_info:
            NewStats.objects.all().update(iph=F('iph') + 1)
        elif 'Android' in os_info:
            NewStats.objects.all().update(android=F('android') + 1)
        elif 'Linux' in os_info:
            NewStats.objects.all().update(linux=F('linux') + 1)
        else:
            NewStats.objects.all().update(oth=F('oth') + 1)

    def __call__(self, request):
        self.request_handled += 1
        if 'admin' not in request.path:
            self.stats(request.META["HTTP_USER_AGENT"])
        print(f'Requests handled so far : {self.request_handled}')
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'View Name:{view_func.__name__}')
        pass

    def process_exception(self, request, exception):
        self.num_exceptions += 1
        print(f"Exception Count:{self.num_exceptions}")
        pass

    def process_template_response(self, request, response):
        response.context_data["new_data"] = self.context_response
        return response

