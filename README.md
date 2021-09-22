Django - lessons

DB dump export (win)

python -X utf8 manage.py dumpdata mainapp.ProductCategory -o mainapp\fixtures\categories.json

DB import
python manage.py loaddata mainapp\fixtures\categories.json