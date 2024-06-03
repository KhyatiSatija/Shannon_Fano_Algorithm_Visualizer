# Shannon_Fano_Algorithm_Visualizer

Conversation with ChatGPT:

- [Link 1](https://chatgpt.com/share/48c3e2f2-e04d-4a47-871b-1e01bad583fb)
- [Link 2](https://chatgpt.com/share/0c60cda9-b2ee-452e-985a-d09343e986f3)

Collab Notebook:

- [Notebook Link](https://colab.research.google.com/drive/1iNqUznoF2nDKdOS7XG0-85iJyzBttVeD?usp=sharing)

## Run `example.py` to get the visualization.
### Shannon-Fano Algorithm

The Shannon-Fano algorithm is a technique used for lossless data compression, primarily in the field of information theory. Named after Claude Shannon and Robert Fano, it's one of the early techniques developed for data compression.

#### Algorithm Steps:

1. **Sorting Symbols**: Given a set of symbols and their probabilities, sort the symbols in descending order of probability.
2. **Recursive Division**: Recursively divide the sorted symbols into two groups such that the total probabilities of the two groups are as close as possible.
3. **Assigning Binary Codes**: Assign the bit '0' to one group and '1' to the other.
4. **Repetition**: Repeat the process for each group until each symbol has its unique binary code.

The resulting binary codes are uniquely decodable, meaning no code is a prefix of another code, ensuring lossless compression. While the Shannon-Fano algorithm was an important step in the development of data compression techniques, it's less efficient than later algorithms like Huffman coding, which achieves better compression ratios by assigning shorter codes to more frequent symbols.
