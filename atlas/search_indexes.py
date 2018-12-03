from haystack import indexes
from atlas.models import Ship

class ShipIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    imo = indexes.IntegerField(model_attr='imo', null=True)
    type = indexes.CharField(model_attr='type', null=True)
    year_built = indexes.IntegerField(model_attr='year_built')
    builder = indexes.CharField(model_attr='builder', null=True)
    tonnage = indexes.IntegerField(model_attr='tonnage', null=True)
    length = indexes.IntegerField(model_attr='length', null=True)
    beam = indexes.IntegerField(model_attr='beam', null=True)
    city = indexes.CharField(model_attr='city', null=True)
    country = indexes.CharField(model_attr='country', null=True)
    registers = indexes.MultiValueField(null=True)
    status = indexes.CharField(model_attr='status', null=True)
    uses = indexes.MultiValueField(null=True)
    owner = indexes.CharField(model_attr='owner', null=True)
    former_names = indexes.CharField(model_attr='former_names', null=True)

    def get_model(self):
        return Ship

    def prepare_registers(self, obj):
        return [registers.id for registers in obj.registers.all().order_by('name')]

    def prepare_uses(self, obj):
        return [uses.id for uses in obj.uses.all().order_by('name')]
