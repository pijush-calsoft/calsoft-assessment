MOD = 10**9 + 7

def mat_mult(A, B, mod=MOD):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]

def mat_pow(M, exp, mod=MOD):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while exp:
        if exp % 2:
            result = mat_mult(result, M, mod)
        M = mat_mult(M, M, mod)
        exp //= 2
    return result

def compute_complete_block(m, k, mod=MOD):
    if m == 1:
        f_km1 = k
        S_km1 = (k * (k + 1) // 2) % mod
        return (f_km1, S_km1)

    # Define transformation matrix and base vector
    M = [[k % mod, 0], [(k * (k + 1) // 2) % mod, 1]]
    V0 = [k % mod, (k * (k + 1) // 2) % mod]

    # Compute M^(m-1) * V0
    M_exp = mat_pow(M, m - 1, mod)
    f_km1 = (M_exp[0][0] * V0[0] + M_exp[0][1] * V0[1]) % mod
    S_km1 = (M_exp[1][0] * V0[0] + M_exp[1][1] * V0[1]) % mod

    return (f_km1, S_km1)

def compute_f_k(n, k, mod=MOD):
    
    if n < k:
        return (n + 1) % mod

    m, r = divmod(n, k)
    
    # Compute f_k(m) and S_k(m-1) efficiently
    f_m, S_m1 = compute_complete_block(m, k, mod)

    # Compute f_k(n) using the recurrence relation
    f_n = (k * S_m1 + (r + 1) * f_m) % mod

    return f_n

def compute():
    N = 10**14
    result = sum(compute_f_k(N, k) for k in range(2, 11)) % MOD
    return result

print(compute())
