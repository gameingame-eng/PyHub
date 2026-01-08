`git clone https://github.com/emscripten-core/emsdk.git C:\emsdk`
run that to be able to build
make sure you are in pong dir
then run `emcc pong.cpp -s USE_SDL=2 -O2 -o index.html`\
this is for me only if ur collabing please dont change this dir
once done, pong dir should look like
```Directory
pong.cpp
index.html
pong.js
pong.wasm
launcher_pong.py
README.md
```