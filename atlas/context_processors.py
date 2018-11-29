"""
Context processors for atlas app in historicshipsatlas project.
"""

from atlas.forms import BasicSearchForm

def basic_search_form(request):
    return {"basic_search_form" : BasicSearchForm()}
