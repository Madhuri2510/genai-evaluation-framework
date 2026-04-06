import os
from datetime import datetime

def generate_html_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/report_{timestamp}.html"

    html_content = f"""
    <html>
    <head>
        <title>GenAI Evaluation Report</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            h1 {{ color: #333; }}
            .test {{ border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; }}
            .pass {{ color: green; }}
            .fail {{ color: red; }}
            .warn {{ color: orange; }}
        </style>
    </head>
    <body>
        <h1>GenAI Test Report</h1>
        <p>Generated at: {timestamp}</p>
    """

    for result in results:
        verdict = result["evaluation"]["verdict"]

        css_class = "pass"
        if "FAIL" in verdict:
            css_class = "fail"
        elif "WARNING" in verdict:
            css_class = "warn"

        html_content += f"""
        <div class="test">
            <h3>{result['test_name']}</h3>
            <p><b>Query:</b> {result['query']}</p>
            <p><b>Response:</b> {result['response']}</p>
            <p><b>Scores:</b> {result['evaluation']['scores']}</p>
            <p class="{css_class}"><b>Verdict:</b> {verdict}</p>
        </div>
        """

    html_content += "</body></html>"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filename