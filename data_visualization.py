# data_visualization.py
import matplotlib.pyplot as plt

def plot_backup_history(backup_dates, success_counts, failure_counts):
    plt.plot(backup_dates, success_counts, label='Success')
    plt.plot(backup_dates, failure_counts, label='Failure')
    plt.xlabel('Backup Dates')
    plt.ylabel('Backup Counts')
    plt.title('Backup History')
    plt.legend()
    plt.show()
