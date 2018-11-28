"""
Search indexes for haystack search in atlas app in historicshipsatlas project.
"""

from haystack import indexes
from atlas.models import Ship

class ShipIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Ship
