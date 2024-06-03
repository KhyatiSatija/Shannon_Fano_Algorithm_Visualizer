from typing import List, Tuple, Dict

def shannon_fano(symbols: List[str], probabilities: List[float]) -> Dict[str, str]:
    """Generate Shannon-Fano codes for the given symbols and probabilities."""
    
    # Pair symbols with their probabilities and sort them in descending order
    symbols_prob = sorted(zip(symbols, probabilities), key=lambda x: x[1], reverse=True)
    
    def shannon_split_best(symbols_prob: List[Tuple[str, float]]) -> Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]:
        """Find the best split position that minimizes the absolute difference in probabilities."""
        total_prob = sum(prob for _, prob in symbols_prob)
        diffs = {
            split_pos: abs(sum(prob for _, prob in symbols_prob[:split_pos]) - (total_prob - sum(prob for _, prob in symbols_prob[:split_pos])))
            for split_pos in range(1, len(symbols_prob))
        }
        best_split = min(diffs, key=diffs.get)
        return symbols_prob[:best_split], symbols_prob[best_split:]
    
    def assign_codes(symbols_prob: List[Tuple[str, float]], code_prefix: str) -> Dict[str, str]:
        """Recursively assign codes to symbols based on the Shannon-Fano algorithm."""
        if len(symbols_prob) == 1:
            symbol, _ = symbols_prob[0]
            return {symbol: code_prefix}
        
        left_part, right_part = shannon_split_best(symbols_prob)
        left_codes = assign_codes(left_part, code_prefix + '1')
        right_codes = assign_codes(right_part, code_prefix + '0')
        
        return {**left_codes, **right_codes}
    
    return assign_codes(symbols_prob, '')