import tensorflow as tf
import matplotlib.pyplot as plt
X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.placeholder(tf.float32)
#Our hypothesis for linear model X * W
hypothesis = X * W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))
# Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())
# Variables for plottinf cost function
W_val = []
cost_val = []
for i in range (-30, 50):
    feed_W = i * 0.1
    curr_cost, curr_w = sess.run([cost,W], feed_dict={W: feed_W})
    W_val.append(curr_w)
    cost_val.append(curr_cost)


# Show the cost function
plt.plot(W_val, cost_val)
plt.show()
