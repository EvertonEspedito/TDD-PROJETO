from uuid import UUID

import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_success():
    product = ProductIn.model_validate(product_data())

    assert product.name == "Iphone 14 Pro Max"
    assert isinstance(product.id, UUID )

def test_schemas_return_raise():
    # price como string inválida ao invés de float
    data = {
        'name': 'Iphone 14 Pro Max',
        'quantity': 10,
        'price': 'oito mil e quinhentos',
        
    }

    with pytest.raises(ValueError) as err:
        ProductIn(**data)

    # Valida se o erro retornado é do campo 'price'
    errors = err.value.errors()
    assert errors[0]['loc'] == ('price',)
    assert errors[0]['msg']