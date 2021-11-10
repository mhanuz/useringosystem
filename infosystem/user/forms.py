from django import forms
from .models import Person, District,Division,PoliceStation

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'village','post_code','division','district', 'policstation')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()

        if 'division' in self.data:
            print('division is in data')
            try:
                division_id = int(self.data.get('division'))
                self.fields['district'].queryset = District.objects.filter(division_id=division_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.division.district_set.order_by('name')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['policstation'].queryset = PoliceStation.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['policstation'].queryset = PoliceStation.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client
        elif self.instance.pk:
            self.fields['policstation'].queryset = self.instance.district.policestation_set.order_by('name')
