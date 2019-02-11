from rest_framework.pagination import PageNumberPagination
class MyPaginatiion(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage'
    page_size_query_param = 'num'
    max_page_size = 20
    last_page_strings = ('end_page',)