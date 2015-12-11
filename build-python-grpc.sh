rm -rf python
mkdir python
protoc -I ../ \
       -I /home/gulfstream/git/gogo-protobuf/ \
       -I /home/gulfstream/git/grpc/third_party/protobuf/src/ \
       --python_out=./python/ \
       --grpc_out=./python/ \
       --plugin=protoc-gen-grpc=/home/gulfstream/git/grpc/bins/opt/grpc_python_plugin  \
       ../etcd/storage/storagepb/kv.proto \
       ../etcd/etcdserver/etcdserverpb/rpc.proto \
       /home/gulfstream/git/gogo-protobuf/gogoproto/*.proto
find python -type d -exec touch {}/__init__.py \;
cd python
python ./etcd/etcdserver/etcdserverpb/rpc_pb2.py
