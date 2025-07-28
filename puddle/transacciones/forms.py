from django import forms
from .models import Transaccion

class TransaccionForm(forms.ModelForm):
	class Meta:
		model = Transaccion
		fields = '__all__'
		exclude = ['monto','estado','pais','moneda']
		widgets= {
				'moneda':forms.Select(choices=[('COP','COP'),('USD','USD')]),
                                'PAN_1': forms.TextInput(attrs={'maxlength': '4', 'placeholder': 'XXXX'}),
                                'PAN_2': forms.TextInput(attrs={'maxlength': '4', 'placeholder': 'XXXX'}),
                                'PAN_3': forms.TextInput(attrs={'maxlength': '4', 'placeholder': 'XXXX'}),
                                'PAN_4': forms.TextInput(attrs={'maxlength': '4', 'placeholder': 'XXXX'}),
                                'CVS': forms.TextInput(attrs={'maxlength': '3', 'placeholder': '123'}),
                                'EXP_M': forms.TextInput(attrs={'maxlength': '2','placeholder': '01'}),
                                'EXP_Y': forms.TextInput(attrs={'maxlength': '2','placeholder': '25'}),
		}

	def clean_ultimos_4_digitos(self):
		data = self.cleaned_data['ultimos_4_digitos']
		if not data.isdigit() or len(data) != 4:
			raise forms.ValidationError("Debe ingresar solo los ultimos 4 Digitos de la tarjeta")
		return data


	def clean_monto(self):
		monto = self.cleaned_data['monto']
		#if monto <= 0:
		#	raise forms.ValidationError('El monto debe ser mayor a 0')
		return monto
