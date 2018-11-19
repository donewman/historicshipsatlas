from django import forms
from atlas.models import Ship, Type, City, Country, Builder, Register, Status, Use, Owner

class BasicSearchForm(forms.Form):
    keywords = forms.CharField(label="Search:", max_length=200)

class AdvancedSearchForm(forms.Form):
    keywords = forms.CharField(label="Keyword(s):", max_length=200, required=False)
    name = forms.CharField(label="Name:", max_length=200, required=False)
    imo = forms.IntegerField(label="IMO Number:", required=False)
    type = forms.ModelMultipleChoiceField(label="Type:", queryset=Type.objects.all(), required=False)
    year_built_from = forms.IntegerField(label="Year Built (From):", required=False)
    year_built_to = forms.IntegerField(label="Year Built (To):", required=False)
    builder = forms.ModelMultipleChoiceField(label="Builder:", queryset=Builder.objects.all(), required=False)
    tonnage_from = forms.IntegerField(label="Gross Tonnage (From):", required=False)
    tonnage_to = forms.IntegerField(label="Gross Tonnage (To):", required=False)
    length_from = forms.IntegerField(label="Length (m) (From):", required=False)
    length_to = forms.IntegerField(label="Length (m) (To):", required=False)
    beam_from = forms.IntegerField(label="Beam (m) (From):", required=False)
    beam_to = forms.IntegerField(label="Beam (m) (To):", required=False)
    city = forms.ModelMultipleChoiceField(label="Location - City:", queryset=City.objects.all(), required=False)
    country = forms.ModelMultipleChoiceField(label="Location - Country:", queryset=Country.objects.all(), required=False)
    register = forms.ModelMultipleChoiceField(label="Historic Register:", queryset=Register.objects.all(), required=False)
    status = forms.ModelMultipleChoiceField(label="Status:", queryset=Status.objects.all(), required=False)
    use = forms.ModelMultipleChoiceField(label="Use:", queryset=Use.objects.all(), required=False)
    owner = forms.CharField(label="Owner:", max_length=200, required=False)
    former_names = forms.CharField(label="Former Names:", max_length=200, required=False)
