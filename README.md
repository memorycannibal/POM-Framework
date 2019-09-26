# POM Framework
Попытка в реализации фреймворка, с целью практики, для автотестов с использованием:
- Selenium WebDriver
- PyTest
- Requests lib

Что сделано:
- Выбор бразуера через --brower Доступны chrome и firefox. Без указания напрямую, тесты будут открыты в chrome
- PageObject Pattern структура - как её вижу я.
- Кастомыне маркеры для запуска только нужных тестов `pytest -m ui/api/smoke`
- Тестирование API с помощью Requests

Планы:
- логирование (easy)
- отчет по тестам (easy)
- улучшение структуры проекта