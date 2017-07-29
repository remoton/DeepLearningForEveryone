import tensorflow as tf
import numpy as np
tf.set_random_seed(777) # for reproducibility

# load and set data from file 
xy=np.loadtxt('data-01-test-score.csv', delimiter=',', dtype=np.float32)

x_data=xy[:, 0:-1]
y_data=xy[:, [-1]]

# make sure the shape and data are OK
print(x_data.shape,'\n', x_data,'\n', len(x_data))
print(y_data.shape,'\n', y_data,'\n', len(y_data))

# placeholder
X=tf.placeholder(tf.float32, shape=[None,3])
Y=tf.placeholder(tf.float32, shape=[None,1])

# trainable variables
W=tf.Variable(tf.random_normal([3,1], name='weight'))
b=tf.Variable(tf.random_normal([1], name='bias'))

# hypothesis
hypothesis=tf.matmul(X,W)+b

# simplified cost functiion
cost=tf.reduce_mean(tf.square(hypothesis-Y))

# minimize cost
optimizer=tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train=optimizer.minimize(cost)

# lauch the graph in a session
sess=tf.Session()
sess.run(tf.global_variables_initializer())

# train
for step in range(2001):
	cost_val, hy_val, _ =sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})
	if step%10==0:
		print(step, "cost:", cost_val, "\nPrediction:\n", hy_val)

# ask my score 
print("your score is ", sess.run(hypothesis, feed_dict={X: [[100,70,101]]}))


