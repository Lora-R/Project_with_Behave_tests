from behave import given, when, then
from framework.initialize_driver_website import web_page


@given("I load the website")
def step_load_website(context):
    web_page.load_website()


@when("I go to page")
def step_go_to_page(context):
    web_page.go_to_page("https://us.trip.com/")


@then("I see this element on the page {element}")
def step_verify_component(context, element):
    context.assertTrue(web_page.verify_component_exists(element))


@then("I quit driver")
def step_close_browser(context):
    web_page.quit_driver()
