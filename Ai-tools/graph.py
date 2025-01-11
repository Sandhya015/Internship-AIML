# Plot 2: Total Syncs
plt.figure(figsize=(10, 6))
plt.plot(time, total_syncs, marker='x', label='Total Syncs', color='green')
plt.title("External Secrets Operator - Total Syncs")
plt.xlabel("Time (minutes)")
plt.ylabel("Total Syncs")
plt.legend()

# Plot 3: Failed Syncs
plt.figure(figsize=(10, 6))
plt.bar(time, failed_syncs, label='Failed Syncs', color='red')
plt.title("External Secrets Operator - Failed Syncs")
plt.xlabel("Time (minutes)")
plt.ylabel("Failed Syncs")
plt.legend()

# Plot 4: Sync Frequency
plt.figure(figsize=(10, 6))
plt.plot(time, sync_frequency, marker='s', label='Sync Frequency (Hz)', color='purple')
plt.title("External Secrets Operator - Sync Frequency")
plt.xlabel("Time (minutes)")
plt.ylabel("Sync Frequency (Hz)")
plt.legend()

# Show all the plots
plt.tight_layout()
plt.show()
