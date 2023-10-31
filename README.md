# LocalFileSearchEngine
A search engine locally for your files

## How it Works?
- Simply type the name of the file you're looking for
- A result will return with listings of entire directories with all the possible matches.

## Initial Problem I ran into:
- Every new search index was cleared and a re-index process occurs.
- This lead the search module to have a time complexity of *O(n^3)* which is very slow for a search engine

## Solution:
- Implement Incremental Indexing
- Instead of re-indexing the entire dataset we would update the index with new or modified content.