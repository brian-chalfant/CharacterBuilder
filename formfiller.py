import io

import pdfrw

from reportlab.pdfgen import canvas


def run():
    canvas_data = get_overlay_canvas()
    form = merge(canvas_data, template_path='./DnD_5E_CharacterSheet - Form Fillable.pdf')
    save(form, filename='merged.pdf')


def get_overlay_canvas() -> io.BytesIO:
        data = io.BytesIO()
        pdf = canvas.Canvas(data)
        pdf.drawString(x=87, y=115, text="Character Name")
        pdf.drawString(x=384, y=84, text='Wizard 1')
        pdf.drawString(x=540, y=84, text='Acolyte')
        pdf.drawString(x=384, y=122, text='Air Genasi')
        pdf.drawString(x=540, y=122, text='Lawful Good')
        pdf.drawString(x=65, y=242, text='15')
        pdf.drawString(x=71, y=278, text='+2')
        pdf.drawString(x=65, y=348, text='11')
        pdf.drawString(x=71, y=375, text='0')
        pdf.drawString(x=65, y=443, text='17')
        pdf.drawString(x=71, y=474, text='+3')

        pdf.save()
        data.seek(0)
        return data


def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
        template_pdf = pdfrw.PdfReader(template_path)
        overlay_pdf = pdfrw.PdfReader(overlay_canvas)
        for page, data in zip(template_pdf.pages, overlay_pdf.pages):
            overlay = pdfrw.PageMerge().add(data)[0]
            pdfrw.PageMerge(page).add(overlay).render()
        form = io.BytesIO()
        pdfrw.PdfWriter().write(form, template_pdf)
        form.seek(0)
        return form


def save(form: io.BytesIO, filename: str):
    with open(filename, 'wb') as f:
        f.write(form.read())


if __name__ == '__main__':
    run()

