from nltk.translate import nist_score


class NISTScorer:
   def __init__(self):
      """
      Initializes the references and hypotheses lists.
      """
      self.hypotheses = []
      self.references = []

   def add_string(self, reference, hypothesis):
      """
      Adds the given hypothesis and reference sentences
      to evaluate them later.
      :param reference: The reference sentence.
      :param hypothesis: The hypothesis sentence.
      """
      self.references.append([reference.split()])
      self.hypotheses.append(hypothesis.split())

   def result_string(self):
      """
      Calculates the `NIST` score for every hypothesis-reference
      pair.
      :returns: The score.
      """
      print(self.references)
      print(self.hypotheses)
      return nist_score.corpus_nist(self.references, self.hypotheses)