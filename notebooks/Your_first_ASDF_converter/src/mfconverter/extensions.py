from asdf.extension import Extension
from .converter import PhotoIDConverter

class MFExtension(Extension):
    extension_uri = "asdf://stsci.edu/example-project/photo_id-1.0.0"
    tags = ["asdf://stsci.edu/example-project/tags/photo_id-1.0.0"]
    converters = [PhotoIDConverter()]

# The following will be called by ASDF when looking for ASDF entry points    
def get_extensions():
    return [MFExtension()]
