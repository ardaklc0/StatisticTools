from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from scipy import stats
import numpy as np

# Path to your WebDriver
driver_path = "chromedriver.exe"

# Initialize the WebDriver
driver = webdriver.Chrome()


def open_browser():
    try:
        print("Opening browser...")
        driver.get("https://www.binance.com/en/futures/DOGEUSDT")
        driver.maximize_window()
        time.sleep(5)
        print("Browser opened successfully!")
    except Exception as error:
        print(f"An error occurred: {error}")


def login_to_binance(email, password):
    try:
        login_button = driver.find_element(By.LINK_TEXT, "Log In")
        login_button.click()

        time.sleep(5)

        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys(email)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(10)

        print("Logged in successfully!")

    except Exception as error:
        print(f"An error occurred: {error}")


def accept_cookies():
    try:
        print("Accepting cookies...")
        cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_button.click()
        print("Cookies accepted!")
    except Exception as error:
        print(f"An error occurred: {error}")


def get_last_price(minutes):
    now = time.time()
    future = now + (minutes * 60)
    prices = []
    last_html_content = None  # To track the previous HTML content of the price

    try:
        print("Getting last prices...")
        while time.time() < future:
            # Locate the price element
            price_class = driver.find_element(By.CLASS_NAME, "contractPrice")
            price_element = price_class.find_element(By.TAG_NAME, "div")

            # Extract the text and other content
            current_html_content = price_element.get_attribute("outerHTML")
            current_price = price_element.text

            try:
                # Convert price to float
                current_price = float(current_price)

                # Only append if the element content changes
                if current_html_content != last_html_content:
                    prices.append(current_price)
                    last_html_content = current_html_content
                    print(f"Price updated: {current_price}")

            except ValueError:
                print(f"Invalid price data: {current_price}")
        return prices
    except Exception as error:
        print(f"An error occurred: {error}")
        return []


def calculate_mean(prices):
    """The average of the dataset, calculated by summing all values and dividing by the count."""
    try:
        print("Calculating average price...")
        average = np.mean(prices)
        print(f"Average price: {average}")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_standard_deviation(prices):
    """The measure of the amount of variation or dispersion of a set of values.
    A low standard deviation indicates that the values tend to be close to the mean,
    while a high standard deviation indicates that the values are spread out over a wider range."""
    try:
        print("Calculating standard deviation...")
        standard_deviation = np.std(prices, ddof=1)
        print(f"Standard deviation: {standard_deviation}")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_mode(prices):
    """The value that appears most frequently in a data set.
     A set of data may have one mode, more than one mode, or no mode at all."""
    try:
        print("Calculating mode price...")
        mode_result = stats.mode(prices, keepdims=True)
        print(f"Mode price: {mode_result.mode[0]} (Count: {mode_result.count[0]})")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_median(prices):
    """The middle value of a dataset, separating the higher half from the lower half."""
    try:
        print("Calculating median price...")
        median = np.median(prices)
        print(f"Median price: {median}")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_variance(prices):
    """The average of the squared differences from the Mean.
    It measures the dispersion of a set of data points around the Mean.
    Higher variance indicates higher dispersion. High dispersion can be due to outliers.
    Lower variance indicates lower dispersion. Lower dispersion can be due to a more consistent dataset."""
    try:
        print("Calculating variance...")
        variance = np.var(prices, ddof=1)
        print(f"Variance: {variance}")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_skewness(prices):
    """A measure of the asymmetry of the probability distribution of a real-valued random variable about its mean.
    Negative skewness indicates a left-skewed distribution, while positive skewness indicates a right-skewed
    distribution. Left-skewed distributions have a longer left tail, while right-skewed distributions have a longer
    right tail. Longer tails indicate more extreme values. Smaller tails indicate more consistent values.  A skewness
    of zero indicates a symmetrical distribution"""
    try:
        print("Calculating skewness...")
        skewness = stats.skew(prices)
        print(f"Skewness: {skewness}")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_kurtosis(prices):
    """A measure of the "tailedness" of the probability distribution of a real-valued random variable. It describes
    the shape of the distribution. High kurtosis indicates a sharp peak and fat tails, while low kurtosis indicates a
    flat peak and thin tails. A kurtosis of zero indicates a normal distribution."""
    try:
        print("Calculating kurtosis...")
        kurtosis = stats.kurtosis(prices)
        print(f"Kurtosis: {kurtosis}")
    except Exception as error:
        print(f"An error occurred: {error}")


def calculate_range(prices):
    """The difference between the highest and lowest values in a dataset."""
    try:
        print("Calculating range...")
        range_of_prices = np.ptp(prices)
        print(f"Range: {range_of_prices}")
    except Exception as error:
        print(f"An error occurred: {error}")


def close_browser():
    try:
        print("Closing browser...")
        driver.quit()
        print("Browser closed successfully!")
    except Exception as error:
        print(f"An error occurred: {error}")
