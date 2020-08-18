from django.test import TestCase, Client
import datetime as dt


# Create your tests here.

# Задание

# Напишите тесты для проверки страницы сайта с тарифными планами.

# Проверьте, что:
# - главная страница доступна неавторизованному пользователю, а раздел администратора — нет
# - переменная plans есть в контексте шаблона
# - имя шаблона, который вызывается при рендеринге главной страницы — index.html
# - тип переменной plans — это список, состоящий из 3-х элементов, а их тип — словарь
# - на результирующей странице показываются названия тарифных планов и подставляется правильная тема (subject) в ссылку на кнопке "Связаться"
# - в контекстных переменных шаблона присутствует текущий год и он же правильно появляется на странице


class PlansPageTest(TestCase):
    def setUp(self):
        pass

    def testPageCodes(self):
        pass

    def testIndexContext(self):
        pass

    def testIndexTemplate(self):
        pass

    def testIndexPlans(self):
        pass

    def testIndexContent(self):
        # Проверяйте вхождение строки f"mailto:order@company.site?subject={plan['name']}"
        pass

    def testContextProcessor(self):
        # today = dt.datetime.today().year
        pass
