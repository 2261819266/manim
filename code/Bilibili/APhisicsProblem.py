import array
from manimlib import *

FONT = "Noto Sans CJK SC"

class APhisicsProblem(Scene):
    def construct(self) -> None:

        introduce = Text(
            """
        在我初三的时候，曾经遇到过一道关于恒定功率汽车启动物理题目
        并且题目还附了一张v-t的函数图像

            """, 
            font = FONT, font_size = 24, color = BLUE
        )

        self.play(Write(introduce), run_time = 5)
        self.play(introduce.animate.shift(UP * 3), run_time = 2)

        axes = Axes(
            x_range = (0, 2),
            y_range = (0, 8),
            axis_config = {
                "include_tip": True,
            },
        ).shift(DOWN * 2 + LEFT * 1)
        axes.flip(UR)
        # axes.add_coordinate_labels()

        self.play(FadeIn(axes))

        f = lambda v : (-math.log(1 - v) - v)
        graph = axes.get_graph(f, x_range = (0, 0.9999, 0.002), color = BLUE)
        limit_line = DashedLine(axes.coords_to_point(1, 0), axes.coords_to_point(1, 8))
        self.play(Write(graph), Write(limit_line))


        explain_the_problem = VGroup(
            Text("题目描述大概是说在前一段时间汽车做加速运动，后面一段时间做匀速运动", font = FONT, font_size = 24, color = BLUE),
            Text("我当时的直觉就是汽车的速度应该只会无线逼近那个最大值但是不会达到", font = FONT, font_size = 24, color = BLUE),
            Text("那时只会一些导数和积分的知识的我试图证明它，", font = FONT, font_size = 24, color = BLUE),
            Text("我认为只要求出速度或加速度的解析式再积分一下就可以了", font = FONT, font_size = 24, color = BLUE),
            Text("可是怎么都写不出那个解析式，那时我就放弃了", font = FONT, font_size = 24, color = BLUE),
            # font = FONT, font_size = 24, color = BLUE, buff = 1
        )

        j = 3
        for i in explain_the_problem:
            self.play(Write(i.shift(UP * j / 2 )))
            j -= 1

        self.play(FadeOut(introduce), FadeOut(axes), FadeOut(explain_the_problem), FadeOut(limit_line), FadeOut(graph))
        self.wait()