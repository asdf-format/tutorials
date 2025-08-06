import sys

from asdf.resource import DirectoryResourceMapping

import importlib.resources as importlib_resources


def get_resource_mappings():
    """
    Get the resource mapping instances for myschemas
    and manifests.  This method is registered with the
    asdf.resource_mappings entry point.

    Returns
    -------
    list of collections.abc.Mapping
    """
    from . import resources
    resources_root = importlib_resources.files(resources)

    return [
        DirectoryResourceMapping(
            resources_root / "schemas", "asdf://stsci.edu/example-project/schemas/"),
        DirectoryResourceMapping(
            resources_root / "manifests", "asdf://stsci.edu/example-project/manifests/"),
    ]
