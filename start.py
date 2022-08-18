from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        # 在水平方向上拉伸到四倍
        self.play(circle.animate.stretch(4, dim=0))
        # 旋转90°
        self.play(Rotate(circle, TAU / 4))
        # 在向右移动2单位同时缩小为原来的1/4
        self.play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))
        # 为了非线性变换，给circle增加10段曲线（不会播放动画）
        circle.insert_n_curves(10)
        # 给circle上的所有点施加f(z)=z^2的复变换
        self.play(circle.animate.apply_complex_function(lambda z: z**(-1/2)))
        # 关闭窗口并退出程序
        # exit()