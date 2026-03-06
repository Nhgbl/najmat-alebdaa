#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# إنشاء حساب المدير مع تجاهل الخطأ إذا كان موجوداً
python scripts/create_admin.py || true
