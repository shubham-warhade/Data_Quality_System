from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def generate_report(summary, recommendations, filename):

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph("<b>QualiAI Report</b>", styles["Title"])
    )

    story.append(
        Paragraph("<br/><br/>", styles["Normal"])
    )

    # Summary
    for key, value in summary.items():

        story.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    # Recommendations
    story.append(
        Paragraph("<br/><br/><b>Recommendations</b>", styles["Heading2"])
    )

    for rec in recommendations:

        story.append(
            Paragraph(f"• {rec}", styles["Normal"])
        )

    doc.build(story)