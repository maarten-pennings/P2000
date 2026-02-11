# P2000 cartridge header analysis
import sys

if len(sys.argv) != 2 :
    print("ERROR: pass file.bin as argument")
    sys.exit()
inname= sys.argv[1]

print( f"open  {inname}")
with open(inname, 'br') as file:
  content=file.read()
print( f"size  {len(content)} bytes")
head=""
for i,c in enumerate(content[0:14]) :
  head+=f"{c:02X} "
  if i in [0,2,4] : head+="| "
print( f"head  {head}")
print()

sig= content[0]
print( f"sig   {sig:02X}")
count= content[1]+256*content[2]
print( f"count {count:04X} ({count} bytes)")
insum= content[3]+256*content[4]
print( f"insum {insum:04X}")
cname=""
for c in content[5:5+9]:
  cname+= chr(c) if 32<=c and c<=127 else "."
print( f"cname '{cname}'")
print()

csum= insum
for c in content[5:5+count] :
  csum+= c
csum16 = csum % 0x10000
print( f"csum  {0x1005:04X}-{0x1005+count-1:04X} = {csum16:04X} {'ok' if csum16==0 else 'err'}")
insumok= 0x10000 - ((csum-insum)%0x10000)
print( f"insum {insumok:04X} (makes csum ok)" )

