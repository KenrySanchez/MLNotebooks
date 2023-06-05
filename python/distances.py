class Metrics():
   def euclidean_distance(self, X, Y):
       return sum([(x-y)**2 for x, y in zip(X, Y)]) ** (1/2)

   def manhattan_distance(self, X, Y):
       return sum([abs(x-y) for x, y in zip(X, Y)])

   def cosine_similarity(self, X, Y):
       product = sum([(x*y) for x, y in zip(X, Y)])
       mod_x = sum([(x)**2 for x in X])** (1/2)
       mod_y = sum([(y)**2 for y in Y])** (1/2)

       return product / (mod_x*mod_y)

   def jaccard_similarity(self, X, Y):
       return len(set(X).intersection(Y))/len(set(X).union(Y))


def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]
