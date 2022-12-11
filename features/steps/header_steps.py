from behave import when, then
from pages.home import home_page


@when('I try click {click_icon}')
def click_icon_or_button(context, click_icon):
    home_page.click_icon_or_button(click_icon)


@when('I write {text} in the search field')
def search_field(context, text):
    home_page.search_field(text)


@when('Delete departure place information for light')
def delete_current_departure(context):
    home_page.if_departure_place_delete_it()


@when('Enter your conditions {from_where} {to_where}')
def find_flight_departure_arrival_place(context, from_where, to_where):
    home_page.find_flight_departure_arrival_place(from_where, to_where)


@when('Select dates {go_flight_date} {return_flight_data}')
def find_flight_departure_arrival_date(context, go_flight_date, return_flight_data):
    home_page.find_flight_departure_arrival_date(go_flight_date,
                                                 "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]"
                                                 "/div/div/div/form/div/div[2]/div[1]/ul/li[2]/div[1]/div/div")
    home_page.find_flight_departure_arrival_date(return_flight_data,
                                                 "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]"
                                                 "/div/div/div/form/div/div[2]/div[1]/ul/li[2]/div[2]/div/div")


@then('I see this component {component}')
def verify_component(context, component):
    if home_page.verify_opened_successfully_and_component_present(component):
        return True
    else:
        return False


@then('I compare search text {text} with result {component}')
def verify_component_text(context, text, component):
    assert (home_page.verify_component_text(text, component) is True)


@then('I close the window')
def close_the_driver(context):
    home_page.close_window()
