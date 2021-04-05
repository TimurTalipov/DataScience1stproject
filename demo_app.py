import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
from celluloid import Camera

# Based on this recipe:
# https://discuss.streamlit.io/t/matplotlib-animation-in-streamlit-through-html-js/5587
with st.echo(code_location='below'):
    st.title("Hello, World!")
    """
    This is a test.
    """
    x = np.linspace(0, 10, 500)
    fig = plt.figure()
    camera = Camera(fig)
    for i in range(10):
        plt.plot(x, np.sin(x + i))
        plt.ylim(-2, 2)
        camera.snap()
    animation = camera.animate()

    components.html(animation.to_jshtml(), height=1000)