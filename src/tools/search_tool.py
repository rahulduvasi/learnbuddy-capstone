# src/tools/search_tool.py
# Simple mock search tool - replace with real search API for full demo.
def web_search(query, top_k=3):
    # Mocked responses
    return [
        {'title': f'Resource about {query} - 1', 'url': 'https://example.com/1'},
        {'title': f'Resource about {query} - 2', 'url': 'https://example.com/2'},
        {'title': f'Resource about {query} - 3', 'url': 'https://example.com/3'}
    ]
