from protobuf.proto import user_pb2


def write_user_to_disk():
    user = user_pb2.User()
    user.id = 2
    user.name = 'Rocks526'
    user.email = "Rocks@126.com"
    with open('./protobuf/data/user.txt', 'wb') as f:
        f.write(user.SerializeToString())


def read_user_from_disk():
    # 注意要以二进制读取
    with open('./protobuf/data/user.txt', 'rb') as f:
        user_str = f.read()
        user = user_pb2.User()
        print(user)
        user.ParseFromString(user_str)
        print(user)


if __name__ == '__main__':
    # write_user_to_disk()
    read_user_from_disk()