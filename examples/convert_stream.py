import convertapi
import os
import io
import tempfile

convertapi.api_credentials = os.environ['API_TOKEN'] # your api token

# Example of using content stream to convert to pdf
# https://www.convertapi.com/txt-to-pdf

content = "Test content string"

upload_io = convertapi.UploadIO(content, 'test.txt')

result = convertapi.convert('pdf', { 'File': upload_io })

saved_files = result.save_files(tempfile.gettempdir())

print("The PDF saved to %s" % saved_files)

