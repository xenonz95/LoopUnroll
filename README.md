# LoopUnroll

基于宏编程的循环展开实现，可用于HLS开发

目前仅实现一维循环展开

包含分号（用于执行）与逗号（用于参数列表或初始化列表）分隔的两种循环

使用clang可编译运行

## Generator Usage

```bash
python3 generator.py > MACRO_LOOP.h
```

## Header Usage

Watch example.cpp
