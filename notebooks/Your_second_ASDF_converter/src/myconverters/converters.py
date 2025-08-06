from asdf.extension import Converter
from .photo_id import PhotoID
from .traffic_citation import TrafficCitation


class PhotoIDConverter(Converter):
    tags = ["asdf://stsci.edu/example-project/tags/photo_id-*"]
    types = ["myconverters.photo_id.PhotoID"]
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
        return PhotoID(node['last_name'],
                       node['first_name'],
                       node['photo'])


class TrafficCitationConverter(Converter):
    tags = ["asdf://stsci.edu/example-project/tags/traffic_citation-1.0.0"]
    types = ["myconverters.traffic_citation.TrafficCitation"]

    def to_yaml_tree(self, obj, tags, ctx):
        node = {}
        node['ociffer'] = obj.ociffer
        node['violation'] = obj.violation
        node['date'] = obj.date
        node['time'] = obj.time
        node['photo_id'] = obj.photo_id
        return node

    def from_yaml_tree(self, node, tag, ctx):
        return TrafficCitation(node['ociffer'],
                               node['violation'],
                               node['date'],
                               node['time'],
                               node['photo_id'])
