def chain_of_thought_reasoning(query, context):
    reasoning = f"Step 1: The user asked: '{query}'\n"
    reasoning += f"Step 2: Retrieved relevant information: '{context}'\n"
    reasoning += "Step 3: Formulating an answer based on retrieved context.\n"
    return reasoning