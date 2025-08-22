
import pydivsufsort
from typing import List


def build_suffix_array(text: str) -> List[int]:
    """Build a suffix array using pysais (fast + memory-efficient)."""
    return pydivsufsort.divsufsort(text)

class SuffixDataset:
    """Dataset of suffixes for given text."""
    def __init__(self, text:str, suffix_array:List[int]):
        self.text = text
        self.suffix_array = suffix_array

    def is_substring(self, query):
        """Check if a query (substring) is in text."""
        return self._binary_search(query)
    
    def _binary_search(self, query:str) -> bool:
        """ binary search on if a query (substring) is in text.
            Args:
                query: str = substring to search for
                text: str = Entire text which suffix array was built from
                suffix_array: list =  Suffix array of text
            Returns:
                bool = True if query is in text, False otherwise.
        
        """
        lo, hi = 0, len(self.suffix_array)
        while lo < hi:
            mid = (lo + hi) // 2
            start = self.suffix_array[mid]
            cmp = self.text[start:start+len(query)]
            if cmp.lower() == query.lower():
                return True
            elif cmp < query:
                lo = mid + 1
            else:
                hi = mid
        return False

    def __len__(self):
        return len(self.suffix_array)