## 4.1

```shell
[sqrt serial]:          [702.568] ms
[sqrt ispc]:            [171.418] ms
[sqrt task ispc]:       [24.834] ms
                                (4.10x speedup from ISPC)
                                (28.29x speedup from task ISPC)
```

## 4.2

将values数组的所有值设置为2.999f，这样每次SIMD命令执行时，所有的标量迭代次数都相同，没有掩码的出现。其次根据README中的图，计算2.999f需要相当多的迭代次数。综上，这样的条件可以在控制变量的情况下充分体现出SIMD和多线程的优势。
```shell
[sqrt serial]:          [2260.202] ms
[sqrt ispc]:            [362.549] ms
[sqrt task ispc]:       [47.482] ms
                                (6.23x speedup from ISPC)
                                (47.60x speedup from task ISPC)
```

由多个task带来的加速比相比与4.1几乎是没有改变的，因为改变输入值，改变的是单核内SIMD不同标量的同步时间，而不影响不同核之间的同步时间。

## 4.3

将values数组的所有值设置为1.000f，能够取得最小的加速比。
```shell
[sqrt serial]:          [22.386] ms
[sqrt ispc]:            [13.314] ms
[sqrt task ispc]:       [15.205] ms
                                (1.68x speedup from ISPC)
                                (1.47x speedup from task ISPC)
```

当x值为1.000f时，每个标量的迭代次数都是0，对于每个标量来说其只需要执行的代码为：
```shell
float x = values[i];
float guess = initialGuess;
float error = fabs(guess * guess * x - 1.f);
output[i] = x * guess;
```

对于load、mul、sub、store等操作，SIMD和多线程能够进行并行加速。但是由于计算量不够大，此程序的性能**瓶颈并不是在迭代的计算**上，因此加速比并不明显。

甚至可以看到多线程之间的通信代价大于了并行的提升，导致多核上的SIMD比单核的SIMD反而取得了更低的加速比。