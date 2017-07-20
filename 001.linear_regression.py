#1. Build Graph Using TensorFlow--------------------------------
import tensorflow as tf

# x and y data
x_train=[1,2,3]
y_train=[1,2,3]

W=tf.Variable(tf.random_normal([1]), name='weight')
b=tf.Variable(tf.random_normal([1]), name='bias')

# our hypothesis is linear, W*x+b
hypothesis=x_train*W + b

# cost/loss function
cost=tf.reduce_mean(tf.square(hypothesis-y_train))

#minimize cost
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)

#2. Launch the Graph in a Session--------------------------------
sess=tf.Session()
#initialize global variables in the graph
#sess.run(tf.global_variables_initializer())
sess.run(tf.global_variables_initializer())
#Fit the line
for step in range(2001):
	sess.run(train)
	if step % 20 == 0:
		print(step, sess.run(cost), sess.run(W), sess.run(b))


