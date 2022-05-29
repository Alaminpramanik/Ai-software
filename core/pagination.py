from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'  # items per page


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'