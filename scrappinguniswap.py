import commune as c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class UniswapBot(c.Module):
    def __init__(self, a=1, b=2):
        self.set_config(kwargs=locals())

    def call(self, x: int = 1, y: int = 2) -> int:
        c.print(self.config)
        c.print("This is the config, it is a Munch object")
        return x + y

    def install(self):
        return c.cmd("pip3 install selenium")

    def train_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        c.print("Mean Squared Error:", mse)
        return model

    def test(self):
        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome()
        # Go to the Uniswap website
        driver.get("https://info.uniswap.org/")
        # Find the volume column header to sort by volume
        volume_header = driver.find_element_by_xpath("//th[contains(text(),'Volume')]")
        volume_header.click()
        # Find all the table rows for pairs with volume over 1 million
        pairs_rows = driver.find_elements_by_xpath(
            "//tr[contains(@class, 'MuiTableRow-root')][td[5]>1000000]"
        )

        # Extract features and target variable for training
        features = []
        target = []

        # Iterate over the pairs and collect data
        for pair_row in pairs_rows:
            # Assuming you have more features and a target variable to predict
            feature1 = float(pair_row.find_element_by_xpath("./td[2]").text)
            feature2 = float(pair_row.find_element_by_xpath("./td[3]").text)
            # Add more features as needed
            target_variable = float(pair_row.find_element_by_xpath("./td[6]").text)

            features.append([feature1, feature2])  # Add more features as needed
            target.append(target_variable)

        # Train the model
        model = self.train_model(features, target)

        # Close the browser
        driver.quit()

        # Now you can use the trained model to make predictions on new data or for other purposes
        # Example: model.predict(new_data)


# Example usage
bot = UniswapBot()
bot.test()
