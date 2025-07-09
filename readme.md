# Building Trustworthy LLM Pipelines Workshop

This repository contains materials for the workshop on building trustworthy LLM-based systems, focusing on structured outputs and RAG evaluation. The workshop, organized by **[MACHINERY](https://www.meetup.com/data-science-club-belgrade/)** as part of **[Belgrade's AI Week](https://startit.rs/ai-week/)**, is designed for professionals developing or evaluating LLM-based systems.

## About The Workshop

This workshop dives into two essential components of modern LLM-based systems: structured outputs and RAG evaluation. You will learn how to leverage these techniques to reduce model errors, enforce data consistency, and improve the overall reliability of your applications.

## Repository Structure

This repository is organized into two main parts, corresponding to the two tracks of the workshop:

-   `structured_outputs_applications/`: Contains materials for the first session on Structured Outputs. It includes a hands-on workshop in a Jupyter Notebook (`workshop.ipynb`).
-   `rag_evaluation/`: Contains materials for the second session on RAG Evaluation. It includes a hands-on workshop in a Jupyter Notebook (`rag_workshop.ipynb`).

## Workshop Content

### Structured Outputs with LLMs and its applications

In this part of the workshop, we’ll dive into the power of Structured Outputs in modern LLM-based systems. You’ll learn how they can be used to reduce hallucinations, enforce data integrity, and improve reliability in real-world applications.

**Brief track agenda:**
- What are Structured Outputs, and how do they help mitigate hallucinations?
- Defining schemas for Structured Outputs:
  - Introduction to Pydantic and how to use it for schema definition
- Using Structured Outputs and Visual Language Models for data extraction from invoices
- Applications of Structured Outputs in RAG systems:
  - Enhancing search results with query expansion, suggested time ranges, and data source identification (generate relevant metadata based on a user’s query)
- Reasoning with Structured Outputs (SO):
  - Combining Structured Outputs with custom Chains of Thought and show its application for the RAG systems (Enterprise RAG Challenge Winner: https://abdullin.com/ilya/how-to-build-best-rag/)

### RAG Evaluation

This track covers practical approaches to evaluating RAG pipelines. It includes working with query–document/snippet–answer datasets, using standard retrieval metrics like recall@k, and assessing generation quality with LLM-based evaluators. Participants will also explore how to design custom metrics for citation accuracy, response quality, and text formatting, followed by one iteration of metric improvement.

**Brief track agenda:**
- Understanding the components of a RAG evaluation stack
- Measuring retrieval performance using IR metrics (recall@k on documents, snippets, and citations)
- Evaluating answer quality with LLM-as-a-judge tools (e.g., DeepEval, RAGAS)
- Designing custom metrics for citation relevance and answer usefulness
- Introducing evaluation methods for style and formatting
- Iterating on metric development to refine evaluation signals

## Getting Started

To get started with the workshop materials, you'll need to set up your environment.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <workshop_part>
    ```

3.  **Explore the notebooks:**
    - For the Structured Outputs track, open and run the cells in `structured_outputs_applications/workshop.ipynb`.
    - For the RAG Evaluation track, open `rag_evaluation/rag_workshop.ipynb`. Please check the notebook for any specific dependencies you might need to install.

We hope you find these materials useful. Enjoy the workshop!

The Structured Output session was prepared by Arsenii Shkunkov, and the second part about RAG Evaluation was prepared by Vladimir Ageev.