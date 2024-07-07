from django import forms

PRODUCT_IDS = [
    ("B004Q7CK9M", "Most Reviews - B004Q7CK9M"),
    ("B004LLIKVU", "2nd Most Reviews - B004LLIKVU"),
    ("B0091JKVU0", "3rd Most Reviews - B0091JKVU0"),
    ("B00JDQJZWG", "4th Most Reviews - B00JDQJZWG"),
    ("B0091JKY0M", "5th Most Reviews - B0091JKY0M"),
    ("B014S24DAI", "6th Most Reviews - B014S24DAI"),
    ("B004LLIKY2", "7th Most Reviews - B004LLIKY2"),
    ("B0066AZGD4", "8th Most Reviews - B0066AZGD4"),
    ("B00H5BMH44", "9th Most Reviews - B00H5BMH44"),
    ("B0091JL3OI", "Least Reviews - B0091JL3OI"),
    ("B017THJLZG", "Bad Product - B017THJLZG"),
]

ALGORITHMS = [
    ('random_forest_model', 'Random Forest'),
    ('naive_bayes_model', 'Naive Bayes'),
    ('svm_model', 'SVM'),
    ('xg_boost_model', 'XGBoost'),
]


class ProductSearchForm(forms.Form):
    product_id = forms.ChoiceField(choices=PRODUCT_IDS, label='Choose Product ID')
    algorithm = forms.ChoiceField(choices=ALGORITHMS, label='Choose Algorithm')
