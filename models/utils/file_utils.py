import json


def parse_zaloqa22(infile):
    outfile = infile.replace('.json', '_squad.json')
    json_data = json.load(open(infile, 'r'))
    n_sample = json_data['_count_']
    n_full, n_false, n_partial = 0, 0, 0
    data = []
    for item in json_data['data']:
        _id = item['id']
        question = item['question']
        title = item['title']
        text = item['text']
        category = item['category']
        is_long_answer = item['is_long_answer']
        if category == 'FULL_ANNOTATION':
            n_full += 1

            short_candidate_start = item['short_candidate_start']
            short_candidate = item['short_candidate']
            answer = item['answer']

            if is_long_answer:
                is_imposible = False
            else:
                is_imposible = True

            paragraph = [
                {
                    'id': _id,
                    'qas': [
                        {
                            'question': question,
                            'answers': [
                                {
                                    'text': short_candidate,
                                    'answer_start': short_candidate_start,
                                    'answer': answer
                                },
                            ],
                            'is_impossible': is_imposible
                        }
                    ],
                    'context': text
                }
            ]
            data.append({
                'title': title,
                'paragraphs': paragraph
            })
        elif category == 'FALSE_LONG_ANSWER':
            n_false += 1
            paragraph = [
                {
                    'id': _id,
                    'qas': [
                        {
                            'question': question,
                            'answers': [
                            ],
                            'is_impossible': True
                        }
                    ],
                    'context': text
                }
            ]
            data.append({
                'title': title,
                'paragraphs': paragraph
            })

        elif category == 'PARTIAL_ANNOTATION':
            n_partial += 1
            pass
    squad_sample = {
        'n_sample': n_sample,
        'n_full_annotation': n_full,
        'n_false_long_answer': n_false,
        'n_partial_annotation': n_partial,
        'data': data
    }

    json.dump(squad_sample, open(outfile, 'w'), indent=4, ensure_ascii=False)