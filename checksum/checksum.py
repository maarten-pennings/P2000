inname= "CPM Nater.bin"
print( f"Reading '{inname}'")
with open(inname, 'br') as file:
  content=file.read()
print( f"size  {len(content)} bytes")
sig= content[0]
print( f"sig   {sig:02X}")
count= content[1]+256*content[2]
print( f"count {count:04X}")
insum= content[3]+256*content[4]
print( f"insum {insum:04X}")
cname=""
for c in content[5:5+9]:
  cname+= chr(c) if 32<=c and c<=127 else "."
print( f"cname '{cname}'")

csum= insum
for c in content[5:5+count] :
  csum+= c
csum %= 65536
print( f"csum  {0x1005:04X}-{0x1005+count-1:04X} = {csum:04X} {'ok' if csum==0 else 'err'}")

