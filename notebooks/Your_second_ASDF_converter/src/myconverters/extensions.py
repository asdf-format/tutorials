from asdf.extension import ManifestExtension
from .converters import (
    PhotoIDConverter,
    TrafficCitationConverter,)

MY_CONVERTERS = [
    PhotoIDConverter(),
    TrafficCitationConverter(),
]

MY_EXTENSIONS = [
    ManifestExtension.from_uri(
        "asdf://stsci.edu/example-project/manifests/allmyschemas-1.0",
        converters=MY_CONVERTERS)
]
