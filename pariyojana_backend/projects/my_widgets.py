# my_widgets.py
from import_export.widgets import ForeignKeyWidget

class SafeForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value in [None, ""]:
            return None
        return self.model.objects.filter(**{self.field: value}).first()
