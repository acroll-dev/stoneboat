from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas

NAVY = HexColor("#0b2545")
HARBOR = HexColor("#1d4e89")
ROPE = HexColor("#c9a66b")
SAND = HexColor("#f4efe6")
INK = HexColor("#07172c")
FOAM = HexColor("#e8eef5")

def header_footer(canv, doc):
    canv.saveState()
    # Top nautical band
    canv.setFillColor(NAVY)
    canv.rect(0, LETTER[1]-0.55*inch, LETTER[0], 0.55*inch, fill=1, stroke=0)
    canv.setFillColor(ROPE)
    canv.rect(0, LETTER[1]-0.60*inch, LETTER[0], 0.05*inch, fill=1, stroke=0)
    canv.setFillColor(ROPE)
    canv.setFont("Helvetica-Bold", 11)
    canv.drawString(0.7*inch, LETTER[1]-0.35*inch, "⚓  STONEBOAT QUAY")
    canv.setFillColor(FOAM)
    canv.setFont("Helvetica", 9)
    canv.drawRightString(LETTER[0]-0.7*inch, LETTER[1]-0.35*inch,
                         "Modernization Project  ·  100 Bronte Road")
    # Footer band
    canv.setFillColor(NAVY)
    canv.rect(0, 0, LETTER[0], 0.45*inch, fill=1, stroke=0)
    canv.setFillColor(ROPE)
    canv.rect(0, 0.45*inch, LETTER[0], 0.04*inch, fill=1, stroke=0)
    canv.setFillColor(FOAM)
    canv.setFont("Helvetica", 8)
    canv.drawString(0.7*inch, 0.2*inch,
                    "Design: Clinton Design Inc. (clintondesign.ca)  ·  Management: CIE (teamcie.ca)")
    canv.drawRightString(LETTER[0]-0.7*inch, 0.2*inch, f"Page {doc.page}")
    canv.restoreState()

doc = SimpleDocTemplate(
    "/sessions/festive-tender-hopper/mnt/outputs/Stoneboat_Quay_Handout.pdf",
    pagesize=LETTER, topMargin=0.9*inch, bottomMargin=0.7*inch,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    title="Stoneboat Quay Modernization Handout")

styles = getSampleStyleSheet()
title = ParagraphStyle('t', parent=styles['Title'], fontName='Helvetica-Bold',
                       textColor=NAVY, fontSize=22, leading=26, spaceAfter=6, alignment=TA_LEFT)
tag = ParagraphStyle('tag', parent=styles['Normal'], fontName='Helvetica-Bold',
                     textColor=ROPE, fontSize=9, leading=12, spaceAfter=2, alignment=TA_LEFT)
h2 = ParagraphStyle('h2', parent=styles['Heading2'], fontName='Helvetica-Bold',
                    textColor=NAVY, fontSize=14, leading=18, spaceBefore=10, spaceAfter=6)
h3 = ParagraphStyle('h3', parent=styles['Heading3'], fontName='Helvetica-Bold',
                    textColor=HARBOR, fontSize=11, leading=14, spaceBefore=6, spaceAfter=2)
body = ParagraphStyle('b', parent=styles['BodyText'], fontName='Helvetica',
                      textColor=INK, fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=6)
small = ParagraphStyle('s', parent=styles['BodyText'], fontName='Helvetica-Oblique',
                       textColor=HARBOR, fontSize=8.5, leading=11, spaceAfter=4)
quote = ParagraphStyle('q', parent=styles['BodyText'], fontName='Helvetica-Oblique',
                       textColor=NAVY, fontSize=10.5, leading=15, leftIndent=14,
                       rightIndent=14, spaceBefore=4, spaceAfter=8,
                       borderPadding=6)

def stat_card(value, label):
    t = Table([[Paragraph(f"<b>{value}</b>", ParagraphStyle(
        'v', fontName='Helvetica-Bold', textColor=HARBOR, fontSize=22, leading=26, alignment=TA_CENTER))],
        [Paragraph(label, ParagraphStyle(
        'l', fontName='Helvetica', textColor=NAVY, fontSize=8.5, leading=11, alignment=TA_CENTER))]],
        colWidths=[2.1*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), SAND),
        ('LINEABOVE',(0,0),(-1,0), 2, ROPE),
        ('TOPPADDING',(0,0),(-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 8),
        ('LEFTPADDING',(0,0),(-1,-1), 6),
        ('RIGHTPADDING',(0,0),(-1,-1), 6),
    ]))
    return t

story = []

story.append(Paragraph("⚓  A FRESH COURSE FOR OUR HARBOUR HOME", tag))
story.append(Paragraph("Stoneboat Quay Modernization", title))
story.append(Paragraph("Hallway &amp; common-area renewal — 100 Bronte Road  ·  65 units  ·  three floors", small))
story.append(Spacer(1, 0.15*inch))

# Intro
story.append(Paragraph(
    "Our hallways and common areas have not been renewed in more than 20 years. "
    "This modernization project refreshes every corridor, every doorway entrance, "
    "and every shared threshold — preserving the character of Stoneboat Quay while "
    "protecting and growing the value of every owner's home.", body))

# Stat row
story.append(Spacer(1, 0.1*inch))
stat_table = Table([[stat_card("20+", "Years since last hallway renewal"),
                     stat_card("5–10%", "Typical value uplift (GTA &amp; comparable markets)"),
                     stat_card("60%", "Faster sales for modernized buildings")]],
                   colWidths=[2.3*inch]*3)
stat_table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(stat_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("Why Now — the GTA Market in 2025–2026", h2))
story.append(Paragraph(
    "Greater Toronto Area condo inventory sits near historic highs. Buyers have more "
    "choice than ever — and they reward buildings that present well. Research from the "
    "2025–2026 Canadian market is consistent: <b>well-priced, well-presented listings "
    "continue to move efficiently</b>, while dated buildings tend to sit on the market "
    "and discount below asking.", body))
story.append(Paragraph(
    "&#8220;Buyers decide whether to buy within the first 60 seconds of entry.&#8221;",
    quote))
story.append(Paragraph(
    "For Stoneboat Quay — a 65-unit, three-storey building on the Lake Ontario harbour — "
    "a refreshed hallway experience is the single highest-impact upgrade we can make.", body))

# Value per unit table
story.append(Paragraph("What It Could Mean Per Unit (Illustrative)", h2))
data = [["Item", "Amount"],
        ["Illustrative per-unit assessment", "$8,000"],
        ["Projected value uplift (5% on a $600,000 unit)", "$30,000"],
        ["Net equity gain per owner", "$22,000"],
        ["Common-area lighting savings (annual)", "15–30%"]]
t = Table(data, colWidths=[4.3*inch, 1.9*inch])
t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0), NAVY),
    ('TEXTCOLOR',(0,0),(-1,0), ROPE),
    ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
    ('FONTNAME',(0,1),(-1,-1),'Helvetica'),
    ('FONTSIZE',(0,0),(-1,-1), 10),
    ('ROWBACKGROUNDS',(0,1),(-1,-1), [white, SAND]),
    ('TEXTCOLOR',(0,1),(-1,-1), INK),
    ('ALIGN',(1,0),(1,-1),'RIGHT'),
    ('BOTTOMPADDING',(0,0),(-1,-1), 7),
    ('TOPPADDING',(0,0),(-1,-1), 7),
    ('LINEBELOW',(0,0),(-1,0), 1.5, ROPE),
]))
story.append(t)
story.append(Paragraph(
    "Figures are illustrative, drawn from GTA and comparable-market research. "
    "Actual assessment and uplift will be confirmed by the Board.", small))

story.append(PageBreak())

story.append(Paragraph("⚓  THE MODERNIZATION", tag))
story.append(Paragraph("What You'll See in the Hallways", title))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Lighter, Warmer Corridors", h3))
story.append(Paragraph(
    "A neutral, light palette replaces our dated finishes. Layered LED lighting — with "
    "occupancy sensors in low-traffic areas — brightens every floor while cutting energy "
    "costs. Crisp new trim and wall treatments make every hallway feel fresh.", body))

story.append(Paragraph("Refreshed Doorway Entrances", h3))
story.append(Paragraph(
    "Every unit gets an upgraded threshold: refreshed door hardware, refined unit numbers, "
    "and a tidy, modern frame that gives every home a proper welcome.", body))

story.append(Paragraph("Durable, Modern Flooring", h3))
story.append(Paragraph(
    "Premium luxury vinyl plank or commercial-grade tile replaces worn carpet — quieter "
    "underfoot, dramatically easier to clean, and designed to look excellent for decades.", body))

story.append(Paragraph("The Market Evidence", h2))
story.append(Paragraph(
    "In Toronto and across the GTA, modernized buildings maintain pricing while comparable "
    "dated buildings discount 3–5% below asking. In Vancouver, modernized units sold in "
    "<b>14 days versus 38</b> for dated stock. New York cooperative data shows "
    "<b>10–15% value uplift</b> from corridor renewal. A long-term case study from the "
    "Dorchester market found hallway and lobby renovation was <b>&#8220;100% helpful&#8221; "
    "to resale for every owner</b> — including units that were never themselves updated.", body))

story.append(Paragraph(
    "&#8220;Beautiful common areas can elevate perceptive value anywhere from 5–10%.&#8221;",
    quote))

# Designer spotlight box
story.append(Paragraph("Designed and Supervised By Clinton Design Inc.", h2))
story.append(Paragraph(
    "Clinton Design Inc. specializes in the refurbishment of condominium common elements "
    "throughout Toronto, the GTA, and the surrounding areas. Their work spans "
    "before-and-after design, 3D renderings, and — through their Design-Build partner "
    "<b>dot dot dot</b> — turnkey delivery from concept to completed construction. Their "
    "construction team prides itself on <b>&#8220;clean and quality work.&#8221;</b> "
    "Studio: 6 Brentcliffe Road, Toronto. Website: clintondesign.ca.", body))

# The voyage
story.append(Paragraph("The Voyage Ahead", h2))
voyage = [
    ("Stage 1 — Design &amp; Renderings",
     "Clinton Design prepares a full concept with before/after renderings, so every owner can see the finished hallways before work begins."),
    ("Stage 2 — Owner Communication",
     "You receive renderings, finish samples, cost breakdowns, and a clear timeline. Nothing is hidden. Questions are welcomed."),
    ("Stage 3 — Phased Construction",
     "Work is scheduled floor by floor to minimize disruption. A safe, clear path to every unit is maintained throughout."),
    ("Stage 4 — Reveal &amp; Value Reset",
     "A completed modernization resets the building's effective age and is reflected in every future Status Certificate."),
]
for t_, d in voyage:
    story.append(Paragraph(t_, h3))
    story.append(Paragraph(d, body))

# Contact box
story.append(Spacer(1, 0.1*inch))
contact = Table([[Paragraph("<b>Questions About the Project?</b><br/><br/>"
                            "Please contact our management company, <b>CIE</b>, "
                            "who are coordinating all owner communication for the modernization.<br/><br/>"
                            "<b>teamcie.ca</b>",
                            ParagraphStyle('c', fontName='Helvetica', fontSize=10,
                                           textColor=FOAM, leading=14))]],
                colWidths=[6.3*inch])
contact.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1), NAVY),
    ('LINEABOVE',(0,0),(-1,0), 3, ROPE),
    ('TOPPADDING',(0,0),(-1,-1), 14),
    ('BOTTOMPADDING',(0,0),(-1,-1), 14),
    ('LEFTPADDING',(0,0),(-1,-1), 18),
    ('RIGHTPADDING',(0,0),(-1,-1), 18),
]))
story.append(contact)

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("PDF built")
