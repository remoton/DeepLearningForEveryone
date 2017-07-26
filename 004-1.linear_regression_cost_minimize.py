import tensorflow as tf
import matplotlib.pyplot as plt
tf.set_random_seed(777) # for reproducibility

# observation data -> It seems to be linear relation
X=[1,2,3]
Y=[1,2,3]

W=tf.placeholder(tf.float32)

# our hypothesis for linear model -> X * W
hypothesis = X*W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis-Y))

# Lauch the graph in a Session
sess=tf.Session()

# variables for plotting cost function
W_history=[]
cost_history=[]

# Initiallize global variables in the graph
# sess.run(tf.global_variables_initializer())

for i in range(-30,50):
	curr_W = i*0.1
	curr_cost = sess.run(cost, feed_dict={W: curr_W})
	W_history.append(curr_W)
	cost_history.append(curr_cost)
	
# Show the cost function
plt.plot(W_history,cost_history)
plt.show()
