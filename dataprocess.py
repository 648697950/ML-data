import json
import time
from datasets import load_dataset


def find_first_match(text):
    """
    Find which substring appears first from left to right in the given text.
    Return "No" if "No" appears first, otherwise return "Yes".
    """
    pos_no = text.find("No")
    pos_yes = text.find("Yes")

    # If both substrings are not found, return None
    if pos_no == -1 and pos_yes == -1:
        return None

    # If only "No" is found
    if pos_no != -1 and pos_yes == -1:
        return "No"

    # If only "Yes" is found
    if pos_yes != -1 and pos_no == -1:
        return "Yes"

    # If both substrings are found, return the one with the smaller index
    if pos_no < pos_yes:
        return "No"
    else:
        return "Yes"

def parse_questions_answers(entry):
    """
    questions-answers parse
    """
    qas = []
    questions_answers = entry.split('\n\n')
    questions_answers.pop()
    for qa in questions_answers:
        if qa.strip():
            qa = qa.replace('\n', ' ')
            if qa.endswith('Yes') or qa.endswith('No'):
                question, answer = qa.rsplit('?', 1)
                answer = find_first_match(answer)
                qas.append((question.strip() + '?', answer.strip()))
            else:
                print(f'Skipped: {qa}')

    return qas


def process_entries(entries):
    """
    Process each entry to extract question-answer pairs.
    Save them in a structured JSON format.
    """
    processed_data = []
    qid = 0
    for entry in entries:
        qas = parse_questions_answers(entry)
        for question, answer in qas:
            processed_data.append({
                "id": str(qid),
                "Question": question,
                "Answer": answer
            })
            qid += 1
    return processed_data


def save_to_json(data, output_file):
    """
    Save the processed data to a JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    # start time
    start_time = time.time()

    # Load the Headline subset of the AdaptLLM/finance-tasks dataset
    dataset = load_dataset('json', data_files='headline.json')

    # Extract entries from the 'input' column
    entries = dataset['train']['input']

    # Process entries to extract question-answer pairs
    processed_data = process_entries(entries)

    # Save the processed data to a JSON file
    output_file = 'output.json'
    save_to_json(processed_data, output_file)

    # end time
    end_time = time.time()

    # take time
    elapsed_time = end_time - start_time

    print(f"Processed data saved to {output_file}")
    print('question-answers sum：' + str(len(processed_data)))
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
