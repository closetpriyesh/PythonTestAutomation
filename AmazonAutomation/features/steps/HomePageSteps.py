from behave import given, when

AMAZON_HOME = "https://amazon.in"


@given(u'user is on home page')
def user_is_on_home_page(context):
    context.driver.get(AMAZON_HOME)


@when(u'user enters "{word}"')
def step_impl(context, word):
    context.home_page.get_search_box().send_keys(word)
    context.home_page.get_search_icon().click()

