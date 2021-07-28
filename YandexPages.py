from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_NEWS_LIST = (By.CLASS_NAME, "news__list")


class SearchHelper(BasePage):

    def check_news_list(self):
        counter = 0
        list_news = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NEWS_LIST, time=2)
        for news in str.split(list_news[0].text, "\n"):
            if len(news) > 0:
                counter += 1
        if len(list_news[1].text) > 0:
            counter += 1
        return counter

    def find_text_news(self, text):
        list_news = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NEWS_LIST, time=2)
        if list_news[1].text == text:
            return True
        else:
            for news in str.split(list_news[0].text, "\n"):
                if news == text:
                    return True
        return False
