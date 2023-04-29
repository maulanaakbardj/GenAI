import tensorflow as tf
import numpy as np
from PIL import Image

IMAGE_SIZE = 64
BATCH_SIZE = 32
NOISE_SIZE = 100
LEARNING_RATE = 0.0002
BETA1 = 0.5
EPOCHS = 5000

def generator(noise, text):
    with tf.variable_scope("generator"):
        # concatenate the noise and text inputs
        inputs = tf.concat([noise, text], axis=1)

        # create the generator network with 3 fully connected layers
        x = tf.layers.dense(inputs, 1024, activation=tf.nn.relu)
        x = tf.layers.dense(x, 4 * 4 * 256, activation=tf.nn.relu)
        x = tf.reshape(x, [-1, 4, 4, 256])
        x = tf.layers.conv2d_transpose(x, 128, 5, strides=2, padding="same", activation=tf.nn.relu)
        x = tf.layers.conv2d_transpose(x, 64, 5, strides=2, padding="same", activation=tf.nn.relu)
        x = tf.layers.conv2d_transpose(x, 3, 5, strides=2, padding="same", activation=tf.nn.sigmoid)

        return x

def discriminator(image, text, reuse=False):
    with tf.variable_scope("discriminator", reuse=reuse):
        # concatenate the image and text inputs
        inputs = tf.concat([image, text], axis=1)

        # create the discriminator network with 3 convolutional layers
        x = tf.layers.conv2d(inputs, 64, 5, strides=2, padding="same", activation=tf.nn.leaky_relu)
        x = tf.layers.conv2d(x, 128, 5, strides=2, padding="same", activation=tf.nn.leaky_relu)
        x = tf.layers.conv2d(x, 256, 5, strides=2, padding="same", activation=tf.nn.leaky_relu)
        x = tf.layers.flatten(x)
        x = tf.layers.dense(x, 1)

        return x

def train():
    # load the text dataset
    text_file = "text_dataset.txt"
    with open(text_file, "r") as f:
        text_lines = f.readlines()

    # load the image dataset
    image_folder = "image_dataset"
    image_files = tf.data.Dataset.list_files(image_folder + "/*.jpg")
    image_dataset = image_files.map(lambda x: tf.image.decode_jpeg(tf.io.read_file(x), channels=3))
    image_dataset = image_dataset.map(lambda x: tf.image.resize_images(x, [IMAGE_SIZE, IMAGE_SIZE]))
    image_dataset = image_dataset.batch(BATCH_SIZE)
    iterator = image_dataset.make_initializable_iterator()
    next_batch = iterator.get_next()

    # create the noise placeholder
    noise = tf.placeholder(tf.float32, [None, NOISE_SIZE])

    # create the text placeholder
    text = tf.placeholder(tf.float32, [None, len(text_lines)])

    # create the generator and discriminator models
    gen_images = generator(noise, text)
    real_images = next_batch
    disc_real = discriminator(real_images, text)
    disc_fake = discriminator(gen_images, text, reuse=True)

    # calculate the loss for the generator and discriminator models
    gen_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=disc_fake, labels=tf.ones_like(disc_fake)))
    disc_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits
(logits=disc_real, labels=tf.ones_like(disc_real)))
disc_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=disc_fake, labels=tf.zeros_like(disc_fake)))
disc_loss = disc_loss_real + disc_loss_fake

# create the optimizer for the generator and discriminator models
gen_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope="generator")
disc_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope="discriminator")
gen_opt = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE, beta1=BETA1).minimize(gen_loss, var_list=gen_vars)
disc_opt = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE, beta1=BETA1).minimize(disc_loss, var_list=disc_vars)

# initialize the TensorFlow session and variables
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # train the model for the specified number of epochs
    for epoch in range(EPOCHS):
        # initialize the iterator for the image dataset
        sess.run(iterator.initializer)

        # generate noise for the current batch
        batch_noise = np.random.uniform(-1, 1, [BATCH_SIZE, NOISE_SIZE])

        # generate text for the current batch
        batch_text = np.random.choice(len(text_lines), size=[BATCH_SIZE])
        batch_text = np.eye(len(text_lines))[batch_text]

        # train the discriminator on the current batch
        for i in range(5):
            _, d_loss = sess.run([disc_opt, disc_loss], feed_dict={noise: batch_noise, text: batch_text})

        # train the generator on the current batch
        _, g_loss = sess.run([gen_opt, gen_loss], feed_dict={noise: batch_noise, text: batch_text})

        # print the current epoch and losses
        print("Epoch:", epoch, "Generator Loss:", g_loss, "Discriminator Loss:", d_loss)

        # save a generated image for visualization
        if epoch % 100 == 0:
            sample_noise = np.random.uniform(-1, 1, [1, NOISE_SIZE])
            sample_text = np.random.choice(len(text_lines), size=[1])
            sample_text = np.eye(len(text_lines))[sample_text]
            sample_image = sess.run(gen_images, feed_dict={noise: sample_noise, text: sample_text})
            sample_image = sample_image[0] * 255
            sample_image = sample_image.astype(np.uint8)
            sample_image = Image.fromarray(sample_image)
            sample_image.save("generated_image_epoch" + str(epoch) + ".jpg")
if name == "main":
train()
