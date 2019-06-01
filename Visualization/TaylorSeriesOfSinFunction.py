import matplotlib.pyplot as plt
import numpy as np

print("Formally we say that the Taylor series of a function is its representation as a power series. Let's see what this really means.")

print("\nConsider the cosine function from trigonometry. It has a nice smooth shape but if I asked you the cosine of some random number you'd probably have only a rough idea what the answer is. Traditionally it had to be worked out geometrically.")

print("\nWe can be more clever than that. There is one that we know for sure: cos(0) = 1. We will make an approximation starting with this requirement that approx(0) = 1.")

print("\nWhat should be used to make the approximation? Polynomials are very easy to evaluate and they can take lots of different shapes.")

print("\nSo lets start with the simplest polynomial... a horizontal line. There aren't many options here.")


print("\nObviously this isn't a very good quality approximation.")

print("\nTo make a better approximation we need to fit the curve of the cosine function. Fortunately that is a well known concept in calculus: the derivate.")

print("\nSo lets check the derivative of cos(0)... its zero. Our approximation also has a derivative of zero so we're matching!")

print("\n(Of course that means our approximation isn't any better.)")

print("\nBut the derivative doesn't tell the whole story. Lets check the second derivative of cos(0). That is -1!")

print("\nSo now we need to change our polynomial to give it a second derivative that is equal to -1. In order to have a second derivative it will have to be quadratic.")

print("\nSince polynomials are so well behaved this isn't a hard requirement to match. The power rule tells us that the second derivative of a quadratic polynomial is 2b, where b is the second coefficient. To make 2b = -1 we just have to say that b = -1/2.")

print("\nWe can continue in this way as long as desired. All of the odd terms will have a derivative of zero and so don't contribute. But each even term will make the approximation better.")


x = np.linspace(-5,5,100)
y = np.cos(x)

approx1 = [1]*len(x)
approx2 = [1-(i**2)/2 for i in x]
approx3 = [1-(i**2)/2+(i**4)/24 for i in x]
approx4 = [1-(i**2)/2+(i**4)/24-(i**6)/720 for i in x]

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_axis_off()

plt.ylim(-2,2)
plt.plot(x,y)
plt.plot(x,approx1)
plt.title("First Approximation: 1")

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_axis_off()

plt.ylim(-2,2)
plt.plot(x,y)
plt.plot(x,approx2)
plt.title("Second Approximation: 1 - (x^2)/2")

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_axis_off()

plt.ylim(-2,2)
plt.plot(x,y)
plt.plot(x,approx3)
plt.title("Third Approximation: 1-(x^2)/2 + (x^4)/24")

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_axis_off()

plt.ylim(-2,2)
plt.plot(x,y)
plt.plot(x,approx4)
plt.title("Fourth Approximation: 1-(x^2)/2 + (x^4)/24 - (x^6)/720")