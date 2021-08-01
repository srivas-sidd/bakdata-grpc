import asyncio
import logging
import grpc
from grpc.aio import AioRpcError

import protofile.produceurl_pb2 as produceurl_pb2
import protofile.produceurl_pb2_grpc as produceurl_pb2_grpc
from src.services.GetNewsUrls import GetUrls
from delphai_utils.grpc_server import create_grpc_server, start_server

class UrlProducer(produceurl_pb2_grpc.ProduceUrlServicer):

    async def SendUrl(self, request:produceurl_pb2.UrlRequest, context: grpc.aio.ServicerContext) -> produceurl_pb2.UrlResponse:
        try:
            url = await GetUrls().get_urls()
            return produceurl_pb2.UrlResponse(url=url)

        except AioRpcError as ex:
            await context.abort(ex.code, ex.details())

        except Exception as ex:
            await context.abort(grpc.StatusCode.INTERNAL, str(ex))

if __name__ == '__main__':
    server = create_grpc_server(produceurl_pb2.DESCRIPTOR)
    produceurl_pb2_grpc.add_ProduceUrlServicer_to_server(UrlProducer(),server)
    start_server(server)