import allure
from httpx import Response

from clients.base_client import BaseClient, get_http_client
from config import Settings
from schema.operations import CreateOperationSchema, UpdateOperationSchema, OperationSchema
from tools.routes import APIRoutes


class OperationsClient(BaseClient):
    @allure.step("Get list of operations")
    def get_operations_api(self) -> Response:
        return self.get(APIRoutes.OPERATIONS)

    @allure.step("Get operation by id {operation_id}")
    def get_operation_api(self, operation_id: int) -> Response:
        return self.get(f"{APIRoutes.OPERATIONS}/{operation_id}")

    @allure.step("Create operation")
    def create_operation_api(self, operation: CreateOperationSchema) -> Response:
        return self.post(
            APIRoutes.OPERATIONS,
            json=operation.model_dump(mode='json', by_alias=True)
        )

    @allure.step("Update operation by id {operation_id}")
    def update_operation_api(
            self,
            operation_id: int,
            operation: UpdateOperationSchema
    ) -> Response:
        return self.patch(
            f"{APIRoutes.OPERATIONS}/{operation_id}",
            json=operation.model_dump(mode='json', by_alias=True, exclude_none=True)
        )

    @allure.step("Delete operation by id {operation_id}")
    def delete_operation_api(self, operation_id: int) -> Response:
        return self.delete(f"{APIRoutes.OPERATIONS}/{operation_id}")

    def create_operation(self) -> OperationSchema:
        request = CreateOperationSchema()
        response = self.create_operation_api(request)
        return OperationSchema.model_validate_json(response.text)


def get_operations_client(settings: Settings) -> OperationsClient:
    return OperationsClient(client=get_http_client(settings.fake_bank_http_client))
