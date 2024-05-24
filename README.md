Take Home Test: Reformat a Public Dataset for LLM Training

Objective

The goal of this task is to prepare public datasets for more effective use in training and fine-tuning Large Language Models (LLMs). You are required to reformat a specific subset of a public dataset into a structured, consistent format to facilitate its usability.
Detailed Instructions

1. Dataset Selection and Preparation

Dataset: You are assigned the Headline subset of the AdaptLLM/finance-tasks dataset.
Task Description: Each entry in the input column contains multiple "Yes" or "No" questions alongside their respective answers. Your task is to:
Develop a Python script to parse and separate each question and its answer from the entry.
Save each question-answer pair in a structured JSON format as follows:
{
  "id": "<unique_identifier>",
  "Question": "<question_text>",
  "Answer": "<answer_text>"
}
You are encouraged to introduce additional attributes if needed to preserve the integrity and completeness of the information. Adding relevant tag information is strongly recommended.
Automation Requirement: The task must be completed using Python. Manual editing or data manipulation is strictly prohibited. Your script should efficiently handle variations in data format within the column.

2. Deliverables

Reformatted Dataset: Provide the schema of the final format you adopted for saving the results.
Transformation Code: Submit the complete code used for converting the dataset into the designated format.
Statistics: Report the total number of question-answer pairs extracted from the dataset.
Performance Metrics: Document the time taken to complete the dataset cleanup and transformation process.

数据集文件：headline.json
数据处理python脚本：dataprocess.py
输出结果文件：output.json
输出总问答对数：102735
运行时间：2.67秒
