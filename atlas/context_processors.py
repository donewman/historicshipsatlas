from atlas.forms import BasicSearchForm, AdvancedSearchForm

def basic_search_form(request):
    return {'basic_search_form' : BasicSearchForm()}

def advanced_search_form(request):
    return {'advanced_search_form' : AdvancedSearchForm()}
