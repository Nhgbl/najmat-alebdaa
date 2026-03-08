import os
import uuid
import mimetypes
from django.core.files.storage import Storage
from django.conf import settings
from django.utils.deconstruct import deconstructible
from supabase import create_client, Client

@deconstructible
class SupabaseStorage(Storage):
    def __init__(self):
        self.url = getattr(settings, 'SUPABASE_URL', '')
        self.key = getattr(settings, 'SUPABASE_KEY', '')
        self.bucket_name = getattr(settings, 'SUPABASE_BUCKET', 'media')
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)
        else:
            self.supabase = None

    def _save(self, name, content):
        if not self.supabase:
            raise ValueError("Supabase URL and Key are not configured.")
            
        ext = name.split('.')[-1]
        unique_name = f"{uuid.uuid4().hex}.{ext}"
        
        content.seek(0)
        content_bytes = content.read()
        
        content_type = getattr(content, 'content_type', None)
        if not content_type:
            content_type, _ = mimetypes.guess_type(name)
        if not content_type:
            content_type = 'application/octet-stream'
             
        self.supabase.storage.from_(self.bucket_name).upload(
            file=content_bytes,
            path=unique_name,
            file_options={"content-type": content_type}
        )
        return unique_name

    def exists(self, name):
        return False

    def url(self, name):
        if not self.supabase:
            return f"{settings.MEDIA_URL}{name}"
            
        res = self.supabase.storage.from_(self.bucket_name).get_public_url(name)
        return res
