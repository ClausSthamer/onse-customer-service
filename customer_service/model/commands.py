def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(customer, customer_repository):
    customer_repository.store(customer)

def update_customer(first_name, surname, customer_id, customer_repository):
    customer_to_update = customer_repository.fetch_by_id(customer_id)
    customer_to_update.first_name = first_name
    customer_to_update.surname = surname
    customer_repository.store(customer_to_update)
    #
    # updated_customer = customer_repository.fetch_by_id(new_customer_values.customer_id)
    #
    # return updated_customer
