import logging
import asyncio
import grpc
import protofile.produceurl_pb2 as produceurl_pb2
import protofile.produceurl_pb2_grpc as produceurl_pb2_grpc

async def run() -> None:
    async with grpc.aio.insecure_channel('0.0.0.0:8080') as channel:
        try:
            stub = produceurl_pb2_grpc.ProduceUrlStub(channel)
            response = await stub.SendUrl(produceurl_pb2.UrlRequest(req='hey'))
            logging.info(response)

        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.CANCELLED:
                logging.info(f"Cancelled")
            elif rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                logging.info(f"Unavailable")
            else:
                logging.info(f"Received unknown RPC error: code={rpc_error.code()} message={rpc_error.details()}")


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())