#!/usr/bin/env python3

import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
from azure.mgmt.loganalytics.models import Table

SUBSCRIPTION_ID = os.getenv("AZ_SUBSCRIPTION_ID", "<YOUR_SUBSCRIPTION_ID>")
RESOURCE_GROUP  = os.getenv("AZ_RESOURCE_GROUP", "<YOUR_RESOURCE_GROUP>")
WORKSPACE_NAME  = os.getenv("AZ_WORKSPACE_NAME", "<YOUR_WORKSPACE_NAME>")

cred = DefaultAzureCredential()
client = LogAnalyticsManagementClient(cred, SUBSCRIPTION_ID)

for table in client.tables.list_by_workspace(RESOURCE_GROUP, WORKSPACE_NAME):
    name = table.name
    print(f"Updating retention for table: {name}")
    client.tables.update(
        RESOURCE_GROUP,
        WORKSPACE_NAME,
        name,
        parameters=Table(
            retention_in_days=730,
            is_troubleshoot_enabled=table.is_troubleshoot_enabled
        )
    )
