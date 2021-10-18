from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите поисковый запрос', 'aria-label':'Request', 'aria-describedby':'button-addon2'}))
