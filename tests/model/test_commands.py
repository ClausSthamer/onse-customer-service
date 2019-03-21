from unittest.mock import Mock

import pytest

from customer_service.model import commands
from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_get_customer_when_customer_does_not_exist(customer_repository):
    with pytest.raises(CustomerNotFound):
        commands.get_customer(customer_id=99999,
                              customer_repository=customer_repository)


def test_get_customer(customer_repository):
    customer = Customer(customer_id=1234, first_name='Gene', surname='Kim')
    customer_repository.store(customer)

    result = commands.get_customer(customer_id=1234,
                                   customer_repository=customer_repository)

    assert result is customer


def test_create_customer(customer_repository):
    customer = Customer(first_name='Nicole', surname='Forsgren')

    commands.create_customer(customer=customer,
                             customer_repository=customer_repository)

    stored_customer = customer_repository.fetch_by_id(customer.customer_id)

    assert stored_customer.first_name == 'Nicole'
    assert stored_customer.surname == 'Forsgren'


def test_update_customer(customer_repository):

    # Given customer exists
    existing_customer = Customer(first_name='Nicole',
                        surname='Foresgren')

    customer_repository.store(existing_customer)
    
    # When customer updated
    commands.update_customer(first_name='Bob',
                             surname='Todd',
                             customer_id=existing_customer.customer_id,
                             customer_repository=customer_repository)

    # Then
    updated_customer = customer_repository.fetch_by_id(existing_customer.customer_id)
    assert updated_customer.first_name == 'Bob'
    assert updated_customer.surname == 'Todd'
    assert updated_customer.customer_id == existing_customer.customer_id
