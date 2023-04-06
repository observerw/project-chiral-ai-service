def summarize_length(doc: str) -> int:
    doc_length = len(doc)

    if doc_length > 8192:
        return 4096

    if doc_length < 100:
        return doc_length
    elif doc_length < 512:
        return int(doc_length * 0.7)
    else:
        return 512
