# enctools
A program that helps you encrypt / decrypt files with:
- Shifting bits
- SHA-256 checksum
- SHA-512 checksum
- Flip bits
- Reverse bytes
- Reverse bits
- Overwrite with nulls
# Usage
Shifting: `enctools -shift <number_of_shifts> <input_file> <output_file>` or `enctools -shift <number_of_shifts> <input_file>`. If you want to encrypt by shift `x` times, you need to decrypt by shifting `-x` times.  
SHA-256 checksum: `enctools -sha256 <input_file> <output_file>`  
SHA-512 checksum: `enctools -sha512 <input_file> <output_file>`  
Flip bits: `enctools -flipbit <input_file> <output_file>`. If you want to decrypt, just "encrypt" it one more time.  
Reverse bits: `enctools -revbit <input_file> <output_file>`. If you want to decrypt, just "encrypt" it one more time.  
Reverse bytes: `enctools -revbyte <input_file> <output_file>`. If you want to decrypt, just "encrypt" it one more time.  
Nullify: `enctools -null <input_file>`.  
Help: `enctools -h`.  
# Examples
Shifting:  
`D:\Code\dist>more a.bat`  
`echo hello`  
`D:\Code\dist>enctools -shift 1 a.bat b.bat`  
`D:\Code\dist>more b.bat`  
`┬▓┬▒┬┤7┬É42┬╢67`  
`D:\Code\dist>enctools -shift -1 b.bat c.bat`   
`D:\Code\dist>more c.bat`  
`echo hello`  
SHA-256 Checksum:  
`D:\Code\dist>enctools -sha256 a.bat b.bat`  
`SHA256 Checksum: 584a331fd6b02dcb1ecbe2eba731f609a2e1e3dac0bb73ae998dfad14c309a77`  
SHA-512 Checksum:  
`D:\Code\dist>enctools -sha512 a.bat b.bat`  
`SHA512 Checksum: 92ffc373afc6ef7f7f128e9c8058457998c908e7ae5812d38760748cf16dd883a33226b91b0059b1910058518d1aab73f4a0b75dd4c33130ce0856f5f4f8a9a7`  
Reverse Bytes:  
`D:\Code\dist>enctools -revbyte a.bat b.bat`  
`D:\Code\dist>more b.bat`  
`olleh ohce`  
`D:\Code\dist>enctools -revbyte b.bat c.bat`  
`D:\Code\dist>more c.bat`  
`echo hello`  
Reverse Bits:  
`D:\Code\dist>enctools -revbit a.bat b.bat`  
`D:\Code\dist>more b.bat`  
`├╢66┬ª▬♦├╢▬├å┬ª`  
`D:\Code\dist>enctools -revbit b.bat c.bat`  
`D:\Code\dist>more c.bat`  
`echo hello`  
Flip Bits:  
`D:\Code\dist>enctools -flipbit a.bat b.bat`  
`D:\Code\dist>more b.bat`  
`┬Ü┬£┬ù┬É├ƒ┬ù┬Ü┬ô┬ô┬É`  
`enctools -flipbit b.bat c.bat`  
`D:\Code\dist>more c.bat`  
`echo hello`  
Nullify:  
`D:\Code\dist>enctools -null a.bat b.bat`  
`D:\Code\dist>more b.bat`  
``  
``  
``  
``  
``  
``  
``  
``  
``  
``  
`D:\Code\dist>enctools -null a.bat`  
`D:\Code\dist>more a.bat`  
``  
``  
``  
``  
``  
``  
``  
``  
``  
``
# Notes
When the output file is not provided, the output file is the input file.  
The program is in testing, so there are a few exceptions that the program didn't catch.
The program may won't work in some binary files (.exe, ...)
# Special
Thanks ChatGPT for corprating with me to make this program.
