import re
count_of_barcodes = int(input())
pattern = r"@#{1,}[A-Z][a-zA-Z0-9]{4,}[A-Z]@#{1,}"
for _ in range(1, count_of_barcodes+1):
    barcode = input()
    is_valid = re.findall(pattern, barcode)
    if is_valid:
        product_group = ""
        for ch in barcode:
            if ch.isdigit():
                product_group += ch
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
