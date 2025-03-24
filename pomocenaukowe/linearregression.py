'''
Klasa LinearRegression zawiera metodę wyliczania współczynników regresji liniowej za pomocą metody najmniejszych kwadratów.
'''
class LinearRegression:
    def __init__(self):
        pass

    def fit(self, x, y):
        n = len(x)
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        xy_mean = sum([x[i] * y[i] for i in range(n)]) / n
        x2_mean = sum([x[i] ** 2 for i in range(n)]) / n
        self.a = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
        self.b = y_mean - self.a * x_mean
        return self.a, self.b

# Implementation of usage from user input
if __name__ == "__main__":
    x = []
    y = []
    print("Podaj pomiary, aby zakończyć wprowadzanie, wprowadź wartość niebędącą liczbą (zmiennoprzecinkową)")
    while True:
        try:
            x.append(float(input("Podaj x: ")))
            y.append(float(input("Podaj y: ")))
        except ValueError:
            break
    reg = LinearRegression()
    a, b = reg.fit(x, y)
    print("Współczynniki regresji liniowej: a =", a, "b =", b)