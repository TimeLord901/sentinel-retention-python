# Sentinel Retention Automation (Python)

Automate setting **2-year (730-day)** retention on all Azure Sentinel tables using Python.

## Requirements
- Python 3.7+
- \`pip install azure-identity azure-mgmt-loganalytics\`
- \`az login\`

## Usage
1. Clone this repo:
   \`\`\`bash
   git clone https://github.com/<YourUsername>/sentinel-retention-python.git
   cd sentinel-retention-python
   \`\`\`
2. Fill in your settings in \`update_retention.py\` or export env vars:
   \`\`\`bash
   export AZ_SUBSCRIPTION_ID="00000000-0000-0000-0000-000000000000"
   export AZ_RESOURCE_GROUP="myResourceGroup"
   export AZ_WORKSPACE_NAME="mySentinelWorkspace"
   \`\`\`
3. Run the script:
   \`\`\`bash
   python3 update_retention.py
   \`\`\`
