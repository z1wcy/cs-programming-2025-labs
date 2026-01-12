reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org  "},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp  "},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org  "},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp  "}
]

reports_with_links = filter(
    lambda report: 'http://' in report["text"] or 'https://' in report["text"],
    reports
)

def replace_first_link(text):
    http_pos = text.find('http://')
    https_pos = text.find('https://')

    start_pos = min((pos for pos in [http_pos, https_pos] if pos != -1), default=-1)

    if start_pos == -1:
        return text

    end_pos = len(text)
    for i in range(start_pos, len(text)):
        if text[i].isspace():
            end_pos = i
            break

    new_text = text[:start_pos] + '[ДАННЫЕ УДАЛЕНЫ]' + text[end_pos:]
    return new_text

def remove_all_links(text):
    current_text = text
    while 'http://' in current_text or 'https://' in current_text:
        new_text = replace_first_link(current_text)
        if new_text == current_text:
            break
        current_text = new_text
    return current_text

filtered_reports_sanitized = list(map(
    lambda report: {
        "author": report["author"],
        "text": remove_all_links(report["text"])
    },
    reports_with_links
))

print(filtered_reports_sanitized)