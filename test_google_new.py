from selene import browser, be, have

def test_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_size_browser():
    browser.open('https://google.com')
    browser.element('[name="q"]').type(';lkkljsdfjlkj lfdjlshkjdfh fkjsghlkfjs').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('По запросу ;lkkljsdfjlkj lfdjlshkjdfh fkjsghlkfjs ничего не найдено')

test_google()
test_size_browser()