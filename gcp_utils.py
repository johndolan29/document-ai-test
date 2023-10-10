from google.cloud import storage

def download_blob(bucket_name: str, 
                  source_blob_name: str, 
                  destination_file_name: str):
    """
    Download a blob (file) from a Google Cloud Storage bucket.

    Args:
        bucket_name: The name of the GCS bucket.
        source_blob_name: The name of the blob in the GCS bucket.
        destination_file_name: The local file path where the blob should be saved.

    Prints:
        A message indicating that the blob has been downloaded.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name, raw_download=True)

def list_blobs(bucket_name):
    """
    List all the files in a GCS bucket.

    Args:
        bucket_name: The ID to give to the new bucket.

    Returns:
        A list of files in the bucket
    """
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    return [blob.name for blob in blobs]