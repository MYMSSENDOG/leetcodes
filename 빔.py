input_line = input().split()

H = int(input_line[0])#높이
W = int(input_line[1])#넓이
mirror = [""  for i in range(H)]

for i in range(H):
    mirror[i] = input()
dir = [0,1]
y = 0
x = 0
ret = 0
while x>=0 and x< W and y >=0 and y <H:

    if mirror[y][x] == "-":
        pass
    else:
        if mirror[y][x] == "/":
            dir = [-dir[1],-dir[0]]
        elif mirror[y][x] == "\\":
            dir = [dir[1],dir[0]]
    ret += 1
    y += dir[0]
    x += dir[1]
print(ret)


"""
늦게 알림이 발송되어야 하는 경우에는 큐 구조를 이용해 메세지를 저장한다. 
추가적으로 DB를 두어서 유저의 요청을 저장한다.  유저 요청이 있는경우, 큐와 DB 전체를 검사한 후 요청을 수락할 지 거부할 지 판단한다. 큐가 꽉 찬 이후에 오는 요청은 DB에 별도로 저장된다. 
만일 큐의 용량이 가득 찬다면, DB에 응답하지 못한 요청으로 저장한다. 처음부터 이렇게 하지 않는 이유는 메모리에 남겨두는것이 처리하는게 훨씬 빠르기 때문이다. 
"""
"""
로컬dns에 url이 있는지 udp로  질의한다. 있다면 ip주소를 획득하고 없다면 루트 dns로 질의한다.
https 이므로 브라우저와 서버는 ssl handshake과정을 통해 연결한다. 연결 후 패킷으로 페이지를 요청하는 패킷을 암호화해 서버에 요청하면, 서버는 패킷을 해독 한 뒤, 다시 암호화한 웹페이지 소스를 브라우저로 보낸다.
브라우저는 이것을 복호화해 창에 띄운다."""