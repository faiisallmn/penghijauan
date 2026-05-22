#!/usr/bin/env python3
"""
Script untuk membuat commit otomatis setiap hari
Menambahkan timestamp ke activity.log
"""

from datetime import datetime
import os

def update_activity_log():
    """Menambahkan timestamp ke activity.log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_file = "activity.log"
    
    # Baca konten yang ada
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            content = f.read()
    else:
        content = "# Activity Log\n# File ini akan diupdate otomatis setiap hari oleh GitHub Actions\n\n"
    
    # Tambahkan entry baru
    new_entry = f"[{timestamp}] ✅ Auto commit - Keeping the streak alive!\n"
    
    with open(log_file, 'w') as f:
        f.write(content + new_entry)
    
    print(f"✅ Activity log updated: {timestamp}")
    return True

if __name__ == "__main__":
    update_activity_log()
