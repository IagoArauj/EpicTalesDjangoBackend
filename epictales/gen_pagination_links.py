from rest_framework.request import Request
from django.db.models import Model

def gen_pagination_links(request: Request, Model: Model, limit: int, offset: int) -> tuple[int, int, str, str]:
    path = request.build_absolute_uri(request.path)
    count = Model.objects.count()
    
    pages = count // limit if count % limit == 0 else count // limit + 1
    
    next_page = int(offset) + int(limit) if int(offset) + int(limit) < count else None
    prev_page = int(offset) - int(limit) if int(offset) - int(limit) >= 0 else None

    next_link = f"{path}?limit={limit}&offset={next_page}" if next_page is not None else None
    prev_link = f"{path}?limit={limit}&offset={prev_page}" if prev_page is not None else None
    
    return (count, pages, next_link, prev_link)