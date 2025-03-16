def rerank_results(query, results):
    ranked_results = sorted(results, key=lambda x: len(set(query.split()) & set(x.split())), reverse=True)
    return ranked_results