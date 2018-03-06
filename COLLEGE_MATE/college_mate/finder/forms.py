from django import forms
from finder.models import Post


class FinderForm(forms.ModelForm):
	 post=forms.CharField(max_length=500)
	

	 class Meta:
		 model=Post
		 fields=('post',
				'image',
				)
