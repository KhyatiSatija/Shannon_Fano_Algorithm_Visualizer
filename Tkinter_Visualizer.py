from shannon_fano import *
import tkinter as tk

def shannon_split_best(symbols_prob: List[Tuple[str, float]]) -> Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]:
    """Find the best split position that minimizes the absolute difference in probabilities."""
    total_prob = sum(prob for _, prob in symbols_prob)
    diffs = {
        split_pos: abs(sum(prob for _, prob in symbols_prob[:split_pos]) - (total_prob - sum(prob for _, prob in symbols_prob[:split_pos])))
        for split_pos in range(1, len(symbols_prob))
    }
    best_split = min(diffs, key=diffs.get)
    return symbols_prob[:best_split], symbols_prob[best_split:]

def draw_tree(canvas, x, y, symbols_prob, code_prefix, x_offset, y_offset):
    if len(symbols_prob) == 1:
        symbol, prob = symbols_prob[0]
        canvas.create_text(x, y, text=f"{symbol} ({prob:.2f})", font=("Helvetica", 12), anchor="w")
        canvas.create_text(x, y + 20, text=f"{code_prefix}", font=("Helvetica", 12), anchor="w")
        return x

    left_part, right_part = shannon_split_best(symbols_prob)
   
    # Calculate positions for children
    left_x = draw_tree(canvas, x - x_offset, y + y_offset, left_part, code_prefix + '1', x_offset // 2, y_offset)
    right_x = draw_tree(canvas, x + x_offset, y + y_offset, right_part, code_prefix + '0', x_offset // 2, y_offset)

    mid_x = (left_x + right_x) // 2
    canvas.create_line(x, y + 20, left_x, y + y_offset - 20, arrow=tk.LAST)
    canvas.create_line(x, y + 20, right_x, y + y_offset - 20, arrow=tk.LAST)
    canvas.create_text(left_x, y + y_offset - 30, text="1", font=("Helvetica", 12), anchor="s")
    canvas.create_text(right_x, y + y_offset - 30, text="0", font=("Helvetica", 12), anchor="s")
   
    return mid_x

def visualize_shannon_fano(symbols, probabilities):
    root = tk.Tk()
    root.title("Shannon-Fano Tree")

    canvas = tk.Canvas(root, width=1500, height=800, bg="white")
    canvas.pack()

    symbols_prob = sorted(zip(symbols, probabilities), key=lambda x: x[1], reverse=True)
    draw_tree(canvas, 750, 20, symbols_prob, '', 300, 80)

    root.mainloop()

    