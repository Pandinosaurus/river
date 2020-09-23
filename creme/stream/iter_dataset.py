import inspect
import importlib


__all__ = [
    'available_datasets',
    'iter_dataset'
]


def _available_datasets():
    return dict(inspect.getmembers(
        importlib.import_module('creme.stream.datasets'),
        inspect.isclass
    ))


def available_datasets():
    """Return the list of available datasets.

    Each element in the returned list can be passed to `stream.iter_dataset` to iterate over it.

    """
    return list(_available_datasets().keys())


def iter_dataset(name: str, **kwargs):
    """Iterate over a dataset.

    Parameters
    ----------
    name
        The name of the dataset to load. You can check the list of available datasets by calling
        `stream.available_datasets`.
    kwargs
        Extra keyword arguments are used to parametrize certain datasets that come under different
        variants.

    """
    return _available_datasets()[name](**kwargs)