from .models import Article


class Database:

    def get_latest_articles(self):
        return Article.objects.order_by("-id")[:5]

    def get_articles(self):
        return Article.objects.all()

    def get_article_by_slug(self, slug):
        return Article.objects.get(slug=slug)

    def add_article(self, title, content):
        Article.objects.create(title=title, content=content)

    # MUAMMONI TUZATADIGAN METOD
    def find_articles_by_title(self, q):
        return Article.objects.filter(title__icontains=q)