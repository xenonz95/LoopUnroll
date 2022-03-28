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

## 感谢

[参考这篇文章进行编写](https://zhou-yuxin.github.io/articles/2016/用C语言宏批量生成代码的思考与实现)
