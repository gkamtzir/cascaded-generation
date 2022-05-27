from rouge import Rouge


class RougeScorer:
   def __init__(self):
      """
      Initializes `Rouge` scorer. 
      """
      self.scorer = Rouge()
      self.hypothesis = []
      self.references = []

   def add_string(self, reference, hypothesis):
      """
      Adds the given hypothesis and reference sentences
      to evaluate them later.
      :param reference: The reference sentence.
      :param hypothesis: The hypothesis sentence.
      """
      self.references.append(reference)
      self.hypothesis.append(hypothesis)

   def result_string(self):
      """
      Calculates the `Rouge` score of every hypothesis-reference
      pair.
      """
      return self.scorer.get_scores(self.hypothesis, self.references, avg=True)