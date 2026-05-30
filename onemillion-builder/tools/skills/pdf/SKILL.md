# PDF Generation Skill

Generate professional PDF reports using Python reportlab.

## Install

```bash
pip install reportlab
```

## Basic Report Template

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

def generate_report(output_path: str, title: str, sections: list):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 0.25*inch))
    
    for section in sections:
        story.append(Paragraph(section['heading'], styles['Heading1']))
        story.append(Paragraph(section['body'], styles['Normal']))
        story.append(Spacer(1, 0.1*inch))
    
    doc.build(story)
```

## Table Style

```python
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
    ('PADDING', (0, 0), (-1, -1), 6),
])
```

## Color Palette

| Purpose | Hex |
|---------|-----|
| Primary header | `#1a365d` |
| Dark header | `#1e293b` |
| Critical | `#dc2626` |
| High | `#ea580c` |
| Medium | `#ca8a04` |
| Pass/Low | `#16a34a` |
| Info | `#6b7280` |

## Embedding Images

```python
from reportlab.platypus import Image

img = Image('/path/to/chart.png', width=6*inch, height=3*inch)
story.append(img)
```
