# backup_logic.py
import os
from datetime import datetime
from data_compression import compress_data
from remote_storage import transfer_to_remote
from error_handling import handle_error
from recovery_process import restore_backup
from data_visualization import plot_backup_history

def backup_data(source_paths, output_path):
    try:
        # Compress data
        compress_data(source_paths, output_path)

        # Get backup date
        backup_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Transfer to remote storage
        transfer_to_remote(output_path, f'/remote/path/backup_{backup_date}.zip', 'hostname', 'username', '/path/to/private/key.pem')

        # Log success
        log_backup_status(backup_date, 'Success')

    except Exception as e:
        # Log failure
        log_backup_status(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f'Failure: {str(e)}')
        # Handle the error
        handle_error(e)
        raise  # Re-raise the exception after logging

def log_backup_status(backup_date, status):
    with open('logs/backup_log.txt', 'a') as log_file:
        log_file.write(f'{backup_date} - {status}\n')

def visualize_backup_history(backup_dates, success_counts, failure_counts):
    plot_backup_history(backup_dates, success_counts, failure_counts)
