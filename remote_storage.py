# remote_storage.py
import paramiko

def transfer_to_remote(source_path, remote_path, hostname, username, private_key_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, key_filename=private_key_path)

    sftp = ssh.open_sftp()
    sftp.put(source_path, remote_path)

    sftp.close()
    ssh.close()
