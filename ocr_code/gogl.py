import io


from google.cloud import storage

from google.cloud import vision_v1 as vision
from google.cloud.vision import types



def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

def detect_handwritten_ocr(path):
    client = vision.ImageAnnotatorClient()
    file_name ='a.jpg'
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])

    response = client.document_text_detection(image=image,
                                              image_context=image_context)

    print('Full Text: {}'.format(response.full_text_annotation.text))
    with open('text.txt','w') as f:
        f.write(response.full_text_annotation.text)
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

if __name__=="__main__":
    bucket_name='scic-8bdc2.appspot.com'
    source_blob_name='images/a.jpg'
    destination_file_name='a.jpg'
    source_txt='text.txt'
    destination_blob_txt='text.txt'
    download_blob(bucket_name, source_blob_name, destination_file_name)
    detect_handwritten_ocr("a.jpg")
    upload_blob(bucket_name, source_txt, destination_blob_txt)
