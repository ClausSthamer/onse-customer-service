from behave import when, then


@when(u'I update customer "{customer_id}" name to "{new_name}"')
def update_customer_name(context, customer_id, new_name):
    (first_name, surname) = new_name.split(' ', 2)
    response = context.web_client.put(
        '/customers/' + customer_id,
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 200, response.status_code


@then(u'I should fetch customer "{new_name}" with customer ID "{customer_id}"')
def step_impl(context, customer_id, new_name):
    response = context.web_client.get(f'/customers/{customer_id}')

    assert response.status_code == 200, response.status_code
    customer = response.get_json()
    return_name = f"{customer['firstName']} {customer['surname']}"
    assert return_name == new_name, f'{return_name} != {new_name}'
