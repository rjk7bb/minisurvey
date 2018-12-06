from django import forms


class Question1(forms.Form):
    number = forms.IntegerField(min_value=0, max_value=100, label='', required=False)

    def clean(self):
        cleaned_data = super(Question1, self).clean()
        num = cleaned_data.get('number')
        if not num:
            raise forms.ValidationError('Enter a number.')


class Question2(forms.Form):
    Choices = (('Extremely below average', 'Extremely below average'),
               ('Moderately below average', 'Moderately below average'),
               ('Slightly below average', 'Slightly below average'),
               ('Average', 'Average'),
               ('Slightly above average', 'Slightly above average'),
               ('Moderately above average', 'Moderately above average'),
               ('Extremely above average', 'Extremely above average'))
    Options = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect, label='')


class Question3(forms.Form):
    response = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': 7, 'cols': 20}), label='', max_length=140,
                               required=False)


class Question4(forms.Form):
    response = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': 7, 'cols': 20}), label='', max_length=140,
                               required=False)


    # def clean(self):
    #     cleaned_data = super(Question4, self).clean()
    #     resp = cleaned_data.get('response')
    #     if not resp:
    #         raise forms.ValidationError('Enter a response.')



class Question5(forms.Form):
    Choices = (('ABC Chief White House Correspondent', 'ABC Chief White House Correspondent'),
               ('ABC Digital Correspondent', 'ABC Digital Correspondent'),
               ('ABC Medical Correspondent', 'ABC Medical Correspondent'),
               ('ABC Policy Analyst', 'ABC Policy Analyst'),
               ('Assistant Director FBI', 'Assistant Director FBI'),
               ('Attorney General', 'Attorney General'),
               ('CBS Chief White House Correspondent', 'CBS Chief White House Correspondent'),
               ('CBS Digital Correspondent', 'CBS Digital Correspondent'),
               ('CBS Medical Correspondent', 'CBS Medical Correspondent'),
               ('CBS Political Analyst', 'CBS Political Analyst'),
               ('Deputy Attorney General', 'Deputy Attorney General'),
               ('Deputy Press Secretary', 'Deputy Press Secretary'),
               ('Deputy Secretary of State', 'Deputy Secretary of State'),
               ('Director of National Intelligence', 'Director of National Intelligence'),
               ('National Security Advisor', 'National Security Advisor'),
               ('NBC Chief White House Correspondent', 'NBC Chief White House Correspondent'),
               ('NBC Digital Correspondent', 'NBC Digital Correspondent'),
               ('NBC Medical Correspondent', 'NBC Medical Correspondent'),
               ('NBC Political Analyst', 'NBC Political Analyst'),
               ('Presidential Physician', 'Presidential Physician'),
               ('Secret Service agent-In-Charge', 'Secret Service agent-In-Charge'),
               ('Secretary of Commerce', 'Secretary of Commerce'),
               ('Secretary of Defense', 'Secretary of Defense'),
               ('Secretary of Homeland Security', 'Secretary of Homeland Security'),
               ('Secretary of State', 'Secretary of State'),
               ('Secretary of Transportation', 'Secretary of Transportation'),
               ('Secretary of Treasury', 'Secretary of Treasury'),
               ('Special Assistant to the President', 'Special Assistant to the President'),
               ('White House Chief of Staff', 'White House Chief of Staff'),
               ('White House Communications Director', 'White House Communications Director'),
               ('White House Counsel', 'White House Counsel'),
               ('White House Political Director', 'White House Political Director'))

    Options = forms.CharField(label='', widget=forms.Select(choices=Choices), required=False)


class Question7(forms.Form):
    yn = forms.CharField(label='', widget=forms.Select(choices=(('Yes', 'Yes'), ('No', 'No'))), required=False)
    response = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': 7, 'cols': 20}), label='', max_length=140,
                               required=False)
    response2 = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': 7, 'cols': 20}), label='', max_length=140,
                                required=False)


class Question10(forms.Form):
    options = (('Invoke', 'Invoke'), ('Not Invoke', 'Not Invoke'))
    q1 = 'I would invoke/not invoke the 25th Amendment'
    option = forms.CharField(widget=forms.Select(choices=options), required=False)
    q2 = 'One reason for this decision is:'
    q2a = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 7, 'cols': 20}), max_length=140,
                          required=False)
    q3 = 'Another reason is:'
    q3a = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 7, 'cols': 20}), max_length=140,
                          required=False)
    q4 = 'A final reason is:'
    q4a = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 7, 'cols': 20}), max_length=140,
                          required=False)


class Question11(forms.Form):
    Choices = (('Strongly Agree', 'Strongly Agree'),
               ('Agree', 'Agree'),
               ('Somewhat Agree', 'Somewhat Agree'),
               ('Neither Agree nor Disagree', 'Neither Agree nor Disagree'),
               ('Somewhat Disagree', 'Somewhat Disagree'),
               ('Disagree', 'Disagree'),
               ('Strongly Disagree', 'Strongly Disagree'))
    option = forms.ChoiceField(choices=Choices, label='', widget=forms.RadioSelect)


class Question12(forms.Form):
    Response = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 7, 'cols': 20}), max_length=140,
                               required=False)
    """
    def clean(self):
        cleaned_data = super(Question12, self).clean()
        resp = cleaned_data
        if not resp:
            raise forms.ValidationError('Write a response')
    """


class Question13(forms.Form):
    Choices = (('Extremely positive', 'Extremely positive'),
               ('Moderately positive', 'Moderately positive'),
               ('Slightly positive', 'Slightly positive'),
               ('Neither positive nor negative', 'Neither positive nor negative'),
               ('Slightly negative', 'Slightly negative'),
               ('Moderately negative', 'Moderately negative'),
               ('Extremely negative', 'Extremely negative'))
    Options = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect, label='')


class Question14(forms.Form):
    comment = forms.CharField(label='', widget=forms.widgets.Textarea(attrs={'rows': 7, 'cols': 20}), max_length=140,
                              required=False)

    # def clean(self):
    #     cleaned_data = super(Question14, self).clean()
    #     resp = cleaned_data.get('comment')
    #     if not resp:
    #         raise forms.ValidationError('Write a response')


class Question15(forms.Form):
    comment1 = forms.CharField(label='', widget=forms.widgets.Textarea(attrs={'rows': 7, 'cols': 20}),
                               max_length=140)
    comment2 = forms.CharField(label='', max_length=20)
