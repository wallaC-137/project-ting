def test(word, instance, content=1):
    found_word = []
    for file_dict in instance._queue:
        file_name = file_dict["nome_do_arquivo"]
        lines = file_dict["linhas_do_arquivo"]

        occurrences = []
        for line_num, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_num, "conteudo": line})

        print(f"resultado espera: {occurrences}")

        if occurrences:
            found_word.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )

    # deletar chave content do found_word
    if content == 0:
        for found in occurrences:
            del found["conteudo"]

    return found_word


def exists_word(word, instance):
    # found_word = []
    # for file_dict in instance._queue:
    #     file_name = file_dict["nome_do_arquivo"]
    #     lines = file_dict["linhas_do_arquivo"]

    #     occurrences = []
    #     for line_num, line in enumerate(lines, start=1):
    #         if word.lower() in line.lower():
    #             occurrences.append({"linha": line_num})

    #     if occurrences:
    #         found_word.append(
    #             {
    #                 "palavra": word,
    #                 "arquivo": file_name,
    #                 "ocorrencias": occurrences,
    #             }
    #         )

    return test(word, instance, content=0)


def search_by_word(word, instance):
    found = test(word, instance)
    if not found:
        return []

    return test(word, instance)
