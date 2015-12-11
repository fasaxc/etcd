from grpc.beta import implementations
import traceback
import etcd.etcdserver.etcdserverpb.rpc_pb2 as rpc_pb2
import os
import time
from threading import Thread
_TIMEOUT_SECONDS = 10

print
print

def run():
  channel = implementations.insecure_channel('localhost', 2378)
  stub = rpc_pb2.beta_create_KV_stub(channel)
  num = 0
  last_log = time.time()
  while True:
    response = stub.Put(rpc_pb2.PutRequest(key="/foobarbaxbiffbop%s" % (num % 1000), value="%s" % time.time()), 1000)
    num += 1
    if num % 1000 == 0:
      now = time.time()
      print "Sent", num, now - last_log
      last_log = now 


if __name__ == '__main__':
    try:
        run()
    except BaseException as e:
        traceback.print_exc()
        os._exit(1)
