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