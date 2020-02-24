# Language Model Probabilities

We always represent and compute language model probabilities in log format as __log probabilities__. Since probabilities are (by definition) less than or equal to 1, the more probabilities we multiply together, the smaller the product becomes. __Multiplying enough n-grams together would result in numerical underflow.__ By using log probabilities instead of raw probabilities, we get numbers that are not as small.

Adding in log space is equivalent to multiplying in linear space, so we combine log probabilities by adding them. The result of doing all computation and storage in log space is that we only need to convert back into probabilities if we need to report them at the end; then we can just take the exp of the logprob:

  p1 x p2 x p3 x p4 = exp(log p1 + log p2 + log p3 + log p4)
