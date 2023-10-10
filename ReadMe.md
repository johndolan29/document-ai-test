# Document AI Test

This is a POC for how to integrate with the Document AI API on GCP

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.txt

```bash
pip install -r requirements.txt
```

Next, you need to login to your gcp account using the GCP SDK

```bash
gcloud auth application-default login
```
You also need to set up a GCP project to run in.

## Usage

Once you've logged in, you now need to set up the GCP storage bucket that will house the pdfs and the Document AI parser.
You can do this by going to [Google Cloud Storage](https://console.cloud.google.com/storage/browser)

Next, you want to upload a pdf to your newly created bucket. You can choose the one attached to this repo.
Make a note of the bucket name.

Next, go to [Document AI](https://console.cloud.google.com/ai/document-ai).
Go to Explore Processors.
Search for 'Invoice Parser'
Select Create Processor.
Any name and location should work.

Now, you should have a default parser (under Processor Details). You need to make a note of the processor ID that we will use in our API call.

Next, fill in your bucket_name, project_id, location, and processor_id in the main.py file

Then, simply running, 

```bash
python main.py
```

should output a table of entities that is in the document.

## Disclaimer

This is not production ready code. This is merely a toy piece of code to show how GCP's Document AI system works. Use at your own peril :)
