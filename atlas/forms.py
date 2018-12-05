from django import forms
from haystack.forms import SearchForm
from atlas.models import Ship, Type, City, Country, Builder, Register, Status, Use, Owner

# Basic search form--appears on all pages
class BasicSearchForm(SearchForm):
    q = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'input-group-field'}), required=False)

# Advanced search form--appears on search page only
class AdvancedSearchForm(SearchForm):
    q = forms.CharField(label='Keyword(s):', max_length=200, required=False)
    name = forms.CharField(label='Name:', max_length=200, required=False)
    imo = forms.IntegerField(label='IMO Number:', required=False)
    type = forms.ModelMultipleChoiceField(label='Type:', queryset=Type.objects.all(), required=False)
    year_built_from = forms.IntegerField(label='Year Built (From):', required=False)
    year_built_to = forms.IntegerField(label='Year Built (To):', required=False)
    builder = forms.CharField(label='Builder:', max_length=200, required=False)
    tonnage_from = forms.IntegerField(label='Gross Tonnage (From):', required=False)
    tonnage_to = forms.IntegerField(label='Gross Tonnage (To):', required=False)
    length_from = forms.IntegerField(label='Length (m) (From):', required=False)
    length_to = forms.IntegerField(label='Length (m) (To):', required=False)
    beam_from = forms.IntegerField(label='Beam (m) (From):', required=False)
    beam_to = forms.IntegerField(label='Beam (m) (To):', required=False)
    city = forms.CharField(label='Location - City:', max_length=200, required=False)
    country = forms.ModelMultipleChoiceField(label='Location - Country:', queryset=Country.objects.all(), required=False)
    register = forms.ModelMultipleChoiceField(label='Historic Register(s):', queryset=Register.objects.all(), required=False)
    status = forms.ModelMultipleChoiceField(label='Status:', queryset=Status.objects.all(), required=False)
    use = forms.ModelMultipleChoiceField(label='Use(s):', queryset=Use.objects.all(), required=False)
    owner = forms.CharField(label='Owner:', max_length=200, required=False)
    former_names = forms.CharField(label='Former Names:', max_length=200, required=False)

    # Overrides no_query_found() in haystack.forms to return all results instead of empty SearchQuerySet when 'q' is blank
    def no_query_found(self):
        return self.searchqueryset.all()

    def search(self):
        # Stores the SearchQuerySet received from other processing
        sqs = super(AdvancedSearchForm, self).search()

        # Return all results if 'q' is blank
        if not self.is_valid():
            return self.no_query_found()

        # Filter sqs based on form fields
        if self.cleaned_data['name']:
            sqs = sqs.filter(name__contains=self.cleaned_data['name'])

        if self.cleaned_data['imo']:
            sqs = sqs.filter(imo__exact=self.cleaned_data['imo'])

        if self.cleaned_data['type']:
            sqs = sqs.filter(type=self.cleaned_data['type'])

        if self.cleaned_data['year_built_from']:
            sqs = sqs.filter(year_built__gte=self.cleaned_data['year_built_from'])

        if self.cleaned_data['year_built_to']:
            sqs = sqs.filter(year_built__lte=self.cleaned_data['year_built_to'])

        if self.cleaned_data['builder']:
            sqs = sqs.filter(builder__contains=self.cleaned_data['builder'])

        if self.cleaned_data['tonnage_from']:
            sqs = sqs.filter(tonnage__gte=self.cleaned_data['tonnage_from'])

        if self.cleaned_data['tonnage_to']:
            sqs = sqs.filter(tonnage__lte=self.cleaned_data['tonnage_to'])

        if self.cleaned_data['length_from']:
            sqs = sqs.filter(length__gte=self.cleaned_data['length_from'])

        if self.cleaned_data['length_to']:
            sqs = sqs.filter(length__lte=self.cleaned_data['length_to'])

        if self.cleaned_data['beam_from']:
            sqs = sqs.filter(beam__gte=self.cleaned_data['beam_from'])

        if self.cleaned_data['beam_to']:
            sqs = sqs.filter(beam__lte=self.cleaned_data['beam_to'])

        if self.cleaned_data['city']:
            sqs = sqs.filter(city__contains=self.cleaned_data['city'])

        if self.cleaned_data['country']:
            sqs = sqs.filter(country=self.cleaned_data['country'])

        if self.cleaned_data['register']:
            sqs = sqs.filter(register=self.cleaned_data['register'])

        if self.cleaned_data['status']:
            sqs = sqs.filter(status=self.cleaned_data['status'])

        if self.cleaned_data['use']:
            sqs = sqs.filter(use=self.cleaned_data['use'])

        if self.cleaned_data['owner']:
            sqs = sqs.filter(owner__contains=self.cleaned_data['owner'])

        if self.cleaned_data['former_names']:
            sqs = sqs.filter(former_names__contains=self.cleaned_data['former_names'])

        # Return filtered sqs
        return sqs
