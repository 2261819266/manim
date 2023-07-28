import array
from manimlib import *

class APhisicsProblem(Scene):
    def construct(self) -> None:

        introduce = Text(
            """
        在我初三的时候，曾经遇到过一道关于恒定功率汽车启动物理题目
        并且题目还附了一张v-t的函数图像

            """, 
            font = "Noto Sans CJK SC", font_size = 24, color = BLUE
        )

        self.play(Write(introduce), run_time = 5)
        self.play(introduce.animate.shift(UP * 3), run_time = 2)

        axes = Axes(
            x_range = (0, 2),
            y_range = (0, 8),
            axis_config = {
                "include_tip": True,
            },
        ).shift(DOWN * 2 + LEFT * 2)
        axes.flip(UR)
        # axes.add_coordinate_labels()

        self.play(FadeIn(axes))

        f = lambda v : (-math.log(1 - v) - v)

        # for v in np.arange(0, 1, 0.01):
        #     t = f(v)
        #     dot = Dot(axes.coords_to_point(v, t))
        #     self.add(dot)
        graph = axes.get_graph(f, x_range = (0, 0.9999, 0.002), color = BLUE)
        limit_line = DashedLine(axes.coords_to_point(1, 0), axes.coords_to_point(1, 8))
        self.play(Write(graph), Write(limit_line))


        

        self.wait()