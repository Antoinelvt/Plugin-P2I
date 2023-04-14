__title__ = "Informations generales 3"
__author__ = "Antoine Levert"
__doc__ = """Ceci est le bouton d'informations"""


#VARIABLES
uidoc = __revit__.ActiveUIDocument

# CUSTOM IMPORT
from Snippets._selection import get_selected_elements

if __name__ == '__main__':
    print (get_selected_elements(uidoc))

