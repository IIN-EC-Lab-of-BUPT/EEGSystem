import asyncio
from injector import inject
from componentframework.api.ConnectManagerInterface import ConnectManagerInterface
from componentframework.api.Enum.StatusEnum import StatusEnum
from componentframework.service.ConnectManagerService import ConnectManagerService
from componentframework.service.serviceInterface.ServiceOperatorInterface import \
    AddListenerOnRequestComponentStopCallbackServiceInterface


class ConnectManagerInterfaceImpl(ConnectManagerInterface):
    @inject
    def __init__(self, connect_manager_forwarder: ConnectManagerService):
        # 初始化操作，可以在这里进行一些初始化设置
        self.shutdown_result = None
        self.__connect_manager_forwarder = connect_manager_forwarder

    async def shutdown(self):
        """关闭连接"""
        # 返回值："关闭连接成功通知"：str类型
        # self.shutdown_result = asyncio.create_task(self.__connect_manager_forwarder.shutdown())
        self.shutdown_result = await self.__connect_manager_forwarder.shutdown()
        return self.shutdown_result

    async def add_listener_on_request_component_stop(self, callback) -> None:
        """
        2.6.7 监听请求组件停止
        """

        # 监听请求组件停止
        # callback包含输入参数
        # request : str
        # callback 无需返回
        class AddListenerOnRequestComponentStopCallbackOperator \
                    (AddListenerOnRequestComponentStopCallbackServiceInterface):
            def __init__(self):
                super().__init__()
                self.__operator = callback

            async def run(self, result):
                await self.__operator.run(result)

        operator = AddListenerOnRequestComponentStopCallbackOperator()
        asyncio.create_task(self.__connect_manager_forwarder.add_listener_on_request_component_stop(operator))

    async def cancel_add_listener_on_request_component_stop(self) -> StatusEnum:
        cancel_add_listener_on_request_component_stop_result = \
            await self.__connect_manager_forwarder.cancel_add_listener_on_request_component_stop()
        return cancel_add_listener_on_request_component_stop_result

    async def startup(self, component_startup_configuration):
        await self.__connect_manager_forwarder.startup(component_startup_configuration)
