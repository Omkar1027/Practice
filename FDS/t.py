import matplotlib.pyplot as plt

# Create a diagram for the Input-Process-Output Model

# Set up figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Inputs box
input_box = plt.Rectangle((0.1, 0.4), 0.2, 0.2, edgecolor='black', facecolor='skyblue', lw=2)
ax.add_patch(input_box)
plt.text(0.2, 0.5, 'Inputs', fontsize=14, ha='center', va='center', weight='bold')

# Input details
plt.text(0.2, 0.45, 'Images\nVideos\nCriminal Records', fontsize=12, ha='center', va='center')

# Process box
process_box = plt.Rectangle((0.4, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightgreen', lw=2)
ax.add_patch(process_box)
plt.text(0.5, 0.5, 'Process', fontsize=14, ha='center', va='center', weight='bold')

# Process details
plt.text(0.5, 0.45, 'AI Image\nRecognition\nData Matching', fontsize=12, ha='center', va='center')

# Outputs box
output_box = plt.Rectangle((0.7, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightcoral', lw=2)
ax.add_patch(output_box)
plt.text(0.8, 0.5, 'Outputs', fontsize=14, ha='center', va='center', weight='bold')

# Output details
plt.text(0.8, 0.45, 'Identified\nCriminal Profiles\nActions for Law Enforcement', fontsize=12, ha='center', va='center')

# Add arrows between boxes
ax.annotate('', xy=(0.3, 0.5), xytext=(0.4, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=2))
ax.annotate('', xy=(0.6, 0.5), xytext=(0.7, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=2))

# Hide axes
ax.axis('off')

# Add title
plt.suptitle('Input-Process-Output Model', fontsize=16, weight='bold')

# Save the diagram as a PDF
plt.savefig('Input_Process_Output_Model.pdf', format='pdf')

# Display the diagram
plt.show()
