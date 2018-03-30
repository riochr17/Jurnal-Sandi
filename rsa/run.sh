
echo "rio-mac:rsa rio.chandra.r$" 'python main.py "generate key"'
python main.py "generate key"


echo "-------TEST USING TEXT FILE-------"
echo "rio-mac:rsa rio.chandra.r$" 'cat hello.c'
cat hello.c

echo "rio-mac:rsa rio.chandra.r$" 'python main.py "rsa" encrypt "key" hello.c hello.c.encrypted'
python main.py "rsa" encrypt "key" hello.c hello.c.encrypted

echo "rio-mac:rsa rio.chandra.r$" 'python main.py "rsa" decrypt "key" hello.c.encrypted hello.c.decrypted'
python main.py "rsa" decrypt "key" hello.c.encrypted hello.c.decrypted

echo "rio-mac:rsa rio.chandra.r$" 'md5 hello.c'
md5 hello.c

echo "rio-mac:rsa rio.chandra.r$" 'md5 hello.c.encrypted'
md5 hello.c.encrypted

echo "rio-mac:rsa rio.chandra.r$" 'md5 hello.c.decrypted'
md5 hello.c.decrypted

echo "rio-mac:rsa rio.chandra.r$" 'cat hello.c.decrypted'
cat hello.c.decrypted

echo "-------TEST USING BINARY FILE-------"
echo "rio-mac:rsa rio.chandra.r$" 'gcc -o helloexe hello.c'
gcc -o helloexe hello.c

echo "rio-mac:rsa rio.chandra.r$" './helloexe'
./helloexe

echo "rio-mac:rsa rio.chandra.r$" 'python main.py "rsa" encrypt "key" helloexe helloexe.encrypted'
python main.py "rsa" encrypt "key" helloexe helloexe.encrypted

echo "rio-mac:rsa rio.chandra.r$" 'python main.py "rsa" decrypt "key" helloexe.encrypted helloexe.decrypted'
python main.py "rsa" decrypt "key" helloexe.encrypted helloexe.decrypted

echo "rio-mac:rsa rio.chandra.r$" 'md5 helloexe'
md5 helloexe

echo "rio-mac:rsa rio.chandra.r$" 'md5 helloexe.encrypted'
md5 helloexe.encrypted

echo "rio-mac:rsa rio.chandra.r$" 'md5 helloexe.decrypted'
md5 helloexe.decrypted

echo "rio-mac:rsa rio.chandra.r$" 'chmod +x helloexe.decrypted'
chmod +x helloexe.decrypted

echo "rio-mac:rsa rio.chandra.r$" './helloexe.decrypted'
./helloexe.decrypted