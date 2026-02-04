# Get the value of the final/last bit in a subnet mask
# This is useful for determining the total number of hosts per network based on a netmask.
def get_final_mask_bit(n):
    if n < 1:
        return n
    x=n
    ctr = 1
    while x > 0:
      if x & 1:
          break
      x = x >> 1
      ctr = ctr << 1
    return ctr

print(get_final_mask_bit(65408))
