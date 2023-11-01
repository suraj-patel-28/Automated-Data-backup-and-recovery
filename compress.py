import zipfile
import os

def compress_and_store_data(source_dir, output_zip, storage_dir):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

    # Move the compressed backup to the storage directory
    backup_path = os.path.join(storage_dir, output_zip)
    os.rename(output_zip, backup_path)

# Example usage
source_directory = "/path/to/source"
output_zipfile = "backup.zip"
storage_directory = "/path/to/storage"
compress_and_store_data(source_directory, output_zipfile, storage_directory)
