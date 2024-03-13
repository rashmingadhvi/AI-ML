import numpy as np
def gradientDescent(area, price):

    weight: float = 0.0  # M
    bias: float = 0.0  # B
    cost: float  # Cost  - Gradient Descent
    iterations: int = 100000
    stepSize: float = 0.0001
    totalDataPoints = len(area)
    costCutOff: float = 0.1

    for i in range(iterations):
        pricePredicted = weight * area + bias
        delta = price - pricePredicted
        weightDerative = -(2 / totalDataPoints) * sum(area * delta)
        biasDerative = -(2 / totalDataPoints) * sum(delta)
        weight -= (weightDerative * stepSize)
        bias -= (biasDerative * stepSize)
        cost = (1 / totalDataPoints) * sum(d ** 2 for d in delta)
        print("Iteration: " + str(i) + ", Cost: " + str(cost) + ", Weight: " + str(weight) + ", Bias: " + str(bias))
        if cost < costCutOff:
            print("Cost reached the cutoff")
            break

    return [weight, bias]


area = np.array([1, 2, 3, 4, 5])
price = np.array([5, 7, 9, 11, 14])

print("The M (Weight) and B(Bias) are : " + str(gradientDescent(area, price)))
