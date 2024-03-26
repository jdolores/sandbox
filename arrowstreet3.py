class WordModifier:
  """
  This class modifies words in a sentence by removing specific endings.

  Attributes:
      suffixes: A tuple containing the suffixes to be removed.
  """

  def __init__(self, suffixes=("ing", "ed", "ly")):
    """
    Initializes the WordModifier class with a list of suffixes to remove.

    Args:
      suffixes: A tuple containing the suffixes to be removed from words (defaults to "ing", "ed", and "ly").
    """
    self.suffixes = suffixes

  def modify_sentence(self, sentence):
    """
    Modifies a sentence by removing the specified suffixes from each word.

    Args:
      sentence: The sentence to be modified.

    Returns:
      A new sentence with the suffixes removed from words.
    """
    modified_words = []
    for word in sentence.lower().split():  # Convert to lowercase for case-insensitive removal
      for suffix in self.suffixes:
        if word.endswith(suffix):
          word = word[:-len(suffix)]  # Slice the word to remove the suffix
          break  # Only remove the first matching suffix
      modified_words.append(word)
    return " ".join(modified_words)

# Example usage
modifier = WordModifier()
original_sentence = "The leaves are falling beautifully in the evening sky."
modified_sentence = modifier.modify_sentence(original_sentence)
print(f"Original sentence: {original_sentence}")
print(f"Modified sentence: {modified_sentence}")