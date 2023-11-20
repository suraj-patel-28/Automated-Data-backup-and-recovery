# recovery_process.py
import zipfile
import os

def restore_backup(backup_path, restore_path):
    try:
        with zipfile.ZipFile(backup_path, 'r') as zipf:
            zipf.extractall(restore_path)
        print("Restore successful!")
    except Exception as e:
        print(f"Restore failed: {str(e)}")
        raise
