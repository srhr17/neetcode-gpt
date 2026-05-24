class Solution:
    def der(self, x):
        return 2 * x
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0 :
            return round(init,5)
        else:
            
            new_init = init - (learning_rate*self.der(init))
            return self.get_minimizer(iterations-1,learning_rate,new_init)
