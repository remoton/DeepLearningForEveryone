import tensorflow as tf
import matplotlib.pyplot as plt

# observation data -> linear relation
X=[1,2,3]
Y=[1,2,3]

W=tf.placeholder(tf.float32)

# our hypothesis for linear model -> X * W
hypothesis = X*W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis-Y))

