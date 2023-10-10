import gcp_utils
import os
import doc_ai_utils
import pandas as pd


bucket_name = ''
project_id = ''
location = ''
processor_id = ''


for pdf in gcp_utils.list_blobs(bucket_name):
    if pdf.endswith(".pdf"):
        print(f'Downloading {pdf}')
        gcp_utils.download_blob(bucket_name, pdf, pdf)


for pdf in os.listdir():
    if pdf.endswith(".pdf"):

        document = doc_ai_utils.process_document(project_id=project_id,
                                  location=location,
                                  processor_id=processor_id, 
                                  file=pdf)
        print(document)
        break # just need to process 1 document as a POC


dict_row = []
for entity in document.entities:
    dictionary = {}
    dictionary["Entity_type"] =  entity.type_
    dictionary["mentioned_text"] =  entity.mention_text
    dictionary["parsed_text"] =  entity.normalized_value.text
    dictionary["confidence"] =  entity.confidence * 100
    dict_row.append(dictionary)



print(pd.DataFrame(dict_row))