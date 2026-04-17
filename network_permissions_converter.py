# -----------------------------------------
# 1. 文字列の分解と結合
# -----------------------------------------
path = "/usr/local/bin/python3"
# split("/") をすると ['', 'usr', 'local', 'bin', 'python3'] と空文字が入るのでスライスで調整
parts = path.split("/")
result_path = "-".join(parts[1:4]) 

print(f"課題1 (Path): {result_path}") # 出力: usr-local-bin


# -----------------------------------------
# 2. 基数変換と0埋め（パーミッション編）
# -----------------------------------------
perm_num = 7
# 2進数にしてから先頭の'0b'を除き、3桁(zfill(3))で揃える
binary_perm = bin(perm_num)[2:].zfill(3)

print(f"課題2 (Perm): {binary_perm}") # 出力: 111


# -----------------------------------------
# 3. リスト内包表記の実践
# -----------------------------------------
ports = [80, 443, 22, 8080]
# すべての要素にstr()関数を適用して新しいリストを作る
str_ports = [str(p) for p in ports]

print(f"課題3 (Ports): {str_ports}") # 出力: ['80', '443', '22', '8080']


# -----------------------------------------
# ボーナス：逆引きサブネット計算 (Mask to CIDR)
# -----------------------------------------
def netmask_to_cidr(mask_str):
    # 1. ドットで分割
    octets = mask_str.split(".")
    
    # 2. 内包表記を使って、各オクテットを8桁の2進数文字列に変換
    # 手順：数値化(int) -> 2進数化(bin) -> 0b除去([2:]) -> 8桁埋め(zfill(8))
    binary_list = [bin(int(o))[2:].zfill(8) for o in octets]
    
    # 3. すべてを1つの長い文字列に合体させる
    full_binary = "".join(binary_list)
    
    # 4. '1' の数をカウントして返す
    return full_binary.count('1')

print(f"ボーナス (255.255.0.0): /{netmask_to_cidr('255.255.0.0')}") # 出力: /16# -----------------------------------------
# 1. 文字列の分解と結合
# -----------------------------------------
path = "/usr/local/bin/python3"
# split("/") をすると ['', 'usr', 'local', 'bin', 'python3'] と空文字が入るのでスライスで調整
parts = path.split("/")
result_path = "-".join(parts[1:4]) 

print(f"課題1 (Path): {result_path}") # 出力: usr-local-bin


# -----------------------------------------
# 2. 基数変換と0埋め（パーミッション編）
# -----------------------------------------
perm_num = 7
# 2進数にしてから先頭の'0b'を除き、3桁(zfill(3))で揃える
binary_perm = bin(perm_num)[2:].zfill(3)

print(f"課題2 (Perm): {binary_perm}") # 出力: 111


# -----------------------------------------
# 3. リスト内包表記の実践
# -----------------------------------------
ports = [80, 443, 22, 8080]
# すべての要素にstr()関数を適用して新しいリストを作る
str_ports = [str(p) for p in ports]

print(f"課題3 (Ports): {str_ports}") # 出力: ['80', '443', '22', '8080']


# -----------------------------------------
# ボーナス：逆引きサブネット計算 (Mask to CIDR)
# -----------------------------------------
def netmask_to_cidr(mask_str):
    # 1. ドットで分割
    octets = mask_str.split(".")
    
    # 2. 内包表記を使って、各オクテットを8桁の2進数文字列に変換
    # 手順：数値化(int) -> 2進数化(bin) -> 0b除去([2:]) -> 8桁埋め(zfill(8))
    binary_list = [bin(int(o))[2:].zfill(8) for o in octets]
    
    # 3. すべてを1つの長い文字列に合体させる
    full_binary = "".join(binary_list)
    
    # 4. '1' の数をカウントして返す
    return full_binary.count('1')

print(f"ボーナス (255.255.0.0): /{netmask_to_cidr('255.255.0.0')}") # 出力: /16