Validation

Typed ffmpeg check the following common error for ffmpeg


0. Not a DAG (it is not possible since the node and stream are made with immutable object)
1. Input / Output not connected (it is check with typed system)
1. Redundant outstream
2. Redundant split
  a. outputs = 1
  b. with redundant outstream
  c. split for input
  d. duplicate split
3. missing Split

Auto Fix

which means you can easy reuse part of previous filter graph and don't need to worry about the missing split.
