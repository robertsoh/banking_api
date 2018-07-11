from banking.common.constants import DEFAULT_PAGINATOR_PAGE, DEFAULT_PAGINATOR_PAGE_SIZE


class CustomPagination(object):
    count = None
    num_pages = None
    page_range = None
    per_page = None
    queryset = []

    def __init__(self, page_size=None, page=None):
        self.page_size = page_size
        self.page = page

    def cleaned_data(self):
        try:
            self.page_size = int(self.page_size) if self.page_size else DEFAULT_PAGINATOR_PAGE_SIZE
        except Exception:
            raise ValueError('The page_size is not valid')
        try:
            self.page = int(self.page) if self.page else DEFAULT_PAGINATOR_PAGE
        except Exception:
            raise ValueError('The page is not valid')
        return {
            'page_size': self.page_size,
            'page': self.page
        }

    def paginate_queryset(self):
        data = {
            "count": self.count,
            "page_range": self.page_range,
            "num_pages": len(self.page_range),
            "page": self.page,
            "page_size": self.page_size,
            "results": self.queryset
        }
        return data

    def set_params(self, queryset, count, page_range):
        self.queryset = queryset
        self.count = count
        self.page_range = page_range
        return self
