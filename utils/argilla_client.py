import argilla as rg
from config import Config

def get_argilla_client():
    """
    Initialize Argilla client.

    Returns:
        Argilla client instance.
    """
    client = rg.Argilla(
        api_url=Config.ARGILLA_API_URL,
        api_key=Config.ARGILLA_API_KEY,
        headers={"Authorization": f"Bearer {Config.HF_TOKEN}"}
    )
    return client

def get_or_create_workspace(client, workspace_name):
    """
    Get or create a workspace.

    Args:
        client: Argilla client.
        workspace_name (str): Workspace name.

    Returns:
        Workspace instance.
    """
    try:
        workspace = client.workspaces(name=workspace_name)
    except rg.NotFoundApiError:
        workspace = rg.Workspace(name=workspace_name, client=client)
        workspace.create()
    return workspace

def get_or_create_dataset(client, workspace, dataset_name, settings):
    """
    Get or create a dataset.

    Args:
        client: Argilla client.
        workspace: Workspace instance.
        dataset_name (str): Dataset name.
        settings: Dataset settings.

    Returns:
        Dataset instance.
    """
    try:
        dataset = client.datasets(name=dataset_name, workspace=workspace)
    except rg.NotFoundApiError:
        dataset = rg.Dataset(
            name=dataset_name,
            workspace=workspace.name,
            settings=settings,
            client=client
        )
        dataset.create()
    return dataset

def log_records_to_dataset(dataset, records):
    """
    Log records to Argilla dataset.

    Args:
        dataset: Argilla dataset instance.
        records (list): List of Argilla records.
    """
    dataset.records.log(records)