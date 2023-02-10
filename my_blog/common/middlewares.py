from django.utils.deprecation import MiddlewareMixin


class CensusMiddlewares(MiddlewareMixin):
    """
    统计pv、uv等等数据
    """
    def process_request(self, request):
        pass
