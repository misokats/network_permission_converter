# 1. パスの操作test_WSL
path = "/usr/local/bin/python3"

parts = path.split("/")
result_path = "-".join(parts[1:4])

print(f"課題１：{result_path}")

# 2. パーミッションの0埋め
perm_num = 7
# ここにコードを書く
binary_perm = bin(perm_num)[2:].zfill(3)

print(f"課題２: {binary_perm}")

# 3. リスト内包表記
ports = [80, 443, 22, 8080]
# ここにコードを書く
str_ports = [str(p) for p in parts]

print(f"課題３: {str_ports}")

# --- ボーナス：逆引きサブネット計算 ---
def netmask_to_cidr(mask_str):
    # ここにロジックを書く
    octets = mask_str.split(".")
    binary_octets = [bin(int(o))[2:].zfill(8) for o in octets]
    cidr = "".join(binary_octets)
    return cidr.count('1')
    pass

print(f"255.255.0.0 は CIDRで: {netmask_to_cidr('255.255.0.0')}")ss