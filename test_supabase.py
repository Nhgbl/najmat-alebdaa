import os
import sys

# Install supabase if not present
try:
    from supabase import create_client, Client
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "supabase"])
    from supabase import create_client, Client

url = "https://yumshpcohoalyancufzi.supabase.co"
key = "sb_publishable_YwTQDhK3KDeFmAkvf4cOhA_ogcoPe3P"

print("Connecting to Supabase...")
try:
    supabase: Client = create_client(url, key)
    
    # Try to list buckets
    print("Testing buckets access...")
    buckets = supabase.storage.list_buckets()
    print("Buckets found:")
    for b in buckets:
        print(f"- {b.name} (Public: {b.public})")
    
    # Check if 'media' is in buckets
    media_bucket = next((b for b in buckets if b.name == 'media'), None)
    if media_bucket:
         print(f"Bucket 'media' found! Public: {media_bucket.public}")
    else:
         print("Bucket 'media' NOT found.")

except Exception as e:
    print("Error:", type(e).__name__, "-", str(e))
