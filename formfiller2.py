

import pdfrw

template_path = './DnD_5E_CharacterSheet - Form Fillable.pdf'

output_path = './output.pdf'

annot_key = '/Annots'
annot_field_key = '/T'
annot_val_key = '/V'
annot_rect_key = '/Rect'
subtype_key = '/Subtype'
widget_subtype_key = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][annot_key]
    for annotation in annotations:
        if annotation[subtype_key] == widget_subtype_key:
            if annotation[annot_field_key]:
                key = annotation[annot_field_key][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


data_dict = {

    'AC': '12',
    'Acrobatics': 1,
    'Age': '34',
    'Alignment':'Lawful Good',
    'Animal': 1,
    'Arcana': 1
            }


if __name__ == '__main__':
    write_fillable_pdf(template_path, output_path, data_dict)