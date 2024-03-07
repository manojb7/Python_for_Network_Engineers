#validate ip address in correct range
#first octet > 0 and < 223 and not equal to 127 and not equal to 169.254
#second, third, fourth octet > 0 and < 255


# def validate_ip_address(ip):
#     ip = ip.split('.')
#     if len(ip) != 4:
#         return False
#     if ip[0] == '127' and ( ip[0] == '169' or ip[1] == '254'):
#         return "Invalid"
#     elif 0 < int(ip[0]) < 223 and 0 < int(ip[1]) < 255 and 0 < int(ip[2]) < 255 and 0 < int(ip[3]) < 255:
#         return "Valid"
#     else:
#         return "Invalid"

# print(validate_ip_address('10.254.0.254'))

def validate_ip_address(ip):
    ip_parts = ip.split('.')
    if len(ip_parts) != 4:
        return False
    
    # Convert octets to integers for comparison
    try:
        ip_parts = [int(part) for part in ip_parts]
    except ValueError:
        # If conversion fails, the IP address is invalid
        return "Invalid"
    
    # Check the first octet
    if not (0 < ip_parts[0] < 223) or ip_parts[0] == 127:
        return "Invalid"
    
    # Check for the 169.254.x.x range
    if ip_parts[0] == 169 and ip_parts[1] == 254:
        return "Invalid"
    
    # Check the remaining octets
    if any(octet < 0 or octet > 254 for octet in ip_parts[1:]):
        return "Invalid"
    
    return "Valid"

# Correct test
print(validate_ip_address('192.168.1.1'))
