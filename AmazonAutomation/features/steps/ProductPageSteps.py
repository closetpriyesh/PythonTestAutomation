from behave import then


@then(u'buy now button and add to cart button are displayed with appropriate texts')
def step_impl(context):
    assert context.product_page.get_add_to_card_button().is_displayed()
    assert context.product_page.get_buy_now_button().is_displayed()
    assert "buy now" in context.product_page.get_buy_now_button().find_element_by_xpath("parent::span/span").text.lower()
    assert "add to cart" in context.product_page.get_add_to_card_button().get_attribute('value').lower()