from django import forms
from .models import Diario

class DiarioForm(forms.ModelForm):

	class Meta:
		model = Diario
		fields = ('fecha', 'id_cta', 'importe', 'ref',)
