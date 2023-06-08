## 3.1

理论上能获得8x的加速，但是实际上只有不到5x的加速：

View1:
```sh
[mandelbrot serial]:            [264.699] ms
Wrote image file mandelbrot-serial.ppm
[mandelbrot ispc]:              [58.052] ms
Wrote image file mandelbrot-ispc.ppm
                                (4.56x speedup from ISPC)
```

View2:
```sh
[mandelbrot serial]:            [125.491] ms
Wrote image file mandelbrot-serial.ppm
[mandelbrot ispc]:              [30.963] ms
Wrote image file mandelbrot-ispc.ppm
                                (4.05x speedup from ISPC)
```
原因依然是在同一次矢量计算中，其中的每个标量的计算负载是不同的。因此，当我们使用ISPC时，我们只能获得每个矢量计算中最慢的标量的加速。
计算负载不同的部分主要出现在黑白过渡的部分，我们观察到View2的这些部分更多，因此它的加速效果更差。

## 3.2

1、使用了两个核心+SIMD后，取得了8x+的加速效果，并且是使用一个核心+SIMD的近两倍。
```shell
[mandelbrot serial]:            [211.001] ms
Wrote image file mandelbrot-serial.ppm
[mandelbrot ispc]:              [44.976] ms
Wrote image file mandelbrot-ispc.ppm
[mandelbrot multicore ispc]:    [25.402] ms
Wrote image file mandelbrot-task-ispc.ppm
                                (4.69x speedup from ISPC)
                                (8.31x speedup from task ISPC)
```

2、理论上来说应该task的数量等于超线程的数量，虽然我的机器是6个核心，但是逻辑核心的数量为12，因此理论上取得最大加速的task的数量应该是24，但是由于Height为800，为了整除，我将task的数量取为了25，得到了近35x的加速。
```shell
[mandelbrot serial]:            [286.957] ms
Wrote image file mandelbrot-serial.ppm
[mandelbrot ispc]:              [61.600] ms
Wrote image file mandelbrot-ispc.ppm
[mandelbrot multicore ispc]:    [8.269] ms
Wrote image file mandelbrot-task-ispc.ppm
                                (4.66x speedup from ISPC)
                                (34.70x speedup from task ISPC)
```

3、当我把task的数量提升至100甚至是800的时候，基本上都是维持在35x加速左右，并没有进一步的提升。可以发现ISPC的加速效果已经达到了极限，而task的数量的增加并没有带来更多的加速。但是当我们在prog1中，开尽可能多的线程时，并不能得到35x加速。
起初我猜测，随着task的数量的提升性能应该是会下降的，因为空闲线程的调度会带来更多的时间开销，但是并没有，可以初步认为ISPC对这种情况进行了优化。