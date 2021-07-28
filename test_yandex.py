from YandexPages import SearchHelper
import pytest


class TestsYandexMainPage:

    def test_yandex_search(self, open_brouser):
        yandex_main_page = SearchHelper(open_brouser)
        yandex_main_page.go_to_site()
        # elements = yandex_main_page.check_navigation_bar()
        count_news = yandex_main_page.check_news_list()
        assert count_news == 5

    @pytest.mark.parametrize("text", ["Зеленский выступил с обращением по случаю годовщины Крещения Руси",
                                      "Исинбаева поддержала захотевшего выгнать иностранного журналиста Медведева",
                                      "Песков назвал бравурными заявления Байдена о проблемах Путина",
                                      "Женская сборная России по баскетболу 3х3 вышла в финал Олимпиады"])
    def test_find_news_text(self, text, open_brouser):
        yandex_main_page = SearchHelper(open_brouser)
        yandex_main_page.go_to_site()
        assert yandex_main_page.find_text_news(text)