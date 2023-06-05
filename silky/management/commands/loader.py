from django.core.management import BaseCommand
from silky.utils.load_questions import load_questions


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("code", nargs="+", type=int)

    def handle(self, *args, **options):
        code = options.get("code")
        load_questions(cat_code=code)

