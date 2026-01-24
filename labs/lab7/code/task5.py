reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org    "},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp    "},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org    "},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp    "}
]

def remove_all_links(text):
    while 'http://' in text or 'https://' in text:
        i = min((text.find(p) for p in ('http://', 'https://') if text.find(p) != -1), default=-1)
        if i == -1:
            break
        j = next((k for k in range(i, len(text)) if text[k].isspace()), len(text))
        text = text[:i] + '[ДАННЫЕ УДАЛЕНЫ]' + text[j:]
    return text

filtered_reports_sanitized = [
    {"author": r["author"], "text": remove_all_links(r["text"])}
    for r in reports if 'http://' in r["text"] or 'https://' in r["text"]
]

print(filtered_reports_sanitized)
