import time

from behave import given, when, then


@then(u'he navigates to page whose title contains "{word}"')
def navigate_to_search_page(context, word):
    time.sleep(2)
    assert word in context.driver.title


@then(u'the searched text "{word}" is displayed in a different color')
def searched_text_displayed_in_different_color(context, word):
    assert word in context.search_page.get_first_item_text_element().text.lower()


@then(u'the first item name contains "{word}"')
def first_item_name_contains_word(context, word):
    assert word in context.search_page.get_searched_text().text


@then(u'selects the first item')
def user_selects_the_first_item(context):
    context.search_page.get_first_item_price_element().click()


@then(u'user goes to child window')
def user_goes_to_child_window(context):
    context.main_window = context.driver.window_handles[0]
    context.child_window = context.driver.window_handles[1]
    context.driver.switch_to.window(context.child_window)




