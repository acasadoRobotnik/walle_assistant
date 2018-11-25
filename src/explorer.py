import random

class Explorer():
  def __init__(self):
    pass

  def search(self, query, receiver):
    pass

  def no_luck_msg(self, query, source):
    messages = ["Seems like there are no docs referring to '{}' on {} :sad:", "We had no luck searching '{}' on {}"]
    messages = list(map(lambda msg: msg.format(query, source), messages))
    return random.sample(messages, 1)[0]

  def success_msg(self, query, source):
    messages = ["Here's what I've found on {} about '{}': 🐙\n", "Here are your results for '{}' on {}"]
    messages = list(map(lambda msg: msg.format(query, source), messages))
    return random.sample(messages, 1)[0]