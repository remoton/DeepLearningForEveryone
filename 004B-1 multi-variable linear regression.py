import tensorflow as tf

# data
x_data=[[73,80,75],[93,88,93],[89,91,90],[96,98,100],[73,66,70]]
y_data=[[152],[185],[180],[196],[142]]

# placeholder
X=tf.placeholder(tf.float32,shape=[None,3])
Y=tf.placeholder(tf.float32,shape=[None,1])

# variables
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
for step in range(200001):
	cost_val, hy_val, _ =sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})
	if step%10==0:
		print(step, "cost:", cost_val, "\nPrediction:\n", hy_val)
		
	