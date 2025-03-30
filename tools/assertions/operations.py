import allure

from schema.operations import CreateOperationSchema, OperationSchema, UpdateOperationSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("OPERATIONS_ASSERTIONS")


@allure.step("Check create operation")
def assert_create_operation(
        actual: OperationSchema,
        expected: CreateOperationSchema | UpdateOperationSchema
):
    logger.info("Check create operation")

    assert_equal(actual.debit, expected.debit, "debit")
    assert_equal(actual.credit, expected.credit, "credit")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.transaction_date, expected.transaction_date, "transaction_date")


@allure.step("Check operation")
def assert_operation(actual: OperationSchema, expected: OperationSchema):
    logger.info("Check operation")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.debit, expected.debit, "debit")
    assert_equal(actual.credit, expected.credit, "credit")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.transaction_date, expected.transaction_date, "transaction_date")
