inname= "basic1.1.log"
outname= "basic1.1.bin"
bin =b""
print( f"Reading {inname}")
with open(inname, 'r') as file:
  for line in file:
    if len(line)!=40 : continue
    hexs = line[6:29].split(" ")
    bin+= bytes([int(x, 16) for x in hexs])

print( f"converted {len(bin)} bytes")

print( f"Writing {outname}")
with open(outname, 'wb') as file:
  file.write(bin)
