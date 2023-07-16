from ting_file_management.queue import Queue


def exists_word(word, instance):
    found_word = []
    for file_dict in instance._queue:
        file_name = file_dict["nome_do_arquivo"]
        lines = file_dict["linhas_do_arquivo"]

        occurrences = []
        for line_num, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_num})

        if occurrences:
            found_word.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )

    return found_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
