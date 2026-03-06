#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# إنشاء/تحديث حساب المدير (سوف يتم تجاهل أي خطأ هنا لضمان نجاح الرفع)
python scripts/create_admin.py || echo "Admin already exists or skipped"
