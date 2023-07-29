from django import forms
from .models import StudentForm,Courses

class SForm(forms.ModelForm):
    class Meta:
        model = StudentForm
        fields = '__all__'

    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['course'].queryset=Courses.objects.none()
