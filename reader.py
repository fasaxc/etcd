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
  watch_stub = rpc_pb2.beta_create_watch_stub(channel)
  response = watch_stub.Watch(generate_watch_reqs(), 1000)

  print "Waiting for responses"
  num = 0
  last_log = time.time()
  while True:
      for v in response:
          num += 1
          if num % 1000 == 0:
              now = time.time()
              print "Read", num, now-last_log
              last_log = now
#  print response.next()


def generate_watch_reqs():
    yield rpc_pb2.WatchRequest(prefix="/")
    print "Asked for /"

    time.sleep(100000)


if __name__ == '__main__':
    try:
        run()
    except BaseException as e:
        traceback.print_exc()
        os._exit(1)
