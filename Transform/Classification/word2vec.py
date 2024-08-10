import numpy as np
from collections import defaultdict, Counter

class TfIdf:
    def __init__(self, ducs: list) -> None:
        self.ducs = ducs
        self.size_ducs = len(ducs)
        self.words = self._collect_words()
        self.word_index = {word: idx for idx, word in enumerate(self.words)}
        self.word_count = self._compute_word_count()
        self.idf_values = self._compute_idf()

    def transform(self) -> np.array:
        return self.tf_idf()

    def tf_idf(self) -> np.array:
        vectors = np.zeros((self.size_ducs, len(self.words)))
        for i, duc in enumerate(self.ducs):
            vectors[i] = self._tf_idf(duc)
        return vectors

    def _tf_idf(self, duc: list) -> np.array:
        vector = np.zeros(len(self.words))
        tf = Counter(duc)
        for word in tf:
            if word in self.word_index:
                vector[self.word_index[word]] = (tf[word] / len(duc)) * self.idf_values[word]
        return vector

    def _compute_idf(self) -> dict:
        idf_values = {}
        for word in self.word_index:
            df = self.word_count[word]
            idf_values[word] = np.log(self.size_ducs / (df + 1))  # Added +1 for smoothing
        return idf_values

    def _collect_words(self) -> list:
        words = set()
        for duc in self.ducs:
            words.update(duc)
        return sorted(words)

    def _compute_word_count(self) -> dict:
        word_count = defaultdict(int)
        for duc in self.ducs:
            unique_words = set(duc)
            for word in unique_words:
                word_count[word] += 1
        return word_count
