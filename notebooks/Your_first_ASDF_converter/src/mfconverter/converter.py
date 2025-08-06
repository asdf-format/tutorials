from asdf.extension import Converter

class PhotoIDConverter(Converter):
    tags = ["asdf://stsci.edu/example-project/tags/photo_id-*"]
    types = ["mfconverter.photo_id.PhotoID"]
    # The above registers the tag that the converter is used for, as well as
    # associating the class that the converter is used for.

    # This method converts from the Python object to yaml
    def to_yaml_tree(self, obj, tags, ctx):
        # The yaml conversion expects a dictionary returned
        node = {}
        node['first_name'] = obj.first_name
        node['last_name'] = obj.last_name
        node['photo'] = obj.photo
        return node

    # This method converts from yaml to the Python object
    def from_yaml_tree(self, node, tag, ctx):
        from .photo_id import PhotoID # Deferred import to avoid always importing 
                                      # when ASDF gets entry points.
        return PhotoID(node['last_name'],
                       node['first_name'],
                       node['photo'])
